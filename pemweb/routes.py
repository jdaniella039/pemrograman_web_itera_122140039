def includeme(config):
    config.add_route('home', '/')
    config.add_route('list_mahasiswa', '/mahasiswa')
    config.add_route('get_mahasiswa', '/mahasiswa/{id}')
    config.add_route('create_mahasiswa', '/mahasiswa/create')
    config.add_route('update_mahasiswa', '/mahasiswa/update/{id}')
    config.add_route('delete_mahasiswa', '/mahasiswa/delete/{id}')
