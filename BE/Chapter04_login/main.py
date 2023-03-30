import uvicorn


# pass Enter PEM pass phrase: it03
if __name__ == "__main__":
    uvicorn.run('projects.run:app', host='0.0.0.0',
                port=200, reload=True, log_level="info")
