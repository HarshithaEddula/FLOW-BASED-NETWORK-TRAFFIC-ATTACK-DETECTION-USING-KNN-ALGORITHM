from ._anvil_designer import Form1Template
from anvil import *
import anvil.server


class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    pred = anvil.server.call('predict',
                             self.text_box_1.text,
                             self.text_box_2.text,
                             self.text_box_3.text,
                             self.text_box_4.text,
                             self.text_box_5.text,
                             self.text_box_6.text,
                             self.text_box_7.text,
                             self.text_box_8.text,
                             self.text_box_9.text,
                             self.text_box_10.text,
                             self.text_box_11.text,
                             self.text_box_12.text,
                             self.text_box_13.text,
                             self.text_box_14.text,
                             self.text_box_15.text,
                             self.text_box_16.text,
                             self.text_box_17.text,
                             self.text_box_18.text,
                             self.text_box_19.text,
                             self.text_box_20.text,
                             self.text_box_21.text,
                             self.text_box_22.text,
                             self.text_box_23.text,
                             self.text_box_24.text,
                             self.text_box_25.text,
                             self.text_box_26.text,
                             self.text_box_27.text,
                             self.text_box_28.text,
                             self.text_box_29.text,
                             self.text_box_30.text
                             )
    if pred:
      self.result.visible =True
      self.result.text= pred
      
