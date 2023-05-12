from website import create_app  #when import name of the folder, we import anything defined in the folder

app = create_app()

if __name__ == '__main__':  #only if we run this file, we will execute the next line
    app.run(debug=True)   #run the application, any change will automically rerun 
    
