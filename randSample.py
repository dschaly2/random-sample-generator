import random
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GLib

counter = 0

class EntryWindow(Gtk.Window):
  
  def __init__(self):
    Gtk.Window.__init__(self, title="Random Sample Generator")
    self.set_border_width(10)
    self.set_size_request(500, 500)
    
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    self.add(vbox)
    
    self.popLabel = Gtk.Label("Enter Population Size:")
    self.pop = Gtk.Entry()
    vbox.pack_start(self.popLabel, True, True, 0)
    vbox.pack_start(self.pop, True, True, 0)

    self.sampLabel = Gtk.Label("Enter Sample Size:")
    self.samp = Gtk.Entry()
    vbox.pack_start(self.sampLabel, True, True, 0)
    vbox.pack_start(self.samp, True, True, 0)

    self.button = Gtk.Button(label="Submit")
    self.button.connect("clicked", self.submit)
    vbox.pack_start(self.button, True, True, 0)
  
  def submit(self, widget):
    global counter
    print("\n==============================================================================\n")
    while counter < int(self.samp.get_text()):
      print(str(counter+1) + ": " + str(random.randint(0, int(self.pop.get_text()))))
      counter += 1
    print("\nFrom population of:" + self.pop.get_text() + " a sample of:" + self.samp.get_text())
    self.destroy()
     

window = EntryWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
