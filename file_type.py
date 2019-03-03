import pandas as pd

file_type = {
	'coding': ['python','.py','java','.c','.cpp','.html','css','.js','.ipynb'],
        'web': ['chrome','firefox','opera','edge'],
        'documentation' : ['.docx','.doc','.odt','.txt','docs'],
        'spread sheet' : ['.xls','.xlsx'],
        'presentation' : ['.ppt','.pptx']
}
#print(file_type)

keys = list(file_type.keys())



def get_file_type(data):
    
    for i in range(0,len(data)):
        for j in keys:
            for k in range(0,len(file_type[j])):
                if file_type[j][k] in data['file name'][i]:
                		data.loc[i,'file cat'] = j 
        
    return data
