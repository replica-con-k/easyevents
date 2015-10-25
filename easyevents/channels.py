#!/usr/bin/env python
# -*- coding: utf-8 -*-

import easyevents


class Subscriptor(object):
    def handle_event(self, event):
        pass

class EventChannel(Subscriptor):
    def __init__(self):
        self.__subscriptors = {}

    def add_subscriptor(self, subs_id, subscriptor):
        self.__subscriptors[subs_id] = subscriptor

    def unsubscribe(self, subs_id):
        if subs_id in self.__subscriptors.keys():
            del(self.__subscriptors[subs_id])

    @property
    def subscribers(self):
        return self.__subscriptors.keys()

    def handle_event(self, event):
        self.publish(event)

    def publish(self, event):
        for subscriptor in self.__subscriptors.values():
            subscriptor.handle_event(event)
