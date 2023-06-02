# server.py
import socket
import json


# Body Mass Index (BMI)
def generate_imc(data):
    """
    Calculate the Body Mass Index (BMI) based on the provided data.

    Parameters:
    - data (dict): A dictionary containing the 'altura' (height) and 'peso' (weight) values.

    Returns:
    - float: The calculated BMI.
    """
    height = data['altura']
    weight = data['peso']
    return round(float(weight / (height * height)), 2)


# BMI Status
def analyse_imc(imc):
    """
    Analyze the Body Mass Index (BMI) and determine its status.

    Parameters:
    - imc (float): The calculated BMI value.

    Returns:
    - str: The status of the BMI.
    """
    if 0 < imc < 18.5:
        status = "Underweight!"
    elif imc <= 24.9:
        status = "Normal weight!"
    elif imc <= 29.9:
        status = "Overweight!"
    elif imc <= 34.9:
        status = "Obesity Class 1!"
    elif imc <= 39.9:
        status = "Obesity Class 2!"
    elif imc <= 40.0:
        status = "Obesity Class 1!"
    else:
        status = "Invalid values"
    return status


# Basal Metabolic Rate (BMR)
def generate_tmb(data):
    """
    Calculate the Basal Metabolic Rate (BMR) based on the provided data.

    Parameters:
    - data (dict): A dictionary containing the 'sexo' (sex), 'peso' (weight),
    'altura' (height), and 'idade' (age) values.

    Returns:
    - float: The calculated BMR.
    """
    sex = data['sexo']
    if sex in 'Mm':
        tmb = 5 + (10 * data['peso']) + (6.25 * (data['altura'] * 100)) - (5 * data['idade'])
    else:
        tmb = (10 * data['peso']) + (6.25 * (data['altura'] * 100)) - (5 * data['idade']) - 5
    return tmb


def generate_cal(data):
    """
    Calculate the daily caloric intake based on the provided data.

    Parameters:
    - data (dict): A dictionary containing the 'nvlAtiv' (activity level) and 'tmb' (basal metabolic rate) values.

    Returns:
    - float: The calculated daily caloric intake.
    """
    if data['nvlAtiv'] == 1:
        fator_ativ = 1.2
    elif data['nvlAtiv'] == 2:
        fator_ativ = 1.375
    elif data['nvlAtiv'] == 3:
        fator_ativ = 1.725
    else:
        fator_ativ = 1.9
    return round((data['tmb'] * fator_ativ), 2)


def generate_nutrients(data):
    """
    Calculate the recommended nutrient intake based on the provided data.

    Parameters:
    - data (dict): A dictionary containing the 'cal' (calories) value.

    Returns:
    - dict: A dictionary containing the calculated values for 'carboidratos' (carbohydrates),
    'proteinas' (proteins), and 'gorduras' (fats).
    """
    carb = str(round((data['cal'] * 0.45), 2))
    prot = str(round((data['cal'] * 0.3), 2))
    fat = str(round((data['cal'] * 0.25), 2))
    return {"carboidratos": carb, "proteinas": prot, "gorduras": fat}


def run_server():
    # Create a socket object
    print('ECHO SERVER for BMI calculation')
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the local machine name
    host = '127.0.0.1'
    port = 9999

    # Bind to the port
    server_socket.bind((host, port))

    # Start listening for requests
    server_socket.listen()
    print('Service running on port {}.'.format(port))

    while True:
        # Establish a connection
        client_socket, addr = server_socket.accept()
        print('Connected to {}'.format(str(addr)))

        # Receive client data
        received = client_socket.recv(1024).decode()

        print('Received data from the client: {}'.format(received))

        # Server processing
        received = json.loads(received)

        # Add the BMI to data sent by the user
        received['imc'] = generate_imc(received)

        # Add the status of the BMI to data sent by the user
        received['statusImc'] = analyse_imc(received['imc'])

        # Add the BMR to data sent by the user
        received['tmb'] = generate_tmb(received)

        # Add the daily caloric intake to data sent by the user
        received['cal'] = generate_cal(received)

        # Add the nutrients to data sent by the user
        received["nutrientes"] = generate_nutrients(received)
        print('The result of processing is {}'.format(received))

        # Serializing the result
        result = json.dumps(received)

        # Send the result
        client_socket.send(result.encode('ascii'))
        print('Client data sent successfully!')

        # Finish the connection
        client_socket.close()


run_server()
