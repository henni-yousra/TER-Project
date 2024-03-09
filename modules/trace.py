
import re

def read_trace(input_trace):
    
    sections = re.split(r'\.\s*\n\s*\.', input_trace)
    sections = [section.strip() for section in sections if section.strip()]
    
    sections.pop(0)
    sections.pop(0)

    keys = []
    for section in sections:
        print(f"Current section: {section}")
        
        match = re.search(r'([01]{5})', section)

        if match:
            key = match.group(1)  
            keys.append(key)   
            print(f"Found key: {key}")


    return sections

if __name__ == "__main__":
    trace_file_path = './data/trace.xtr'
    
    with open(trace_file_path, 'r') as trace_file:
        input_trace = trace_file.read()

    sections = read_trace(input_trace)


