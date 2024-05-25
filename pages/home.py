import streamlit as st
from streamlit_option_menu import option_menu


st.markdown(
    """
    <style>
    .titleContainer {
        width: 350px;
        height: 525px;
        background: rgb(231,184,176);
        background: radial-gradient(circle, rgba(231,184,176,1) 0%, 
        rgba(233,204,191,1) 50%, rgba(246,246,246,1) 100%);
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
    }
    .title{
        font-weight: bold;
        font-size: 100px;
        color: #E8959F;
        margin-top: 270px;
    }
    .subTitle {
        font-size: 15px;
        color: #E8959F;
        font-weight: bold;
        width: 300px;
        text-align: start;
    }
    .serviceSummary {
        color: #cd4662;
        font-size: 14px;
        font-weight: bold;
        text-align: left;
    }
    .tagContainer {
        margin-top: 30px;
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: space-between;
    }
    .tag {
        color: #cd4662;
        font-weight: bold;
        font-size: 16px;
        border-radius: 10px;
        text-align: center;
        padding: 5px;
    }
    .centerContainer {
        margin-top: 10px;
        border-radius: 10px;
        width: 715px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        padding: 20px;
        margin-bottom: 25px;
    }
    .AboutMomEText {
        display: flex;
        flex-direction: column;
        align-items: center;
        font-size: 20px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .AboutMomEContent {
        font-size: 20px;
        text-align: center;
        font-weight: 700px;
    }
    .detailServiceContainer{
        border-radius: 10px;
        width: 350px;
        height: 300px;
        margin-bottom: 10px;  
        padding: 35px;
        background-color: #fff9f0; 
    }
    .infoContainer{
        border-radius: 10px;
        width: 350px;
        height: 300px;
        margin-bottom: 10px;  
        padding: 35px;
        background-color: #FFF9EF; 
    }
    .diaryContainer{
        border-radius: 10px;
        width: 350px;
        height: 300px;
        margin-bottom: 10px;  
        padding: 35px;
        background-color: #FFEEEE; 
    }
    .diaryTestContainer{
        border-radius: 10px;
        width: 350px;
        height: 300px;
        margin-bottom: 10px;  
        padding: 35px;
        background-color: #FFF4ED; 
    }
    .selfTestContainer{
        border-radius: 10px;
        width: 350px;
        height: 350px;
        margin-bottom: 10px;  
        padding: 35px;
        background-color: #FBF6FD; 
    }
    .serviceTitle{
        font-size: 30px;
        text-align: start;
        font-weight: bold;
        margin-bottom: 15px;
        color: #000000;
    }
    .serviceContent {
        width: 300px;
        height: 20px;
        margin-bottom: 15px;  
    }
    .contactContainer{
        margin-top: 10px;
        border-radius: 10px;
        width: 715px;
        height:100px;
    }
    </style>
        """,
        unsafe_allow_html=True
    )

row1, row2 = st.columns(2)

with row1:
    
    
    st.markdown(f"""
            <div class = "titleContainer">
                <div class="title">MomE</div>
                <div class= "subTitle">
                    For Your Own<br>For Your Healthy Nurturing.
                </div>
            </div>   
            """
            ,unsafe_allow_html=True
        )    
    
with row2: 
    st.write("image")
    #st.image("media/titleImg.jpg", width=350)
    
st.markdown(
    f'''
        <div class="centerContainer">
            <div class="AboutMomEText">
                ◾ About MomE ◾
            </div>
            <div class="AboutMomEContent">
                MomE는 산후 우울증을 겪고있는 산모와 가족을 위한 디지털 치료 서비스로 <br>
                사용자들에게 심리적 지원과 도움을 제공합니다.우리의 목표는 <br>
                산후 우울증으로 고통받는 부모들이 안정감을 찾고<br>
                가족과의 삶을 즐길 수 있도록 돕는 것입니다.
            </div>
        </div>
    
    ''',
    unsafe_allow_html=True
)

