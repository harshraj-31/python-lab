class textEditor:
  def __init__(self):
    self.editor = []
    self.output = ""
    self.mainOutput = ''

  def add_text(self, text):
    self.editor.append(text)
    print(self.editor)

  def undo(self):
    self.editor.remove(self.editor[-1])
    print(self.editor)

  def getText(self):
    self.mainOutput = self.output.join(self.editor)
    print(self.mainOutput)


te = textEditor()
# adding text
te.add_text('a')
te.add_text('b')
te.add_text('c')
te.add_text('d')
te.add_text('e')

#removing text -> UNDO
te.undo()

# displaying Editor
te.getText()
