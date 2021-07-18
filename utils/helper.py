def context_response(success, msg=None):

	return {
		'success': success,
		'messages': msg
	}

def set_kelas_klasifikasi(cf_combine):
	if (cf_combine >= 0.7):
		return 1
	else:
		return 0
