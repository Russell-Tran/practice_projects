z = __import__("2015_06")

def test_TurnInstruction():
	line = ['turn', 'off', '102,527', 'through', '650,747']
	instr = z.TurnInstruction(line)
	assert instr.on == False
	assert instr.lower_row == 102
	assert instr.lower_col == 527
	assert instr.upper_row == 650
	assert instr.upper_col == 747

	line = ['turn', 'on', '102,527', 'through', '650,747']
	instr = z.TurnInstruction(line)
	assert instr.on == True

def test_ToggleInstruction():
	instr = z.ToggleInstruction(['toggle', '70,253', 'through', '918,736'])
	assert instr.lower_row == 70
	assert instr.lower_col == 253
	assert instr.upper_row == 918
	assert instr.upper_col == 736
