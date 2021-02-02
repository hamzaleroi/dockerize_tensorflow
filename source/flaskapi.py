import tensorflow as tf

@app.route('/')
def main():
    return f"Hello from Flask, tf_version{tf.__version__}"
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
