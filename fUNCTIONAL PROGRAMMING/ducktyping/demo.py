class Vscode:
    def compile(self):
        print("Compiling using Vscode")
    def execute(self):
        print("Executing using Vscode")
    def debug(self):
        print("Debugging using Vscode")
class Pycharm:
    def compile(self):
        print("Compiling using Pycharm")
    def execute(self):
        print("Executing using Pycharm")
    def debug(self):
        print("Debugging using Pycharm")
class Programmer:
    def coding(self,ide):
        ide.compile()
        ide.execute()
        ide.debug()
dev=Programmer()
pvc=Pycharm()
vs=Vscode()

dev.coding(pvc)
dev.coding(vs)