from pyramid.view import view_config
from pyramid.response import Response
from .models import DBSession, Mahasiswa
import json

@view_config(route_name='home', renderer='json')
def home(request):
    return {'message': 'API Mahasiswa aktif'}

@view_config(route_name='list_mahasiswa', renderer='json', request_method='GET')
def list_mahasiswa(request):
    mhs_list = DBSession.query(Mahasiswa).all()
    return [{'id': m.id, 'nama': m.nama, 'npm': m.npm, 'jurusan': m.jurusan} for m in mhs_list]

@view_config(route_name='get_mahasiswa', renderer='json', request_method='GET')
def get_mahasiswa(request):
    id = int(request.matchdict['id'])
    m = DBSession.query(Mahasiswa).get(id)
    if m:
        return {'id': m.id, 'nama': m.nama, 'npm': m.npm, 'jurusan': m.jurusan}
    return Response(json.dumps({'error': 'Not Found'}), status=404)

@view_config(route_name='create_mahasiswa', renderer='json', request_method='POST')
def create_mahasiswa(request):
    data = request.json_body
    m = Mahasiswa(nama=data['nama'], npm=data['npm'], jurusan=data['jurusan'])
    DBSession.add(m)
    return {'message': 'Mahasiswa ditambahkan'}

@view_config(route_name='update_mahasiswa', renderer='json', request_method='PUT')
def update_mahasiswa(request):
    id = int(request.matchdict['id'])
    m = DBSession.query(Mahasiswa).get(id)
    if not m:
        return Response(json.dumps({'error': 'Not Found'}), status=404)
    data = request.json_body
    m.nama = data['nama']
    m.npm = data['npm']
    m.jurusan = data['jurusan']
    return {'message': 'Mahasiswa diperbarui'}

@view_config(route_name='delete_mahasiswa', renderer='json', request_method='DELETE')
def delete_mahasiswa(request):
    id = int(request.matchdict['id'])
    m = DBSession.query(Mahasiswa).get(id)
    if not m:
        return Response(json.dumps({'error': 'Not Found'}), status=404)
    DBSession.delete(m)
    return {'message': 'Mahasiswa dihapus'}
