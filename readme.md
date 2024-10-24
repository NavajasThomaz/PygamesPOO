<img align="center" style='position: fixed' width=50 src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/06/Logo_FURG_institucional.png/598px-Logo_FURG_institucional.png" />
<div align="center">
<img align="center" width=500 src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Pygame_logo.svg/1280px-Pygame_logo.svg.png" />
<h1>Programação Orientada a Objeto</h>
</div>


##### <div align="center">🧱Esse projeto é uma base para produzir um jogo 2D com pygames.🧱</div>

<div align="center">

[![Readme Card](https://github-readme-stats.vercel.app/api/pin/?username=NavajasThomaz&repo=PygamesPOO&theme=transparent)](https://github.com/NavajasThomaz/PygamesPOO)

</div>



### <div align="center">Thomaz Colalillo Navajas - 140560</div>
<div style="display: inline_block", align="center">
    <a href = "mailto:thomaznavajas@gmail.com"><img src="https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white" target="_blank"></a>
    <a href="www.linkedin.com/in/thomaz-navajas" target="_blank"><img src="https://img.shields.io/badge/-LinkedIn-%230077B5?style=for-the-badge&logo=linkedin&logoColor=white" target="_blank"></a> 
    <a href="https://github.com/NavajasThomaz" target="_blank"><img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" target="_blank"></a>
    <a href="https://www.kaggle.com/thomaznavajas" target="_blank"><img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white" target="_blank"></a>

</div>
<div>
    <details open>
        <summary>

# Sumário</summary>

1. [Introdução](#Introdução)
2. [Implementação](#Implementação)
3. [Instruções](#Instruções)

    </details>
</div>
<details open>
<summary>

# Introdução</summary>

### Objetivo
O projeto visa implementar um programa em PyGames que renderiza uma tela personalizada com a capacidade de aceitar classes customizadas. O cubo é renderizado com iluminação e tonalização, e é possível interagir com ele, movendo-o, rotacionando-o e escalonando-o.

### Ferramentas
<div style=display:inline-block>
<img align="center" width=100 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" />
Linguagem escolhida
</div>
<div>
<img align="center" width=100 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/opengl/opengl-original.svg" />
Biblioteca gráfica para renderização de gráficos 3D.
</div>
<div>
<img align="center" width=100 src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/numpy/numpy-original-wordmark.svg" />
Biblioteca numérica para operar com vetores e matrizes.
</div>
<div>
<img align="center" width=50 src="https://pypi.org/static/images/logo-small.8998e9d1.svg" />
Bibliotecas como GLM w GLFW para gerenciar janelas, eventos, operações de vetores e matrizes.
</div>
</details>

https://drive.google.com/file/d/13srzcwzpOeTazTBZgbHbo_Yagwuhpp2l/view?usp=drive_link


<details open>
<summary>

# Implementação</summary>

###
Essa seção explica o passo a passo da implementação do programa em OpenGL.

1. **Bibliotecas utilizadas:** Na introdução falamos sobre as ferramentas que utilizamos e aqui mostraremos as bibliotecas utilizadas importadas no inicio do código.
```Console
python -m venv venv
```
```Console
venv/Scripts/activate
```
```Console
python main.py
```
```Python
import glfw  # Importa a biblioteca GLFW para criar janelas e gerenciar eventos
import imgui  # Importa a biblioteca ImGui para criar interfaces gráficas
import math  # Biblioteca para operações matemáticas
import glm  # Biblioteca para operações matemáticas de gráficos
import ctypes  # Biblioteca para interação com C/C++
import numpy as np  # Biblioteca para manipulação de arrays
from imgui.integrations.glfw import GlfwRenderer  # Renderer de ImGui para GLFW
from OpenGL.GL import *  # Importa todas as funções da biblioteca OpenGL
from PIL import Image  # Biblioteca para manipulação de imagens

SCREEN_WIDTH = 1280 # Constantes para definir o tamanho da janela
SCREEN_HEIGHT = 720 #
```
2. **Configuração do ambiente:** Fizemos duas classes, uma para janela inicial e outra para a aplicação da OpenGL.

<div align="center">
    <img src="https://github.com/NavajasThomaz/OpenGL_C3/blob/main/avaliacao_CG/Diagrama_das_Classes.png?raw=true"/>
</div>



- Janela inicial

```Python
class StartScreen:
    def __init__(self):
        self.window = glfw.create_window(                 # Instancia a janela
                                        SCREEN_WIDTH, 
                                        SCREEN_HEIGHT, 
                                        "Tela Inicial", 
                                        None, 
                                        None
                                        )
        glfw.make_context_current(self.window)            # Coloca a janela como contexto
        imgui.create_context()
        self.impl = GlfwRenderer(self.window)             # Instancia o renderer da Glfw
        self.start_game = False

    def show(self):
        while not glfw.window_should_close(self.window):  # Loop principal da janela
            glfw.poll_events()                            # Processa os eventos
            self.impl.process_inputs()                    # Processa os inputs do usuário
            imgui.new_frame()                             # Cria um novo frame
            imgui.begin("Bem-vindo!", closable=False)     # Inicia um novo frame
            if imgui.button("Iniciar"):                   # Cria um botão para iniciar a simulação
                self.start_game = True
                glfw.set_window_should_close(self.window, True)
            imgui.end()

            imgui.render()
            self.impl.render(imgui.get_draw_data())
            glfw.swap_buffers(self.window)

        self.impl.shutdown()
        glfw.destroy_window(self.window)
```

- Janela do OpenGL

A classe criada para essa janela é mais complexa doque a anterior, pois ela possue funções para o funcionamento da OpenGl.

#### Inicialização da janela

```Python
class OpenGLApp:
    def __init__(self):
        
        # Instancia a janela do glfw
        self.window = glfw.create_window(SCREEN_WIDTH, SCREEN_HEIGHT, "C3_Logo", None, None)
        
        self.projecao = 0 # Tipo de projeção atual | 0 perspectiva, 1 ortogonal
        self.trans_values = [0.0, 0.0, 0.0] # Vetor de translação
        self.rot_values = [0.0, 0.0, 0.0] # Vetor de rotação
        self.scale_value = 0.0 # Coeficiente de escala
        
        if not self.window:
            glfw.terminate()
            raise Exception("GLFW window can't be created!")

        glfw.make_context_current(self.window) # Define a janela atual como contexto
        glfw.set_input_mode(self.window, glfw.CURSOR, glfw.CURSOR_DISABLED) # Desabilita o cursor
        
        # Set background color
        glClearColor(0.6, 0.7, 1.0, 1.0)

        # Enable depth testing
        glEnable(GL_DEPTH_TEST)

        # Compile the shaders
        self.shader = self.create_shader_program("shaders/vertex_shader.glsl", "shaders/fragment_shader.glsl")

        # Get uniform locations
        self.projection_loc = glGetUniformLocation(self.shader, "projection") # Localização da projeção
        self.view_loc = glGetUniformLocation(self.shader, "view") # Localização da view
        self.model_loc = glGetUniformLocation(self.shader, "model") # Localização da model
        self.luz_pos_loc = glGetUniformLocation(self.shader, "lightPos") # Localização da posição da luz
        self.luz_cor_loc = glGetUniformLocation(self.shader, "lightColor") # Localização das cores da luz
        self.camera_pos_loc = glGetUniformLocation(self.shader, "viewPos") # Localização da posição da camera

        # Camera settings
        self.camera_pos = glm.vec3(0.0, 1.0, 3.0) # Poisção inicial
        self.camera_front = glm.vec3(0.0, 0.0, -1.0) # Direção inicial
        self.camera_up = glm.vec3(0.0, 1.0, 0.0) # Direção inicial
        self.yaw = -90.0 # Rotação inicial
        self.pitch = 0.0 # Rotação inicial
        self.last_x = SCREEN_WIDTH/4  # Ultima posição x do mouse
        self.last_y = SCREEN_HEIGHT/4 # Ultima posição y do mouse
        
        glfw.set_cursor_pos_callback(self.window, self.mouse_callback)

        # Timing
        self.delta_time = 0.0
        self.last_frame = 0.0
        
        # Textura
        self.texture = self.create_texture("Textures/logoFurg.png")
```



#### Criação do cubo



<div align='center'>

Essa função cria o **Vertex Array Object** e o **Vertex Buffer Object** do cubo, ja com o mapeamento de coordenadas das texturas e as normais.

<img src="https://blogger.googleusercontent.com/img/a/AVvXsEgHH1F9U8J1GdqKNNxOnkc1eu8rhuDOYhEhhkzNagpHdu5S4Uha9x-i11CQvy2Wvj8nm4TEgc7lv-hQZ993nqhiE6-hIki6_9NvMY0Valt8CLD9Dy-PH6qufiKLbVshiT4ZFARznVHgjNL0vPyqET1-Vt0FRR6WYNZ1Xunuz6brCWlgTJEyxqZBp4dm=w400-h175"/>

**Vertex Array Object (VAO)** é um objeto que armazena todas as configurações necessárias para a especificação dos dados de vértice que serão usados nas operações de desenho.

**O Vertex Buffer Object (VBO)** é um buffer que armazena dados de vértices na memória da GPU. Isso pode incluir coordenadas de vértices, cores, coordenadas de textura, normais, e outros dados de vértice. O VBO é utilizado para enviar grandes quantidades de dados de vértice para a GPU de uma só vez, o que é muito mais eficiente do que enviar dados um vértice de cada vez.

</div>


```Python
    def create_cube(self):
        """Cria um cubo com coordenadas de textura e vetores normais."""
        vertices = [
            # x     y     z     u    v    norx nory norz
            -0.5, -0.5, -0.5,  0.0, 0.0,  0.0, 0.0, -1.0,
             0.5, -0.5, -0.5,  1.0, 0.0,  0.0, 0.0, -1.0,
             0.5,  0.5, -0.5,  1.0, 1.0,  0.0, 0.0, -1.0,
             0.5,  0.5, -0.5,  1.0, 1.0,  0.0, 0.0, -1.0,
            -0.5,  0.5, -0.5,  0.0, 1.0,  0.0, 0.0, -1.0,
            -0.5, -0.5, -0.5,  0.0, 0.0,  0.0, 0.0, -1.0,

            -0.5, -0.5,  0.5,  0.0, 0.0,  0.0, 0.0, 1.0,
             0.5, -0.5,  0.5,  1.0, 0.0,  0.0, 0.0, 1.0,
             0.5,  0.5,  0.5,  1.0, 1.0,  0.0, 0.0, 1.0,
             0.5,  0.5,  0.5,  1.0, 1.0,  0.0, 0.0, 1.0,
            -0.5,  0.5,  0.5,  0.0, 1.0,  0.0, 0.0, 1.0,
            -0.5, -0.5,  0.5,  0.0, 0.0,  0.0, 0.0, 1.0,

            -0.5,  0.5,  0.5,  1.0, 0.0, -1.0, 0.0, 0.0,
            -0.5,  0.5, -0.5,  1.0, 1.0, -1.0, 0.0, 0.0,
            -0.5, -0.5, -0.5,  0.0, 1.0, -1.0, 0.0, 0.0,
            -0.5, -0.5, -0.5,  0.0, 1.0, -1.0, 0.0, 0.0,
            -0.5, -0.5,  0.5,  0.0, 0.0, -1.0, 0.0, 0.0,
            -0.5,  0.5,  0.5,  1.0, 0.0, -1.0, 0.0, 0.0,

             0.5,  0.5,  0.5,  1.0, 0.0,  1.0, 0.0, 0.0,
             0.5,  0.5, -0.5,  1.0, 1.0,  1.0, 0.0, 0.0,
             0.5, -0.5, -0.5,  0.0, 1.0,  1.0, 0.0, 0.0,
             0.5, -0.5, -0.5,  0.0, 1.0,  1.0, 0.0, 0.0,
             0.5, -0.5,  0.5,  0.0, 0.0,  1.0, 0.0, 0.0,
             0.5,  0.5,  0.5,  1.0, 0.0,  1.0, 0.0, 0.0,

            -0.5, -0.5, -0.5,  0.0, 1.0,  0.0, -1.0, 0.0,
             0.5, -0.5, -0.5,  1.0, 1.0,  0.0, -1.0, 0.0,
             0.5, -0.5,  0.5,  1.0, 0.0,  0.0, -1.0, 0.0,
             0.5, -0.5,  0.5,  1.0, 0.0,  0.0, -1.0, 0.0,
            -0.5, -0.5,  0.5,  0.0, 0.0,  0.0, -1.0, 0.0,
            -0.5, -0.5, -0.5,  0.0, 1.0,  0.0, -1.0, 0.0,

            -0.5,  0.5, -0.5,  0.0, 1.0,  0.0, 1.0, 0.0,
             0.5,  0.5, -0.5,  1.0, 1.0,  0.0, 1.0, 0.0,
             0.5,  0.5,  0.5,  1.0, 0.0,  0.0, 1.0, 0.0,
             0.5,  0.5,  0.5,  1.0, 0.0,  0.0, 1.0, 0.0,
            -0.5,  0.5,  0.5,  0.0, 0.0,  0.0, 1.0, 0.0,
            -0.5,  0.5, -0.5,  0.0, 1.0,  0.0, 1.0, 0.0
        ]
        vertices = np.array(vertices, dtype=np.float32)

        vao = glGenVertexArrays(1) # Vertex Array Object
        vbo = glGenBuffers(1) # Vertex Buffer Object
        
        glBindVertexArray(vao) # Vincula o vao
        glBindBuffer(GL_ARRAY_BUFFER, vbo) # Vincula o tipo de buffer
        glBufferData(GL_ARRAY_BUFFER, vertices.nbytes, vertices, GL_STATIC_DRAW) # Envia os dados dos vértices para o buffer

        # Posição dos vértices
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 8 * vertices.itemsize, ctypes.c_void_p(0))
        glEnableVertexAttribArray(0)
        """
        Aponta para os valores de coordenadas
        vertices = [ x     y     z
                   -0.5, -0.5, -0.5,  0.0, 0.0, 0.0, 0.0, -1.0,
                    0.5, -0.5, -0.5,  1.0, 0.0, 0.0, 0.0, -1.0,
                    0.5,  0.5, -0.5,  1.0, 1.0, 0.0, 0.0, -1.0,
                    ...
                   ]
        """
        
        # Coordenadas de textura
        glVertexAttribPointer(1, 2, GL_FLOAT, GL_FALSE, 8 * vertices.itemsize, ctypes.c_void_p(3 * vertices.itemsize))
        glEnableVertexAttribArray(1)
        """
        Aponta para os valores de texturas
        vertices = [                    u    v
                   -0.5, -0.5, -0.5,  0.0, 0.0, 0.0, 0.0, -1.0,
                    0.5, -0.5, -0.5,  1.0, 0.0, 0.0, 0.0, -1.0,
                    0.5,  0.5, -0.5,  1.0, 1.0, 0.0, 0.0, -1.0,
                    ...
                   ]
        """

        # Vetores das normais
        glVertexAttribPointer(2, 3, GL_FLOAT, GL_FALSE, 8 * vertices.itemsize, ctypes.c_void_p(5 * vertices.itemsize))
        glEnableVertexAttribArray(1)
        """
        Aponta para os valores dos vetores normais
        vertices = [                             x    y    z
                   -0.5, -0.5, -0.5,  0.0, 0.0, 0.0, 0.0, -1.0,
                    0.5, -0.5, -0.5,  1.0, 0.0, 0.0, 0.0, -1.0,
                    0.5,  0.5, -0.5,  1.0, 1.0, 0.0, 0.0, -1.0,
                    ...
                   ]
        """

        glBindVertexArray(0) # Desvincula o vao
        return vao, vbo
```


<div align='center'>
<img align="center" height=300 src="https://docs.hektorprofe.net/cdn/graficos3d/image-84.png" />
<img align="center" width=373 src="https://docs.hektorprofe.net/cdn/graficos3d/image-82.png" />
</div>


#### Criação da textura

```Python
from PIL import image
```
<div align='center'>
<img align="center"  src="https://pillow.readthedocs.io/en/stable/_static/pillow-logo.png" />

Utilizamos a biblioteca pillow para ler a imagem png da textura e converter para RGBA.
</div>


```Python
    def create_texture(self, texture_path):
        """ Cria uma textura OpenGL a partir de um objeto Image. """
        texture = glGenTextures(1)  # Gera um ID para uma nova textura
        glBindTexture(GL_TEXTURE_2D, texture)  # Vincula a textura como uma textura 2D

        # Define parâmetros de wrapping da textura
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)

        # Define parâmetros de filtragem da textura
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)

        # Carrega a imagem
        image = Image.open(texture_path)
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
        img_data = image.convert("RGBA").tobytes()
        glTexImage2D(GL_TEXTURE_2D,  # Define os dados da imagem para a textura
                    0,
                    GL_RGBA, # formato da textura
                    image.width, # largura
                    image.height, # altura
                    0,
                    GL_RGBA,
                    GL_UNSIGNED_BYTE, 
                    img_data)
        glGenerateMipmap(GL_TEXTURE_2D)

        glBindTexture(GL_TEXTURE_2D, 0)  # Desvincula a textura
        return texture # Retorna o ID da textura
```

#### Criação e compilação dos shaders

<div align='center'>
Utlizamos 2 shaders programados em Opengl Shading Language (GLSL)

**Vertex shaders** ajustam a posição e os atributos dos vértices para definir a forma dos objetos 3D. 
</div>


```glsl
#version 330 core
layout (location = 0) in vec3 position; // Posição do vértice
layout (location = 1) in vec2 texCoord; // Coordenadas de textura
layout (location = 2) in vec3 normal; // Normal

out vec2 TexCoord; // Envia as coordenadas de textura para o fragment shader
out vec3 Normal; // Envia o vetor da normal para o fragment shader
out vec3 ViewDir; // Envia o vetor 
out vec3 LightDir; // Envia o vetor de direção da luz

uniform mat4 projection; // Matriz de projeção
uniform mat4 view; // Matriz de visualização
uniform mat4 model; // Matriz de modelo
uniform vec3 lightPos; // Vetor de posição da luz
uniform vec3 viewPos; // Posição da câmera

void main() {
    gl_Position = projection * view * model * vec4(position, 1.0); // Aplica as matrizes
    TexCoord = texCoord; // Passa as coordenadas de textura para o fragment shader
    vec3 FragPos = vec3(model * vec4(position, 1.0));
    Normal = mat3(transpose(inverse(model))) * normal;
    LightDir = normalize(lightPos - FragPos);
    ViewDir = normalize(viewPos - FragPos);
}

```
<div align='center'>

 **Fragment shaders** calculam a cor e os detalhes de cada pixel, permitindo efeitos como texturização e iluminação.
</div>

```glsl
#version 330 core

in vec3 Normal; // Normal da superfície
in vec2 TexCoord;
in vec3 lightDir;
in vec3 viewDir;

out vec4 FragColor;

uniform vec3 lightColor; // Cor da luz
uniform sampler2D ourTexture;

void main()
{
    vec4 color = texture(ourTexture, TexCoord);

    // Luz ambiente
    float ambientStrength = 0.9;
    vec3 ambient = ambientStrength * lightColor;

    // Luz difusa
    vec3 norm = normalize(Normal);
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;

    // Luz especular (simplificada)
    vec3 reflectDir = reflect(-lightDir, norm);  
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32.0);
    vec3 specular = spec * lightColor;  

    vec3 result = (ambient + diffuse + specular) * color.rgb;
    FragColor = vec4(result, 1.0);

}
```
<div align='center'>
Utilizamos 2 funções dentro da nossa classe para criar e compilar os shaders.
</div>

```Python
    def compile_shader(self, source, shader_type):
        """ Compila um shader a partir do código fonte. """
        shader = glCreateShader(shader_type)
        glShaderSource(shader, source)
        glCompileShader(shader)

        # Check for compilation errors
        if glGetShaderiv(shader, GL_COMPILE_STATUS) != GL_TRUE:
            raise Exception(f"Shader compilation failed: {glGetShaderInfoLog(shader).decode()}")

        return shader
```

```Python
    def create_shader_program(self, vertex_file_path, fragment_file_path):
        """Compila e vincula um programa de shader a partir de arquivos de shader"""
        vertex_shader = self.compile_shader(open(vertex_file_path).read(), GL_VERTEX_SHADER)
        fragment_shader = self.compile_shader(open(fragment_file_path).read(), GL_FRAGMENT_SHADER)
        shader_program = glCreateProgram()
        glAttachShader(shader_program, vertex_shader)
        glAttachShader(shader_program, fragment_shader)
        glLinkProgram(shader_program)

        # Check for program linking errors
        if glGetProgramiv(shader_program, GL_LINK_STATUS) != GL_TRUE:
            raise Exception(f"Shader program linking failed: {glGetProgramInfoLog(shader_program).decode()}")

        # Delete individual shaders (no longer needed after linking)
        glDeleteShader(vertex_shader)
        glDeleteShader(fragment_shader)

        return shader_program
```

#### Translação, Rotação e Escala

<div align='center'>
As seguintes funções utilizão funções disponiveis pela glm para calcular a movimentação e escala do cubo.
</div>

**Translação**
```Python
    def transladar(self, model, direcao_x, direcao_y, direcao_z):
        #print(model, direcao_x, direcao_y, direcao_z, "\n")
        """
            model = [1][0][0][0]    # Modelo inicial
                    [0][1][0][0]
                    [0][0][1][0]
                    [0][0][0][1]
            
            model[3] = [0]          # Translação
                       [0]
                       [0]
                       [1]
        """
        model[3][0] += direcao_x
        model[3][1] += direcao_y
        model[3][2] += direcao_z
        """           
            model=  |1 0 0 0 + direcao_x|
                    |0 1 0 0 + direcao_y|
                    |0 0 1 0 + direcao_z|
                    |0 0 0 1|
        """
        return model
        """
        return glm.translate(model, glm.vec3(direcao_x, direcao_y, direcao_z))
         glm.translate
            Assumindo que o modelo esta como indetidade
            model=  |1 0 0 direcao_x|       |1 0 0 0|
                    |0 1 0 direcao_y|   *   |0 1 0 0|
                    |0 0 1 direcao_z|       |0 0 1 0|
                    |0 0 0 1|               |0 0 0 1|

        """v
```
**Rotaçao**
```Python
    def rotacionar(self, model, angle_x, angle_y, angle_z):
        # Transforma os ângulos de graus para radianos
        angle_x = glm.radians(angle_x)
        angle_y = glm.radians(angle_y)
        angle_z = glm.radians(angle_z)

        # Criação das matrizes de rotação para cada eixo
        rot_x = glm.mat4(1.0)
        rot_y = glm.mat4(1.0)
        rot_z = glm.mat4(1.0)
        """rot_x/y/z =  
            [1][0][0][0]    # Rotação inicial
            [0][1][0][0]
            [0][0][1][0]
            [0][0][0][1]
        """
        
        # Rotação em X
        rot_x[1][1] = glm.cos(angle_x)
        rot_x[1][2] = -glm.sin(angle_x)
        rot_x[2][1] = glm.sin(angle_x)
        rot_x[2][2] = glm.cos(angle_x)
        """rot_x = 
                [1] [0]      [0]       [0]
                [0] [cos(x)] [-sin(x)] [0]
                [0] [sin(x)] [cos(x)]  [0]
                [0] [0]      [0]       [1]
        """
        
        # Rotação em Y
        rot_y[0][0] = glm.cos(angle_y)
        rot_y[0][2] = glm.sin(angle_y)
        rot_y[2][0] = -glm.sin(angle_y)
        rot_y[2][2] = glm.cos(angle_y)
        """rot_y = 
                [cos(y)]  [0] [sin(y)] [0]
                [0]       [1] [0]      [0]
                [-sin(y)] [0] [cos(y)] [0]
                [0]       [0] [0]      [1]
        """
        
        # Rotação em Z
        rot_z[0][0] = glm.cos(angle_z)
        rot_z[0][1] = -glm.sin(angle_z)
        rot_z[1][0] = glm.sin(angle_z)
        rot_z[1][1] = glm.cos(angle_z)
        """rot_z = 
                [cos(z)] [-sin(z)] [0] [0]
                [sin(z)] [cos(z)]  [0] [0]
                [0]      [0]       [1] [0]
                [0]      [0]       [0] [1]
        """
        
        # Multiplicação das matrizes na ordem desejada (Z * Y * X * model)
        model = rot_z * rot_y * rot_x * model 

        return model
        """glm.rotate
        model = glm.rotate(model, glm.radians(angle_x), glm.vec3(1.0, 0.0, 0.0))
        model = glm.rotate(model, glm.radians(angle_y), glm.vec3(0.0, 1.0, 0.0))
        model = glm.rotate(model, glm.radians(angle_z), glm.vec3(0.0, 0.0, 1.0))
            Rx = | 1  0       0       0 |
                 | 0  cos(x) -sin(x)  0 |
                 | 0  sin(x)  cos(x)  0 |
                 | 0  0       0       1 |

            Ry = | cos(y)  0  sin(y)  0 |
                 | 0       1  0       0 |
                 | -sin(y) 0  cos(y)  0 |
                 | 0       0  0       1 |
            
            Rz = | cos(z) -sin(z)  0  0 |
                 | sin(z)  cos(z)  0  0 |
                 | 0       0       1  0 |
                 | 0       0       0  1 |
        """
```
**Escala**
```Python
    def escalonar(self, model, escala):
        model[0][0] *= escala
        model[1][1] *= escala
        model[2][2] *= escala
        """
        model = [x*escala] [0]        [0][0]    # Modelo inicial
                [0]        [y*escala] [0][0]
                [0]        [0][z*escala][0]
                [0]        [0][0][1]
        """
        return model
        """glm.scale
        return glm.scale(model, glm.vec3(escala, escala, escala))
            S = | escala  0       0       0 |
                | 0       escala  0       0 |
                | 0       0       escala  0 |
                | 0       0       0       1 |
        """
```


#### Projeções

<div align='center'>

**Perspectiva**, utilizamos a função glm.perspective() para criar uma matriz de projeção em perspectiva para que simule profundidade em 3D.
</div>

```Python
    def perspectiva(self):
        projection = glm.mat4(1.0)
        """
            projection = [1][0][0][0]    # Projeção inicial
                         [0][1][0][0]
                         [0][0][1][0]
                         [0][0][0][1]
        """
        projection[0][0] = 1/( math.tan( math.radians(90/2) ) ) / (SCREEN_WIDTH/SCREEN_HEIGHT)
        projection[1][1] = 1/( math.tan( math.radians(90/2) ) )
        projection[2][2] = -(100.0 + 0.1) / (100.0 - 0.1)
        projection[2][3] = -1
        projection[3][2] = -(2 * 100.0 * 0.1) / (100.0 - 0.1)
        projection[3][3] = 0
        """
            projection = # Projeção de perspectiva
            [cot(fov/2) / aspect]   [0]             [0]                     [0]    
            [0]                     [cot(fov/2)]    [0]                     [0]
            [0]                     [0]             [-(f + n) / (f - n)]    [-(2 * f * n) / (f - n)]
            [0]                     [0]             [-1]                    [0]
        """
        #print(projection)
        glUniformMatrix4fv(self.projection_loc, 1, GL_FALSE, glm.value_ptr(projection))
        # Vincula o resultado da matriz de projeção a uma uniforme no shader
        """glm.perspective
        projection = glm.perspective(glm.radians(90.0), SCREEN_WIDTH / SCREEN_HEIGHT, 0.1, 100.0)
        
        fov = Campo de visão
        aspect = proporção de aspecto da tela
        n = Distancia do plano mais proximo
        f = Distancia do plano mais distante

        Primeira Coluna: Relacionada à escala horizontal e à proporção de aspecto.

            cot(fov/2) / aspect: Escala as coordenadas X para corresponder ao campo de visão e à proporção de aspecto.

        Segunda Coluna: Relacionada à escala vertical.

            cot(fov/2): Escala as coordenadas Y para corresponder ao campo de visão.

        Terceira Coluna: Responsável pela transformação de perspectiva e mapeamento de profundidade.

            -(f + n) / (f - n): Mapeia a coordenada Z para o intervalo [-1, 1], essencial para a renderização.
            -(2 * f * n) / (f - n): Aplica a transformação de perspectiva, fazendo com que objetos mais distantes tenham valores Z menores.

        Quarta Coluna: Usada para a divisão de perspectiva.

            -1: Garante que a coordenada W seja igual a -Z após a multiplicação da matriz. A divisão por W durante a renderização cria o efeito de perspectiva.

        |cot(fov/2) / aspect   0          0                      0|
        |0                     cot(fov/2) 0                      0|
        |0                     0         -(f + n) / (f - n)    -(2 * f * n) / (f - n)|
        |0                     0         -1                      0|

        """
```

<div align='center'>

**Ortogonal**, utilizamos a função glm.ortho() para criar uma matriz de projeção em perspectiva para que simule profundidade em 3D. Esta função da biblioteca GLM cria uma matriz de projeção ortogonal (ou ortográfica). Diferente da projeção em perspectiva, a projeção ortogonal mantém o tamanho dos objetos independentemente da distância da câmera.
</div>

```Python
    def ortogonal(self):
        projection = glm.mat4(1.0)
        """
            projection = [1][0][0][0]    # Projeção inicial
                         [0][1][0][0]
                         [0][0][1][0]
                         [0][0][0][1]
        """
        projection[0][0] = 2 / (10-(-10))
        projection[1][1] = 2 / (-10-10)
        projection[2][2] = -2 / (100.0 - 0.1)
        projection[3][0] = -((-10 + 10) / (10-(-10)))
        projection[3][1] = -((-10 + 10) / (-10 - 10))
        projection[3][2] = -(100.0 + 0.1) / (100.0 - 0.1)
        """
            projection = # Projeção ortogonal
            [2/(right-left)]    [0]                 [0]             [-(right+left)/(right-left)]    
            [0]                 [2/(top-bottom)]    [0]             [-(top+bottom)/(top-bottom)]
            [0]                 [0]                 [-2/(far-near)] [-(far+near)/(far-near)]
            [0]                 [0]                 [0]             [1]
            
            [0.1]   [0]     [0]             [0]
            [0]     [-0.1]  [0]             [0]
            [0]     [0]     [-0,02002...]   [0]
            [0]     [0]     [0]             [-1,002002...]
        """
        
        # Vincula o resultado da matriz de projeção a uma uniforme no shader
        glUniformMatrix4fv(self.projection_loc, 1, GL_FALSE, glm.value_ptr(projection))
        """glm.ortho
        projection = glm.ortho(-10.0, 10.0, -10.0, 10.0, -10.0, 10.0)
        |2/(right-left)    0               0               -(right+left)/(right-left)|
        |0                 2/(top-bottom)  0               -(top+bottom)/(top-bottom)|
        |0                 0               -2/(far-near)   -(far+near)/(far-near)    |
        |0                 0               0               1                         |
        """
```


#### Iluminação e Tonalização
<div align='center'>
O modelo de iluminação Phong e tonalização Gouraud possuem os mesmos calculos utilizando as normais, posição da camera e posição da luz para obter a cor de saida do pixel. A diferença entre elas é de o modelo de Phong realiza esses calculos para cada fragmento, ou seja, dentro do fragment_shader, o que resulta uma melhor performance. Enquanto o modelo de Gouraud realiza os calculos apenas uma vez por vertice, ou seja, dentro do vertex_shader.

</div>

```glsl
#version 330 core
layout (location = 0) in vec3 position; // Posição do vértice
layout (location = 1) in vec2 texCoord; // Coordenadas de textura
layout (location = 2) in vec3 normal; // Normal

out vec2 TexCoord; // Envia as coordenadas de textura para o fragment shader
out vec3 Normal; // Envia o vetor da normal para o fragment shader
out vec3 ViewDir; // Envia o vetor 
out vec3 LightDir; // Envia o vetor de direção da luz

uniform mat4 projection; // Matriz de projeção
uniform mat4 view; // Matriz de visualização
uniform mat4 model; // Matriz de modelo
uniform vec3 lightPos; // Vetor de posição da luz
uniform vec3 viewPos; // Posição da câmera

void main() {
    gl_Position = projection * view * model * vec4(position, 1.0); // Aplica as matrizes
    TexCoord = texCoord; // Passa as coordenadas de textura para o fragment shader
    vec3 FragPos = vec3(model * vec4(position, 1.0));
    Normal = mat3(transpose(inverse(model))) * normal;
    LightDir = normalize(lightPos - FragPos);
    ViewDir = normalize(viewPos - FragPos);
}

```
```glsl
#version 330 core

in vec3 Normal; // Normal da superfície
in vec2 TexCoord;
in vec3 lightDir;
in vec3 viewDir;

out vec4 FragColor;

uniform vec3 lightColor; // Cor da luz
uniform sampler2D ourTexture;

void main()
{
    vec4 color = texture(ourTexture, TexCoord);

    // Luz ambiente
    float ambientStrength = 0.9;
    vec3 ambient = ambientStrength * lightColor;

    // Luz difusa
    vec3 norm = normalize(Normal);
    float diff = max(dot(norm, lightDir), 0.0);
    vec3 diffuse = diff * lightColor;

    // Luz especular (simplificada)
    vec3 reflectDir = reflect(-lightDir, norm);  
    float spec = pow(max(dot(viewDir, reflectDir), 0.0), 32.0);
    vec3 specular = spec * lightColor;  

    vec3 result = (ambient + diffuse + specular) * color.rgb;
    FragColor = vec4(result, 1.0);

}
```

#### Inputs do usuário

<div align='center'>

Funções para processar as entradas de movimento e interações(inputs) do usuario.

**mouse_callback** calcula a direção do movimento do mouse

</div>

```Python
    def mouse_callback(self, window, xpos, ypos):
        xoffset = xpos - self.last_x
        yoffset = self.last_y - ypos 
        self.last_x = xpos
        self.last_y = ypos

        sensitivity = 0.1 
        xoffset *= sensitivity
        yoffset *= sensitivity

        self.yaw += xoffset
        self.pitch += yoffset

        if self.pitch > 89.0:
            self.pitch = 89.0
        if self.pitch < -89.0:
            self.pitch = -89.0

        front = glm.vec3()
        front.x = glm.cos(glm.radians(self.yaw)) * glm.cos(glm.radians(self.pitch))
        front.y = glm.sin(glm.radians(self.pitch))
        front.z = glm.sin(glm.radians(self.yaw)) * glm.cos(glm.radians(self.pitch))
        self.camera_front = glm.normalize(front)
```

<div align='center'>

**process_input** Recebe e trata as entradas do teclado.
</div>

```Python
    def process_input(self, window):
        camera_speed = 2.5 * self.delta_time
        
        # Movimentação da camera
        if glfw.get_key(window, glfw.KEY_W) == glfw.PRESS:
            self.camera_pos += camera_speed * self.camera_front
        if glfw.get_key(window, glfw.KEY_S) == glfw.PRESS:
            self.camera_pos -= camera_speed * self.camera_front
        if glfw.get_key(window, glfw.KEY_A) == glfw.PRESS:
            self.camera_pos -= glm.normalize(glm.cross(self.camera_front, self.camera_up)) * camera_speed
        if glfw.get_key(window, glfw.KEY_D) == glfw.PRESS:
            self.camera_pos += glm.normalize(glm.cross(self.camera_front, self.camera_up)) * camera_speed
        if glfw.get_key(window, glfw.KEY_SPACE) == glfw.PRESS:
            self.camera_pos += camera_speed * self.camera_up
        if glfw.get_key(window, glfw.KEY_LEFT_SHIFT) == glfw.PRESS:
            self.camera_pos -= camera_speed * self.camera_up
            
        # HUD
        if glfw.get_key(window, glfw.KEY_ESCAPE) == glfw.PRESS:
            glfw.set_window_should_close(window, True)
            
        # Muda as projeções
        if glfw.get_key(window, glfw.KEY_P) == glfw.PRESS:
            self.projecao = 0
        if glfw.get_key(window, glfw.KEY_O) == glfw.PRESS:
            self.projecao = 1
            
        # Translacao
        if glfw.get_key(window, glfw.KEY_UP) == glfw.PRESS:
            self.trans_values = [0.0, 0.0, -0.1]
        if glfw.get_key(window, glfw.KEY_DOWN) == glfw.PRESS:
            self.trans_values = [0.0, 0.0, 0.1]
        if glfw.get_key(window, glfw.KEY_LEFT) == glfw.PRESS:
            self.trans_values = [-0.1, 0.0, 0.0]
        if glfw.get_key(window, glfw.KEY_RIGHT) == glfw.PRESS:  
            self.trans_values = [0.1, 0.0, 0.0]
        if glfw.get_key(window, glfw.KEY_PAGE_UP) == glfw.PRESS:
            self.trans_values = [0.0, 0.1, 0.0]
        if glfw.get_key(window, glfw.KEY_PAGE_DOWN) == glfw.PRESS:
            self.trans_values = [0.0, -0.1, 0.0]
            
        # Rotaçao
        if glfw.get_key(window, glfw.KEY_LEFT_ALT) == glfw.PRESS:
            self.rot_values = [0.0, 0.0, 0.5]
        if glfw.get_key(window, glfw.KEY_RIGHT_ALT) == glfw.PRESS:
            self.rot_values = [0.0, 0.0, -0.5]
        if glfw.get_key(window, glfw.KEY_LEFT_CONTROL) == glfw.PRESS:
            self.rot_values = [0.0, 0.5, 0.0]
        if glfw.get_key(window, glfw.KEY_RIGHT_CONTROL) == glfw.PRESS:
            self.rot_values = [0.0, -0.5, 0.0]
        if glfw.get_key(window, glfw.KEY_PERIOD) == glfw.PRESS:
            self.rot_values = [0.5, 0.0, 0.0]
        if glfw.get_key(window, glfw.KEY_COMMA) == glfw.PRESS:
            self.rot_values = [-0.5, 0.0, 0.0]
            
        # Escala
        if glfw.get_key(window, glfw.KEY_0) == glfw.PRESS:
            self.scale_value = 1.1
        if glfw.get_key(window, glfw.KEY_9) == glfw.PRESS:
            self.scale_value = 0.9

        # Phong
        if glfw.get_key(window, glfw.KEY_L) == glfw.PRESS:
            self.toggle_phong()
            
        # Gouraud
        if glfw.get_key(window, glfw.KEY_G) == glfw.PRESS:
            self.toggle_gouraud()
```


#### Execução

```Python
    def run(self):
        self.cube_vao, self.cube_vbo = self.create_cube() # cria o vao e vbo do cubo
        model = glm.mat4(1.0)   
        """Matriz modelo identidade
            |1 0 0|
            |0 1 0|
            |0 0 1|
        """
        
        while not glfw.window_should_close(self.window):
            # atualização da tela
            current_frame = glfw.get_time()
            self.delta_time = current_frame - self.last_frame
            self.last_frame = current_frame

            self.process_input(self.window) # Processa os inputs

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) # limpa o buffer de cor e profundidade

            glUseProgram(self.shader) # Vincula o programa de shader
            
            # Define a projeção
            if self.projecao == 0:
                self.perspectiva()
            else:
                self.ortogonal()
            
            if self.trans_values != [0.0, 0.0, 0.0]: # Verifica se tem input
                model = self.transladar(model, self.trans_values[0], self.trans_values[1], self.trans_values[2]) # Aplica translação com os valores do input
                self.trans_values = [0.0, 0.0, 0.0] # Limpa o input
            
            if self.rot_values != [0.0, 0.0, 0.0]: # Verifica se tem input
                model = self.rotacionar(model, self.rot_values[0], self.rot_values[1], self.rot_values[2]) # Aplica rotação com os valores do input
                self.rot_values = [0.0, 0.0, 0.0] # Limpa o input
                
            if self.scale_value != 0.0: # Verifica se tem input
                model = self.escalonar(model, self.scale_value) # Aplica escala com os valores do input
                self.scale_value = 0.0
            
            glUniform1i(self.usePhongLoc, self.usePhong) # Diz ao shader se deve usar Phong
            
            view = glm.lookAt(self.camera_pos, self.camera_pos + self.camera_front, self.camera_up)
            """glm.lookAt:
            c = camera position
            t = target position
            u = camera up vector
            f = normalize(t - c) 
            r = normalize(cross(f, u)) 
            up = cross(r, f) 

            | rx  ry  rz -dot(r, c) |
            | ux  uy  uz -dot(up, c) |
            | -fx -fy -fz  dot(f, c) |
            |  0   0   0      1      |
            """
            
            glUniformMatrix4fv(self.view_loc, 1, GL_FALSE, glm.value_ptr(view)) #glm.value_ptr: usa ponteiro
            glUniformMatrix4fv(self.model_loc, 1, GL_FALSE, glm.value_ptr(model))
            """glUniformMatrix4fv:
                Manda uma matrix 4x4 de floats pra uma variável uniforme do shader
                Vertex Shader recebe matrix 4x4 de floats do modelo e da view
            """
            
            
            glActiveTexture(GL_TEXTURE0) # Ativa o espaço da memoria GL_TEXTURE0
            glBindTexture(GL_TEXTURE_2D, self.texture) # Vincular textura
            glUniform1i(glGetUniformLocation(self.shader, "ourTexture"), 0) # Passa para o vertex shader o sampler2d

            glBindVertexArray(self.cube_vao) # Seleciona o vao do cubo
            glDrawArrays(GL_TRIANGLES, 0, 36)  # Desenha o cubo usando triangulos como forma primitiva | 0: index inicial, (36: numero de vertices)/3 = 12 triangulos.
            glBindVertexArray(0) # Deseleciona o vao do cubo

            glfw.swap_buffers(self.window)
            glfw.poll_events()

        glfw.terminate()
```

### Resultados

O resultado final do projeto é um programa que renderiza uma escada 3D com iluminação e tonalização, e que permite ao usuário interagir com ela, movendo-a e escalonando-a.

<div align="center">
    <img src="https://github.com/NavajasThomaz/OpenGL_C3/blob/main/avaliacao_CG/Resultado.gif?raw=true"/>
</div>


<div align="center">

### Rasterização (Bresenham)

Neste projeto usamos o algoritmo de Bresenham para rasterizar linhas de forma eficiente e precisa, essa é uma tecnica amplamente utilizada para desenhar linhas entre dois pontos em uma grade de pixels.
</div>

```python
import numpy as np
from OpenGL.GL import *
```
```Python
# Função que implementa o algoritmo de Bresenham para rasterizar uma linha
def bresenham_line(x0, y0, x1, y1):
    """Implementa o algoritmo de Bresenham para rasterizar uma linha"""
    points = []  # Lista que armazenará os pontos da linha
    dx = abs(x1 - x0)  # Diferença absoluta nas coordenadas x
    dy = abs(y1 - y0)  # Diferença absoluta nas coordenadas y
    sx = 1 if x0 < x1 else -1  # Sinal do incremento x
    sy = 1 if y0 < y1 else -1  # Sinal do incremento y
    err = dx - dy  # Erro inicial

    while True:
        points.append((x0, y0))  # Adiciona o ponto atual à lista de pontos
        if x0 == x1 and y0 == y1:  # Verifica se o ponto final foi alcançado
            break
        e2 = 2 * err  # Calcula o dobro do erro
        if e2 > -dy:  # Ajusta o erro e incrementa x
            err -= dy
            x0 += sx
        if e2 < dx:  # Ajusta o erro e incrementa y
            err += dx
            y0 += sy

    return points  # Retorna a lista de pontos da linha
```
```Python
# Função que configura o VAO e VBO para a linha
def setup_line(line_points):
    """Configura o VAO e VBO para a linha"""
    line_vertices = []  # Lista que armazenará os vértices da linha
    for x, y in line_points:
        # Convertendo coordenadas de pixels para coordenadas normalizadas OpenGL
        x_normalized = (x / 640) * 2 - 1  # Normaliza a coordenada x
        y_normalized = (y / 480) * 2 - 1  # Normaliza a coordenada y
        line_vertices.append(x_normalized)  # Adiciona a coordenada x normalizada à lista de vértices
        line_vertices.append(y_normalized)  # Adiciona a coordenada y normalizada à lista de vértices
        line_vertices.append(0.0)  # Adiciona a coordenada z (0.0) à lista de vértices (2D)

    line_vertices = np.array(line_vertices, dtype=np.float32)  # Converte a lista de vértices para um array NumPy

    vao = glGenVertexArrays(1)  # Gera um VAO 
    vbo = glGenBuffers(1)  # Gera um VBO 

    glBindVertexArray(vao)  # Liga o VAO
    glBindBuffer(GL_ARRAY_BUFFER, vbo)  # Liga o VBO
    glBufferData(GL_ARRAY_BUFFER, line_vertices.nbytes, line_vertices, GL_STATIC_DRAW)  # Envia os dados dos vértices para o buffer

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * 4, ctypes.c_void_p(0))  # Define o formato dos dados dos vértices
    glEnableVertexAttribArray(0)  # Habilita o atributo de vértice no índice 0

    glBindBuffer(GL_ARRAY_BUFFER, 0)  # Desliga o VBO
    glBindVertexArray(0)  # Desliga o VAO

    return vao, vbo  # Retorna o VAO e o VBO configurados
```
### Função de rasterização Bresenham
Inicialização:
- definimos os pontos iniciais (x0, y0) e final(x1,y1) da linha,
```Python
def bresenham_line(x0, y0, x1, y1):
    """Implementa o algoritmo de Bresenham para rasterizar uma linha"""
    points = []  # Lista que armazenará os pontos da linha
``` 
- calculamos a diferença absoluta nas coordenadas x(dx) e y(dy),
```Python
    dx = abs(x1 - x0)  # Diferença absoluta nas coordenadas x
    dy = abs(y1 - y0)  # Diferença absoluta nas coordenadas y
``` 
- Determinamos a direção da linha com os dinais incrementados x(sx) e y(sy)
```Python
    sx = 1 if x0 < x1 else -1  # Sinal do incremento x
    sy = 1 if y0 < y1 else -1  # Sinal do incremento y
```   
- inicializamos um valor de erro(err) que vai nos ajudar a decidir quando devemos incrementar as coordenadas x ou y.
```Python
err = dx - dy  # Erro inicial
```      

no looop: 
```Python
while True:
```  
- adicionamos o ponto atual a lista de pontos que compoem a linha
```Python
    points.append((x0, y0))  # Adiciona o ponto atual à lista de pontos
```  
- loop encerrado com o ponto final
```Python
    if x0 == x1 and y0 == y1:  # Verifica se o ponto final foi alcançado
        break
```  
- calcula-se e2 que é duas vezes o erro
```Python
    e2 = 2 * err  # Calcula o dobro do erro
```  
- ajustamos o erro e incrementamos x ou y dependendo do valor de e2
```Python
    if e2 > -dy:  # Ajusta o erro e incrementa x
            err -= dy
            x0 += sx
        if e2 < dx:  # Ajusta o erro e incrementa y
            err += dx
            y0 += sy
```  
### Função para configurar o VAO e VBO para a linha
```Python
# Função que configura o VAO e VBO para a linha
def setup_line(line_points):
    """Configura o VAO e VBO para a linha"""
    line_vertices = []  # Lista que armazenará os vértices da linha
    for x, y in line_points:
        # Convertendo coordenadas de pixels para coordenadas normalizadas OpenGL
        x_normalized = (x / 640) * 2 - 1  # Normaliza a coordenada x
        y_normalized = (y / 480) * 2 - 1  # Normaliza a coordenada y
        line_vertices.append(x_normalized)  # Adiciona a coordenada x normalizada à lista de vértices
        line_vertices.append(y_normalized)  # Adiciona a coordenada y normalizada à lista de vértices
        line_vertices.append(0.0)  # Adiciona a coordenada z (0.0) à lista de vértices (2D)

    line_vertices = np.array(line_vertices, dtype=np.float32)  # Converte a lista de vértices para um array NumPy

    vao = glGenVertexArrays(1)  # Gera um VAO 
    vbo = glGenBuffers(1)  # Gera um VBO 

    glBindVertexArray(vao)  # Liga o VAO
    glBindBuffer(GL_ARRAY_BUFFER, vbo)  # Liga o VBO
    glBufferData(GL_ARRAY_BUFFER, line_vertices.nbytes, line_vertices, GL_STATIC_DRAW)  # Envia os dados dos vértices para o buffer

    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 3 * 4, ctypes.c_void_p(0))  # Define o formato dos dados dos vértices
    glEnableVertexAttribArray(0)  # Habilita o atributo de vértice no índice 0

    glBindBuffer(GL_ARRAY_BUFFER, 0)  # Desliga o VBO
    glBindVertexArray(0)  # Desliga o VAO

    return vao, vbo  # Retorna o VAO e o VBO configurados
``` 
```Python
```          
<div style="display: inline_block">

</div>



<details open>
<summary>

# Instruções</summary>

Nessa seção está o passo a passo de como executar esse projeto em seu própio ambiente.
Nós rencomendamos montar seu ambiente utilizado o 
<a href="https://code.visualstudio.com/" target="_blank"><img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white" target="_blank"></a>
</details>

