


from flask import Blueprint, render_template
from flask import Flask, request, flash, redirect, url_for, render_template, abort, Response, json, jsonify, make_response, current_app, g, session

# from utils.responses import success_response, error_response
import psycopg2
import config
from datetime import timedelta
import uuid
# from views.decorators import *
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
from functools import update_wrapper


def crossdomain(origin=None, methods=None, headers=None, max_age=21600, attach_to_all=True, automatic_options=True):
    if methods is not None:
        methods = ', '.join(sorted(x.upper() for x in methods))
    if headers is not None and not isinstance(headers, basestring):
        # headers = ', '.join(x.upper() for x in headers)
        headers = '*'
    if not isinstance(origin, basestring):
        origin = ', '.join(origin)
    if isinstance(max_age, timedelta):
        max_age = max_age.total_seconds()

    def get_methods():
        if methods is not None:
            return methods

        options_resp = current_app.make_default_options_response()
        return options_resp.headers['allow']

    def decorator(f):
        def wrapped_function(*args, **kwargs):
            if automatic_options and request.method == 'OPTIONS':
                resp = current_app.make_default_options_response()
            else:
                resp = make_response(f(*args, **kwargs))
            if not attach_to_all and request.method != 'OPTIONS':
                return resp

            h = resp.headers

            h['Access-Control-Allow-Origin'] = origin
            h['Access-Control-Allow-Methods'] = get_methods()
            h['Access-Control-Max-Age'] = str(max_age)
            if headers is not None:
                h['Access-Control-Allow-Headers'] = headers
            h['Access-Control-Allow-Headers'] = '*'
            return resp

        f.provide_automatic_options = False
        return update_wrapper(wrapped_function, f)

    return decorator