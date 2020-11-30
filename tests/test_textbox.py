import pglet

def test_textbox():
    tb = pglet.Textbox(id="txt1", label="Your name:")
    assert isinstance(tb, pglet.Control)
    assert isinstance(tb, pglet.Textbox)
    assert str(tb) == "textbox id=\"txt1\" label=\"Your name:\"", "Test failed"

def test_add_textbox():
    # open page
    p = pglet.page('page1', noWindow=True)

    tb_value = "Line1\nLine2\nLine3"

    # add textbox
    tb_id = p.add_textbox(value=tb_value, multiline=True)
    assert tb_id.startswith('_'), "Test failed"

    # get textbox value
    ret_tb_value = p.send(f"get {tb_id} value")
    assert ret_tb_value == tb_value, "Test failed"