class RecursiveDescentParser:
    def __init__(self):
        self.grammar = {}
        self.start_symbol = ""
    
    def input_grammar(self):
        non_terminals = input("Enter non-terminals (separated by commas): ").split(',')
        for nt in non_terminals:
            rules = input(f"Enter rules for non-terminal '{nt}' (separated by '|'): ").split('|')
            self.grammar[nt] = rules
        self.start_symbol = non_terminals[0]
    
    def is_simple(self):
        for nt in self.grammar:
            for rule in self.grammar[nt]:
                if any(symbol.isupper() for symbol in rule[1:]): 
                    return False
        return True
    
    def parse(self, string):
        stack = [self.start_symbol]
        input_str = list(string)
        
        while stack and input_str:
            top = stack.pop()
            if top.isupper():  
                rule_applied = False
                for rule in self.grammar[top]:
                    if rule[0] == input_str[0]:
                        stack.extend(reversed(rule))
                        rule_applied = True
                        break
                if not rule_applied:
                    return False
            else:  
                if top == input_str[0]:
                    input_str.pop(0)
                else:
                    return False
        
        return not stack and not input_str
    
    def run(self):
        while True:
            print("\n👇 Grammars 👇")
            self.input_grammar()
            
            if self.is_simple():
                print("The Grammar is simple.")
            else:
                print("The Grammar isn't simple.")
            
            while True:
                string = input("Enter the string you want to check: ")
                if self.parse(string):
                    print("Your input string is Accepted.")
                else:
                    print("Your input string is Rejected.")
                
                
                choice = input("\n1-Another Grammar.\n2-Another String.\n3-Exit\nEnter your choice: ")
                
                if choice == '1':
                    break  
                elif choice == '2':
                    continue  
                elif choice == '3':
                    print("Exiting...")
                    return
                else:
                    print("Invalid choice, try again.")

parser = RecursiveDescentParser()
parser.run()





