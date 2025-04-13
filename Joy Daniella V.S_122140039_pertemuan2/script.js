class Item {
    constructor(id, text) {
      this.id = id;
      this.text = text;
    }
  }
  
  const scheduleList = document.getElementById('scheduleList');
  const taskList = document.getElementById('taskList');
  const savedNote = document.getElementById('savedNote');
  
  // ⏰ Real-time clock
  const updateClock = () => {
    const now = new Date();
    document.getElementById('clock').textContent = now.toLocaleTimeString();
  };
  setInterval(updateClock, 1000);
  
  // 🔄 Load data from localStorage
  const loadItems = (key) => JSON.parse(localStorage.getItem(key)) || [];
  
  // 💾 Save data to localStorage
  const saveItems = (key, items) => localStorage.setItem(key, JSON.stringify(items));
  
  // 🔄 Render list
  const renderList = (listEl, items, key) => {
    listEl.innerHTML = '';
    items.forEach(item => {
      listEl.innerHTML += `
        <li>
          ${item.text}
          <button onclick="removeItem('${item.id}', '${key}')">🗑</button>
        </li>
      `;
    });
  };
  
  // ➕ Add item
  const addItem = (key, inputId, listEl) => {
    const text = document.getElementById(inputId).value.trim();
    if (text) {
      const items = loadItems(key);
      const newItem = new Item(Date.now().toString(), text);
      items.push(newItem);
      saveItems(key, items);
      renderList(listEl, items, key);
      document.getElementById(inputId).value = '';
    }
  };
  
  const addSchedule = () => addItem('schedule', 'scheduleInput', scheduleList);
  const addTask = () => addItem('tasks', 'taskInput', taskList);
  
  // ❌ Remove item
  const removeItem = (id, key) => {
    const items = loadItems(key).filter(item => item.id !== id);
    saveItems(key, items);
    const listEl = key === 'schedule' ? scheduleList : taskList;
    renderList(listEl, items, key);
  };
  
  // 📝 Notes (async/await)
  const saveNote = async () => {
    const note = document.getElementById('noteInput').value;
    await localStorage.setItem('note', note);
    savedNote.textContent = note;
  };
  
  const init = () => {
    renderList(scheduleList, loadItems('schedule'), 'schedule');
    renderList(taskList, loadItems('tasks'), 'tasks');
    savedNote.textContent = localStorage.getItem('note') || '';
  };
  init();
  
  // 🔄 Tab switching
  document.querySelectorAll('.tab').forEach(tab => {
    tab.addEventListener('click', () => {
      document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.tab-content').forEach(c => c.classList.add('hidden'));
      tab.classList.add('active');
      document.getElementById(tab.dataset.tab).classList.remove('hidden');
    });
  });
  