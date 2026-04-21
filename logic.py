# logic.py

class CalculatorBackend:
    def __init__(self):
        self.current_value = ""
        self.previous_value = 0
        self.operation = None
        self.new_num_expected = False

    def process_input(self, action):
        """
        Main entry point for all button presses.
        Returns the string that should be displayed on the screen.
        """
        if action.isdigit():
            return self._handle_number(action)
        elif action == "C":
            return self._all_clear()
        elif action == "=":
            return self._calculate()
        else:
            return self._handle_operator(action)

    def _handle_number(self, num):
        if self.new_num_expected:
            self.current_value = ""
            self.new_num_expected = False
        
        if num == "0" and self.current_value == "0":
            return "0"
            
        self.current_value += num
        return self.current_value

    def _handle_operator(self, op):
        if self.current_value == "": return "0"
        
        if self.operation:
            self._calculate()
            
        self.previous_value = float(self.current_value)
        self.operation = op
        self.new_num_expected = True
        return self.current_value

    def _calculate(self):
        if not self.operation or self.current_value == "":
            return self.current_value or "0"

        try:
            val2 = float(self.current_value)
            match self.operation:
                case "+": res = self.previous_value + val2
                case "-": res = self.previous_value - val2
                case "*": res = self.previous_value * val2
                case "/": res = self.previous_value / val2 if val2 != 0 else "Error"
            
            # Format result
            formatted_res = str(int(res)) if isinstance(res, float) and res.is_integer() else f"{res:.8g}"
            self.current_value = formatted_res
            self.operation = None
            self.new_num_expected = True
            return formatted_res
        except:
            return "Error"

    def _all_clear(self):
        self.current_value = ""
        self.previous_value = 0
        self.operation = None
        return "0"