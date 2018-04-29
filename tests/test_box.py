from guizero import App, Box, Text
from common_test import (
    schedule_after_test,
    schedule_repeat_test,
    destroy_test,
    display_test, 
    color_test, 
    size_pixel_test,
    events_test)

def test_default_values():
    a = App()
    b = Box(a)
    assert b.master == a
    assert b.layout == "auto"
    assert b.grid == None
    assert b.align == None
    a.destroy()

def test_alt_values():
    a = App(layout = "grid")
    b = Box(a, layout="grid", grid=[0,1], align="top")
    assert b.layout == "grid"
    assert b.grid[0] == 0
    assert b.grid[1] == 1
    assert b.align == "top"
    a.destroy()

def test_after_schedule():
    a = App()
    b = Box(a)
    schedule_after_test(a, b)
    a.destroy()

def test_repeat_schedule():
    a = App()
    b = Box(a)
    schedule_repeat_test(a, b)
    a.destroy()

def test_destroy():
    a = App()
    b = Box(a)
    destroy_test(b)
    a.destroy()

def test_display():
    a = App()
    b = Box(a)
    display_test(b)
    a.destroy()

def test_color():
    a = App()
    b = Box(a)
    color_test(b)
    a.destroy()

def test_size():
    a = App()
    b = Box(a)
    size_pixel_test(b)
    a.destroy()

def test_events():
    a = App()
    b = Box(a)
    events_test(b)
    a.destroy()

def test_cascading_properties():
    a = App()
    b = Box(a)
    t = Text(b)

    a.bg = "red"
    a.text_color = "purple"
    a.text_size = 16
    a.font = "Times New Roman"
    
    assert b.bg == "red"
    assert b.text_color == "purple"
    assert b.text_size == 16
    assert b.font == "Times New Roman"
    
    assert t.bg == "red"
    assert t.text_color == "purple"
    assert t.text_size == 16
    assert t.font == "Times New Roman"
    
    b.bg = "green"
    b.text_color = "yellow"
    b.text_size = 18
    b.font = "Courier New"

    assert a.bg == "red"
    assert a.text_color == "purple"
    assert a.text_size == 16
    assert a.font == "Times New Roman"

    assert b.bg == "green"
    assert b.text_color == "yellow"
    assert b.text_size == 18
    assert b.font == "Courier New"
    
    assert t.bg == "green"
    assert t.text_color == "yellow"
    assert t.text_size == 18
    assert t.font == "Courier New"
    
    a.destroy()

def test_inherited_properties():
    a = App()
    a.bg = "red"
    a.text_color = "purple"
    a.text_size = 16
    a.font = "Times New Roman"
    
    b = Box(a)
    assert b.bg == "red"
    assert b.text_color == "purple"
    assert b.text_size == 16
    assert b.font == "Times New Roman"
    
    b.bg = "green"
    b.text_color = "yellow"
    b.text_size = 18
    b.font = "Courier New"
    
    t = Text(b)
    assert t.bg == "green"
    assert t.text_color == "yellow"
    assert t.text_size == 18
    assert t.font == "Courier New"
    
    a.destroy()
