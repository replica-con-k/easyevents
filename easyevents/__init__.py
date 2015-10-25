#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

'''Event handling using pygame.'''

__all__ = ['channels']

import pygame

KEYUP = pygame.KEYUP
KEYDOWN = pygame.KEYDOWN

K_LEFT = pygame.K_LEFT
K_RIGHT = pygame.K_RIGHT
K_SPACE = pygame.K_SPACE

import channels

ROOT = channels.EventChannel()

def process_events():
    for event in pygame.event.get():
        ROOT.publish(event)

def new_channel(channel_name):
    event_channel = channels.EventChannel()
    ROOT.add_subscriptor(channel_name, event_channel)
    return event_channel

def remove_channel(channel_name):
    ROOT.unsubscribe(channel_name)
    
