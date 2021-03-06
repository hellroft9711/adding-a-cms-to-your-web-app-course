from pyramid.httpexceptions import HTTPNotFound
from pyramid.request import Request
from pyramid.response import Response
from pyramid.view import view_config

from pypi.services import cms_service


@view_config(route_name='cms_request')  # , renderer='pypi:templates/home/index.pt')
def cms_request(request: Request):
    sub_path = request.matchdict.get('sub_path')
    url = '/'.join(sub_path)

    page = cms_service.get_page(url)
    if not page:
        raise HTTPNotFound()

    return Response(body=f"Title: {page.get('title')}, Contents: {page.get('contents')}")
