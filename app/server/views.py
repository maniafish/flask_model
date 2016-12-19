import ujson as json
from . import main
from flask import request


def re_format(retcode, retmsg):
    """keep return format consistently"""
    return json.dumps({'retcode': retcode, 'msg': retmsg}, ensure_ascii=False)


@main.route('/weixinoauth', methods=['GET', 'POST'])
def weixinoauth_page():
    code = request.values.get('code', '').encode('utf-8')
    state = request.values.get('state', '').encode('utf-8')
    print 'code: {0}'.format(code)
    print 'state: {0}'.format(state)
    return re_format(0, 'success')
