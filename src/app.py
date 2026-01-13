import gradio as gr

def my_function(input1, input2):
    """내 함수에 대한 설명"""
    return process(input1, input2)

def letter_counter(word, letter):
    """단어 내 특정 글자의 등장 횟수를 세는 함수
    
    Args:
        word: 분석할 단어나 문장
        letter: 세고자 하는 글자
        
    Returns:
        해당 글자가 단어에 나타난 횟수
    """
    return word.lower().count(letter.lower())

# demo = gr.Interface(fn=my_function, inputs=["text", "text"], outputs="text")

demo = gr.Interface(
    fn=letter_counter,
    inputs=["text", "text"],
    outputs="number",
    title="글자 수 세기",
    description="단어 내 특정 글자가 몇 번 등장하는지 세기"
)


demo.launch(mcp_server=True)  # MCP 서버 활성화!