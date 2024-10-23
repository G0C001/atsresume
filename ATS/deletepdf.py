import os
def delete_pdf_files(directory):
    
    if os.path.exists(directory):
        
        for filename in os.listdir(directory):
            
            if filename.endswith(".pdf"):
                
                file_path = os.path.join(directory, filename)
                try:
                    
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Error deleting {file_path}: {e}")
