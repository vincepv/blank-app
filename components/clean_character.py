
def clean_character(data_frame):
    
	clean_dict = {
		'Ã©' : 'é',
		'Ã¨' : 'è',
		'Ã«' : 'ë',
		'Ã§' : 'ç',
		'Ã®' : 'î',
		'Ã‰' : 'E',
		'Ã”' : 'O',
		'Ã¢' : 'â',
		'Ã¯' : 'ï',
		'Ã´' : 'ô',
		'Ãª' : 'ê',
		'Ãˆ' : 'E',
		'Ã' : 'E',
		'Ο©':'é',
		'Οß':'c',
		'ΟΪ':'e',
		'Ο®':'è',
		'Ο¥':'o',
		'Ο°':'i',
		'Ο·':'i',

	}

	data_frame = data_frame.replace(clean_dict, regex=True)
	return data_frame