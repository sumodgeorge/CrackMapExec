#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class database:

    def __init__(self, conn):
        self.conn = conn

    @staticmethod
    def db_schema(db_conn):
        db_conn.execute('''CREATE TABLE "credentials" (
            "id" integer PRIMARY KEY,
            "username" text,
            "password" text
            )''')

        db_conn.execute('''CREATE TABLE "hosts" (
            "id" integer PRIMARY KEY,
            "ip" text,
            "port" integer,
            "server_banner" text
            )''')
