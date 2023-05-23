from setuptools import setup

readme = open("./README.md", "r")

setup(
    name='consultanitbolivia',
    packages=['consultanitbolivia'],  # this must be the same as the name above
    version='0.1',
    description='Este paquete le permite verificar el ESTADO ACTUAL DEL NIT, en caso de no existir retorna un mensaje indicando que no existe.',
    long_description=readme.read(),
    long_description_content_type='text/markdown',
    author='Giovanni Vega',
    # use the URL to the github repo
    url='https://github.com/zxvega/consulta-nit-bolivia',
    install_requires=['requests'],
    keywords=[],
    classifiers=[ ],
    license='MIT',
    include_package_data=True   
)