row3, row4 = st.columns(2)

with row3:
    st.write("image")
    #st.image("media/pexels-ketut-subiyanto-4473602 1.jpg")
    
    st.markdown(
    '''
        <div class="diaryContainer">
            <div class="serviceContent">
                📖 특별한 순간을 놓치지 않고 남겨보세요.
            </div>
            <div class="serviceTitle">
                일기장 서비스
            </div>
            <div class="serviceContent">
                산모가 육아 일기를 작성하며<br>
                자신의 마음도 함께 돌아볼 수 있는<br>
                서비스를 제공합니다.<br><br>
                가족과 함께 공유해보세요.
            </div>
        </div>      
    ''',
    unsafe_allow_html=True

    )
    st.write("image")
   # st.image("media/pexels-olly-3756036 1.jpg", width=350)
    
    st.markdown(
    '''
        <div class="selfTestContainer">
            <div class="serviceTitle">
                산후우울증<br>
                자가진단<br>
                테스트
            </div>
            <div class="serviceContent">
                에딘버러 산후우울증 척도 K-EPDS를 이용하여 
                산후 우울증 자가진단 및 시각화 데이터를 제공합니다.   
            </div>
        </div>      
    ''',
    unsafe_allow_html=True

    )


with row4:
    st.markdown(
    '''
        <div class="infoContainer">
            <div class="serviceContent">
                📌산후우울증에 대해 알아보아요.
            </div>
            <div class="serviceTitle">
                산후우울증<br>바로알기
            </div>
            <div class="serviceContent">
                산후 우울증(postpartum depression)에<br>
                대한 원인, 증상,치료 등 기본정보를<br>
                제공합니다.
            </div>
        </div>      
    ''',
    unsafe_allow_html=True

    )
    st.write("image")
    #st.image("media/pexels-george-milton-7034449 1.jpg")
    
    st.markdown(
    '''
        <div class="diaryTestContainer">
            <div class="serviceContent">
                🩷자신의 마음도 함께 토닥여주세요.
            </div>
            <div class="serviceTitle">
                일기장 감정 분석<br>서비스
            </div>
            <div class="serviceContent">
                산모의 감정 변화를 추적하고 긍정적인<br>피드백을
                제공하여 부모님들이<br>더 건강한 육아를 할 수 있도록 지원합니다.
            </div>
        </div>      
    ''',
    unsafe_allow_html=True

    )
    st.write("image")
    #st.image("media/pexels-valeria-ushakova-603898-3094230 1.jpg", width=350)

# 문의하기
st.subheader("Contact")
st.markdown("""
    <p class="contact">질문이나 문의 사항이 있으시면 언제든지 <a href="mailto:202100694@hufs.ac.kr">여기</a>로 이메일을 보내주세요.</p>
""", unsafe_allow_html=True)



with st.sidebar:
    menu = option_menu("MomE", ['Home','Dashboard','Diary','육아 SNS','community', '하루 자가진단', 'LogOut'],
                        icons=['bi bi-house-fill','bi bi-grid-1x2-fill','book-half','Bi bi-star-fill','Bi bi-star-fill' ,'bi bi-capsule-pill', 'box-arrow-in-right'],
                        menu_icon="baby", default_index=0,
                        styles={
                            "icon": {"font-size": "23px"},
                            "title": {"font-weight": "bold"}  # MomE 글씨를 볼드체로 변경
                        })

    # 선택된 메뉴에 따라 페이지 변경
if menu =='Diary':
    st.switch_page("pages/diary_page.py")
elif menu =='Dashboard':
    st.switch_page("pages/dashboard_page.py")
elif menu == '육아 SNS':
    st.switch_page("pages/SNS2.py")
elif menu == 'community':
    st.switch_page("pages/community.py")
elif menu =='하루 자가진단': 
    st.switch_page("pages/self_diagnosis.py")
elif menu =='LogOut':
    st.switch_page("dd1.py")
