#!/usr/bin/env python
"""
Main file to run api Application
"""
from app.router import APP_API

if __name__ == '__main__':
    APP_API.run(host='0.0.0.0', port=5000)
