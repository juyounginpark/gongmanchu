# 배경
image scene1yard = "scene1yard.jpg"
image scene2bridge1 = "scene2bridge1.jpg"
image night_college= "night_college.jpg"
image suljari = "suljari.jpg"
image scene3_1_haedalroom = "scene3_1_haedalroom.jpg"
image scene3_gadu = "scene3_gadu.jpg"
image haedalmt = "haedalmt.jpg"
image mg1 ="mg1.jpg"
image mg2 ="mg2.jpg"
image mg3 ="mg3.jpg"
image mg4 ="mg4.jpg"
image scene3_2_mt_fire = "scene3_2_mt_fire.jpg"
image scene3_3_bench = "scene3_3_bench.jpg"
image scene4_wakeup = "scene4_wakeup.jpg"
image scene5_library ="scene5_library.jpg"
image scene7_night_haedalroom = "scene7_night_haedalroom.png"
image scene7_bokdo = "scene7_bokdo.jpg"
image scene7_night_gigsa = "scene7_night_gigsa.jpg"
image scene2_classroom = "scene2_classroom.jpg"
image nightcall = "nightcall.png"
image nightcalling = "nightcalling.png"
image service_1 = "service_1.png"

# 캐릭터
image juyoun_standard = "juyoun_standard.png"
image juyoun_shy = "juyoun_shy.png"
image juyoun_sad = "juyoun_sad.png"
image juyoun_love = "juyoun_love.png"
image gyoungmin_stardard = "gyoungmin_standard.jpg"
image hyeonseo_standard = "hyeonseo_standard.png"
image minsu_standard = "minsu_standard.png"

# 물건
image mtjo = "mtjo.png"

# 스페셜
image parkjuyoung_stadard = "parkjuyoung.png"

# 컬러_주요
define sys = Character('sys',color="#000000")
define gyoungmin = Character('서경민', color="#c8ffc8")
define juyoun = Character('박주연', color ="#e180d1")
define hyeonseo = Character('이현서',color ="#5528de")
define minsu = Character('김민수 교수',color ="#0ecd2b")

# 컬러_스페셜
default name = "서경민"
default s_name = "경민"
define parkjuyoung = Character('박주영', color="#ffd93f")
define bridge1 = Character('한국대학교 총장', color="#3c872d")
define haedal_seo = Character('서주혜', color="#c14772")
define haedal_yang = Character('양승현', color="#163a0f")
define na = Character( "서경민" , color="#ffffff") 

default juyoun_love_num=0
default juyoun_negai=False
default juyoun_negai_check=False
default minsu_love_num=0
default coffee = False
default jbo = False
default democratic_party = 0


init:
    screen stat_overlay:
        frame:
            padding (15, 15)
            background "#4f5a6680"
            align (1.0, 0.0)
            xmaximum 250
            ymaximum 200

            vbox:
                if juyoun_love_num != 0 :
                    if juyoun_negai and juyoun_negai_check:
                        text "주연 🎫{space=15}[juyoun_arr.count(True)*25]" size 28
                    else :
                        text "주연{space=15}[juyoun_arr.count(True)*25]" size 28
                    text " " size 1
                    bar:
                        value juyoun_arr.count(True)*25
                        range 100
                        style "fixed_bar"

                text " " size 3
                if minsu_love_num != 0 :
                    text "민수{space=15}[minsu_arr.count(True)*25]" size 28
                    text " " size 1
                    bar :
                        value minsu_arr.count(True)*25
                        range 100
                        xalign 0.0
                        style "fixed_bar"


init -5 python:
    style.fixed_bar = Style(style.default)

    style.fixed_bar.xmaximum = 200
    style.fixed_bar.ymaximum = 15

    style.fixed_bar.left_gutter = 0
    style.fixed_bar.right_gutter = 0

    style.fixed_bar.left_bar = Frame("images/bar_full.png", 0, 0)
    style.fixed_bar.right_bar = Frame("images/bar_empty.png", 0, 0)

define love = [0, 0]
define juyoun_arr = [False, False, False, False]
define minsu_arr = [False, False, False, False]

            


label start:
    "본 게임물은 픽션이며, 등장하는 인물, 지명, 기관, 사건, 단체 및 배경 등은 실제와 어떠한 관련도 없음을 알려드립니다."
    
    show screen stat_overlay
    # $ love[1] += 30
    # hide screen stat_overlay

    
    
    # na "낯설지 않아 너의 오묘한 눈빛, 평행한 느낌"

    play music "audio/bgm/mainbgm.mp3"
    scene scene1yard with fade
    #S1. 입학식에서 처음 만난 그 선배
    "여기가 한국대학교..?"
    "엄청 넓다.."
    "앗, 입학식 시간이 곧이잖아?"
    
    show juyoun_standard at center
    with easeinright
    with vpunch
    juyoun "혹시 컴퓨터학부 신입생인가요?"

    "아.. "
    extend "넵!!"
    "(우와.. 예쁘다)"
   

    juyoun "저는 컴퓨터학부 학생회장 3학년 박주연이에요."
    juyoun "혹시 이름이 어떻게..."
    $ name = renpy.call_screen("set_name",title="당신의 이름은?", init_name="서경민")
    if len(name) > 2:
        $ s_name = name[1:3]
    # $ na = Character( name , color="#ffffff")
    $ gyoungmin = Character(name, color="#c8ffc8")
    gyoungmin "앗.. 안녕하세요!"
    gyoungmin "저는 새로 입학하게 된 1학년 [name]입니다!"

    juyoun "후훗, 반가워요."
    juyoun "대강당까지 안내해 줄게요."

    gyoungmin "(선배의 따듯한 손..)"

    juyoun "앞으로 선배랑 마주하게 되면 가볍게 목례하는 거,"
    extend "좋은 습관이 될 거에요."
    juyoun "저를 따라와요."
    menu:
        "선배를 따라간다.":
            gyoungmin "잘 부탁드립니다..!!"
            hide juyoun_standard
            show juyoun_love
            juyoun "(웃음)"
            hide juyoun_love
            jump scene1_1
        "선배를 따라가지 않는다.":
            gyoungmin "저 아세요? 근데..?"
            juyoun "네? 아니... 죄송해요.."
            hide juyoun_standard
            show juyoun_sad at center
            juyoun "잠깐이었지만 만나서 즐거웠어요..!! 그럼 다음에 또 봬요..!"
            hide juyoun_sad
            with dissolve
            gyoungmin "정말이지... 여자들이란... 나를 가만 못 둬서 문제라니까.."
            jump badend1

    #E1, 배드 엔딩 1
    label badend1:
        stop music fadeout 5.0
        scene black 
        "(10년 후)"
        gyoungmin "나는 대학시절 내내 화장실에서 밥을 먹었다."
        gyoungmin "만약 그때 그 선배를 따라갔다면 달라졌을까..?"
        "BAD END 1: 별볼일 없는 엔딩"
        return

    #S_1, 입학식 브릿지
    label scene1_1:
        scene scene2bridge1
        bridge1 "우리 한국대학교에 입학하게 되신 여러분 진심으로 환영합니다."
        bridge1 "우리 한국대학교는 예로부터..."
        gyoungmin "(지루하다...)"
        gyoungmin "(빨리 끝나라...)"

        scene black with fade
        gyoungmin "Zzz.........."
        "저기요?"
        "혹시..."
        scene scene2bridge1 with vpunch
        show hyeonseo_standard
        hyeonseo "컴퓨터학부 신입생인가요??"
        hyeonseo "몇 살이에요? 저는 06년생이에요!!"
        hyeonseo "잘해봐요! 신입생끼리!!"
        gyoungmin "아.."
        extend " 네.."
        gyoungmin "(좋은 친구같다..)"
        gyoungmin "(그치만 기빨려..)"
        hide hyeonseo_standard
        jump scene1_2

    #S1_2 입학식 후 브릿지
    label scene1_2: 
        scene night_college
        show juyoun_standard with fade
        juyoun "입학식 어땠어요?"
        hide juyoun_standard
        show juyoun_shy
        juyoun "정말 자랑스럽지 않나요?"
        hide juyoun_shy
        show juyoun_standard
        juyoun "저 고등학교 때 한국대학교에 정말 오고 싶었거든요."
        juyoun "앗..! 저 너무 말이 길었죠.. 끝나고 신입생 뒷풀이 하는데"
        juyoun "오라는 말을 하려 했었어요"
    menu:
        "좋아요!":
            jump bridge_soju 

    label bridge_soju:
        hide juyoun_standard
        show juyoun_love
        juyoun "(웃음)"
        juyoun "학교 정문에 있는 배 터지는 탕수육으로 와요."
        hide juyoun_love
        jump scene1_3

    #1_3. 입학식 뒷풀이, 술자리
    label scene1_3:
        scene suljari with fade
        show juyoun_standard 
        juyoun "술은 처음이에요?"
        juyoun "그럼 마시면서 배우는 술 게임~"
        juyoun "민주당 "
        extend "민주당 "
        extend "민주당 "
        extend "민주당.."
        juyoun "[s_name],"
        extend "너 숙여!"
        gyoungmin "네..? 넵..!!"
        hide juyoun_standard
        scene black with fade
        jump sulgame1

    label sulgame1:
        juyoun "자, "
        extend "이제 제가 하는 말에 대답하면 돼요."
        jump mustsul

    label mustsul:
        if democratic_party > 2:
            jump minju_bad
        juyoun "이 사람! "
        extend "술 마셔? "
        extend "안 마셔?"
    menu:
        "마셔!":
            juyoun "흐흐흐.. 진짜로요?"
            juyoun "좋아요."
            extend "이제 눈 떠봐요."
            jump scene1_4

        "안마셔!":
            $democratic_party = democratic_party + 1
            juyoun "진짜로요"
            extend "...?"
            juyoun "그러면..."
            jump mustsul          

    label minju_bad:
        scene suljari with fade
        show hyeonseo_standard at center
        hyeonseo "이 게임! " with vpunch
        extend "누가 했어!!" with vpunch
        hide hyeonseo_standard



    
    label scene1_4:
        scene suljari
        show juyoun_love
        juyoun "마시면 돼요."
        juyoun "제가 [s_name]씨를 지목했거든요."
        gyoungmin "(눈 감은 사람의 대답에 따라 술 마시는 사람이 결정되는 게임이구나..)"
        hide juyoun_love
        show juyoun_standard
        gyoungmin "진짜 "
        extend "마셔요..?"
        hide juyoun_standard
        show juyoun_standard at right
        show hyeonseo_standard with vpunch
        gyoungmin "(꿀꺽)"
        gyoungmin "으아.."
        hide hyeonseo_standard
        show hyeonseo_standard at left
        hyeonseo "술 "
        extend "마실 "
        extend "시간이 "
        extend "없어요"
        extend "!!!"
        juyoun "현서가! "
        juyoun "좋아하는! "
        extend "랜덤 게임! "
        extend "무슨 게임! "
        extend "게임.."
        hide juyoun_standard
        show juyoun_love at right
        juyoun "스타트!"
        hide juyoun_love
        show juyoun_standard at right
        hyeonseo "저희... "
        hyeonseo "어!" with hpunch
        hyeonseo "신난다. "
        extend "재미난다."
        hyeonseo "더! "
        extend "게임 "
        extend "오브 "
        extend "데! "
        extend "스!" 
        hyeonseo "[s_name]아, "
        extend "너가 원하는 사람을 지목하면 돼."
        gyoungmin "으.. "
        extend "응..!!"
        juyoun "게임이니깐.. "
        extend "편히 골라요."
        jump scene1_4pick

    label scene1_4pick:
        menu:
            "이현서":
                hyeonseo "ㅠㅠ"
                hyeonseo "진짜로?"
                jump scene4_must
            "박주연":
                juyoun "[s_name]씨.."
                juyoun "진짜로요"
                extend "...?"
                jump scene4_must
            "박주영":
                show parkjuyoung_stadard
                parkjuyoung "어이.."
                extend "갑자기 나를 왜 부른건가.."
                parkjuyoung "뭐..? 나보고 술을 마시라고 한건가??!!"
                parkjuyoung "할 수 없군..."
                parkjuyoung "<개발자의 "
                extend "권한>" with vpunch
                "당신은 <개발자의 권한>으로 인해 AURA가 9999999만큼 감소했습니다.."
                "그리고"
                "당신의 머리카락이 "
                extend "하나 빠졌습니다."
                hide parkjuyoung_stadard
                jump scene4_must

    label scene4_must:
        menu:
            "가리킨다.":
                gyoungmin "네 !!"
                gyoungmin "이 사람으로 할게요."
                jump scene4_2
            "다른 사람을 고른다.":
                gyoungmin "아니요.."
                extend "사실은 .."
                jump scene1_4pick

    label scene4_2:
        hyeonseo "4!"
        hyeonseo "하나"
        juyoun "둘"
        parkjuyoung "셋"
        parkjuyoung "[s_name]씨. "
        extend "마시세요 !"
        hyeonseo "흐흐흐.."
        gyoungmin "(현서 자식.. 일부러 날 먹이려고 ...)"
        gyoungmin "넵..!!!"
        hide juyoun_standard
        hide hyeonseo_standard
        show juyoun_standard at center
        juyoun "잠깐!" with vpunch
        juyoun "술은 자신의 주량만큼 먹는게 좋아요."
        juyoun "[s_name]씨 많이 취하신 거 같은데.."
        juyoun "제가 흑장미 .."
        hide juyoun_standard
        show juyoun_love
        juyoun "할게요!!"
        gyoungmin "네..?"
        hide juyoun_love
        menu:
            "그럼.. 부탁해요 선배 !":
                gyoungmin "(얼굴만 이쁘신게 아니였구나 ..)"
                show juyoun_shy
                juyoun "(꿀꺽)"
                juyoun "대신, "
                extend "뭐든지 가능한 소원권 주기에요?"
                gyoungmin "ㄴ.."
                extend " 네!"
                $juyoun_negai = True
                $juyoun_negai_check = True
                "선배가 '소원권'을 획득했다."
                $juyoun_negai_check = False
            "제가 걸린거니까 제가 마실게요..!":
                gyoungmin "제가 걸린거니까 제가 마실게요..!"
                show juyoun_standard
                juyoun "너무 무리하지마요."
                gyoungmin "네.."
                gyoungmin "(힘들다..)"
        hide juyoun_love
        show juyoun_shy
        juyoun "자.."
        extend "다음 게임으로 넘어갈까요?"
        hyeonseo "주연이가 좋아하는 ..."
        scene black with fade
        gyoungmin "아... "
        gyoungmin "내 몸이 왜 이러지.."
        scene suljari with fade
        scene black with fade
        scene suljari with fade
        scene black with fade
        "야!!" with vpunch
        "[name]!!" with vpunch
        extend " 일어나봐 !"
        "선배, 얘 술 많이 취한거 같은데요?"
        "그러게요.. 어떡하지"
        "일단 옮길까요?"
        "네 그래요.."
        "에구.. 그러게 적당히 마시지..."
        gyoungmin "그날.. 술을 너무 무리해서 마셨던 나는"
        gyoungmin "눈떠보니 기숙사 앞에 누워 있었다."
        gyoungmin "너무 부끄러운 나머지.."
        gyoungmin "개강 전까지 집에만 박혀 후회하고 "
        extend "또 후회했다."
        jump scene2

    #scene2. 첫 수업
    label scene2:
        scene scene2_classroom with fade
        gyoungmin "으아... 첫 수업이라니"
        gyoungmin "긴장되서 울렁거려.."
        gyoungmin "아, 교수님 오신다."
        hide gyoungmin_standard
        show minsu_standard
        minsu "Good morning. 컴퓨터학개론 강의를 맡은 ‘김민수’입니다."
        minsu "결석은 세 번만 넘겨도 F니 모두 조심하도록."
        gyoungmin "교수님.. 생각보다 되게 젊으시잖아?"
        gyoungmin "결석 안하도록 조심해야겠다..."
        hide minsu_standard
        show black with fade
        "그러나, 이런 결심이 무색하게"
        "나는 며칠 뒤 몸살로 결석을 하고 말았다.."
        scene scene4_wakeup with fade
        gyoungmin "몸살때문에 수업도 가지 못했다..."
        gyoungmin "어떻게 해야하지?"
        menu:
            "교수님께 연락드린다.":
                gyoungmin "교수님께 이유라도 말씀드려야지."
                gyoungmin "교수님 이메일이... "
                extend "여기 있다."
                gyoungmin "어떻게 적어야 하지..? 우선.."
                jump scene2_email
            "교수님께 연락드리지 않는다.":
                gyoungmin "어차피 모르시겠지..."
                gyoungmin "그냥 다음 수업부터 열심히 해보자."
                jump scene3
            

    label scene2_email:
        scene scene4_wakeup with fade
        menu:
            "신분을 밝힌다.":
                gyoungmin "..."
                extend "... "
                extend "다 적었다."
                gyoungmin "너무 길게 적은거 같은데.."
                gyoungmin "뺄 내용은 없을까?"
                menu:
                    "수강중인 분반":
                        gyoungmin "근데 교수님 같은 강의를 5개 하신다고 들었는데.."
                        gyoungmin "헷갈리시면 어떡하지?"
                        gyoungmin "다시 적어보자."
                        jump scene2_email
                    "결석 사유":
                        gyoungmin "근데 교수님 같은 강의를 5개 하신다고 들었는데.."
                        gyoungmin "헷갈리시면 어떡하지?"
                        gyoungmin "다시 적어보자."
                        jump scene2_email
                    "수업 평가":
                        gyoungmin "수업 평가..?"
                        gyoungmin "왠지 좋아하지 않으실 것 같아.."
                        gyoungmin "지우고 보내는게 좋을 것 같아."
                        gyoungmin "... "
                        extend "보냈다."
                        jump scene2_reply
                    "감사 인사":
                        gyoungmin "그래도 감사 인사는 드려야지."
                        gyoungmin "빼고 보내드리면 왠지 좋아하지 않으실 것 같아"
                        jump scene2_email
            "본론부터 적는다.":
                gyoungmin "근데 이러면 교수님이 내가 누군지 아실까..?"
                gyoungmin "다시 적어보자."
                jump scene2_email
    
    
    label scene2_reply:
        gyoungmin "앗.." with vpunch
        gyoungmin "바로 답장이?"
        minsu "[name] 학생, 확인했습니다."
        minsu "몸조리 잘하고 다음 수업에서 뵙도록 하지요."
        minsu "그나저나.. "
        extend "이메일 매너가 출중하더군요."
        minsu "별건 아니지만 "
        extend "커피 한 잔 하도록 해요."
        gyoungmin "헙.. 커피 기프티콘까지.."
        gyoungmin "감사합니다, 교수님 !!"
        "'교수님이 사준 커피'를 획득했다."
        $minsu_love_num = minsu_love_num + 1
        $ minsu_arr[0] = False
        $ minsu_arr[0] = True
        $coffee = True
                


    #scene3. 동아리 박람회
    label scene3:
        scene scene3_gadu with fade
        "(웅성웅성)"
        gyoungmin "뭐지?"
        show hyeonseo_standard
        hyeonseo "동아리 가두모집 기간 아니야?"
        gyoungmin "아 동아리 가두모집 기간이구나."
        gyoungmin "(어떤 동아리가 나를 기다리려나 ...)"
        gyoungmin "어.. "
        extend "저 사람은?"
        hide hyeonseo_standard
        show hyeonseo_happy
        hyeonseo "맞지? "
        extend "주연 선배."
        hyeonseo "그때 나랑 둘이서 너 챙기느라 엄청 고생했었어."
        gyoungmin "헐 그래? "
        extend "으아.. 어떡하지"
        
        hide hyeonseo_happy
        show juyoun_standard at center
        with fade

        juyoun "'부트캠프'로 코딩 알려주는 해달! 코딩 왕초보도 환영 ~"
        gyoungmin "선배가 동아리 홍보도 하시는건가 ..."
        gyoungmin "근데 어떡하지... 그날 너무 민폐를 끼쳐서"
        gyoungmin "말 걸기 부끄러워..."
        hyeonseo "뭐 어때?"
        hyeonseo "한번 말 걸어봐 !"
        menu:
            "아는 척한다":
                gyoungmin "주연 선배 !!"
                gyoungmin "안녕하세요..? "
                extend "흐흐..."
                $ juyoun_love_num = juyoun_love_num + 1
                $ juyoun_arr[0] = False
                $ juyoun_arr[0] = True
            "그냥 지나간다.":
                gyoungmin "(빨리 지나가야겠다.)"
        juyoun "어! [s_name]씨!"
        juyoun "그땐 잘 들어갔어요?"
        gyoungmin "아... "
        extend "네!!"
        gyoungmin "그때 챙겨주셔서 감사했습니다..."
        juyoun "후후 "
        hide juyoun_standard
        show juyoun_love
        extend "원래 신입생 때는 다 그래요."
        juyoun "[s_name]씨가 잘 들어갔다면 다행이네요."
        hide juyoun_love
        show juyoun_standard
        juyoun "그래서 그런데... "
        extend "저희 동아리 \'해달\'에 가입할 생각 없어요?"
        juyoun "다양한 소모임과 "
        extend "해커톤 등 이벤트가 많아요!"
        juyoun "코딩을 잘 모르더라도 C언어, 웹, 파이썬 부트캠프를 열어서.."
        juyoun "열정!" with vpunch
        extend "만 있다면 누구든 할 수 있답니다~"
        gyoungmin "헉.. 어떡하지.."
        menu:
            "가입한다":
                juyoun "후훗, 동아리 예절도 많이 알려줄게요."
                hyeonseo "그럼 저도 가입할래요!"
                "그렇게 나는 내 친구 현서와 함께 동아리에 가입하게 되었다."
                jump scene3_1

            "가입하지 않는다":
                jump badend2
    label badend2:
        gyoungmin "저는... "
        extend "선배한테 배울 정도는 아닌 거 같아서요."
        hide juyoun_standard
        show juyoun_sad at center
        juyoun "아.. "
        extend "죄송해요..."
        juyoun "그럼 이만..."
        scene black with fade
        "그렇게 선배는 수많은 인파를 제치고"
        "재빠르게 사라져버렸다."
        "나는 선배를 울린 예의없는 후배로 낙인이 찍혔고,"
        "그 후로 어떤 선배와도 친해질 수 없었다."
        "BAD END 2: 나쁜 남자"
        return

    #scene3_1. 동방 예절 수업
    label scene3_1:
        hide juyoun_standard
        scene scene3_1_haedalroom with fade
        
        "(동아리실에 들어가며) "
        hyeonseo "아..안녕하세요!"

        show juyoun_standard at center

        juyoun "안녕~ "
        extend "둘다 동아리실은 처음이지?"
        hyeonseo "넵!!"
        juyoun "반가워, 후훗. "
        extend "그렇게 긴장할 필요 없어요~"
        juyoun "우선 오늘은 처음이니까 동아리 예절부터 알려줄게요."
        juyoun "동아리 예절 첫째, "
        extend "동아리실에 들어오게 되면 누구든지 인사부터 하기. "
        juyoun "둘째, "
        extend "사용 후 깨끗하게 정리하기!"

        show hyeonseo_standard at left 
        with easeinleft
        
        hyeonseo "셋째, 동아리실에서 몰래 게임하다 걸리면 벌금 천원 ~"
        juyoun "ㅎㅎㅎ"
        hide juyoun_standard
        show juyoun_love
        juyoun "좋은 생각인데요?"
        hide juyoun_love
        show juyoun_standard
        gyoungmin "네, 명심할게요 !"
        juyoun "규칙을 잘 지키면 더욱 재밌게 동아리 활동을 할 수 있답니다~"
        juyoun "앗, 혹시 둘다 동아리 MT 신청했나요?"

        menu:
            "네!":
                hide juyoun_standard
                show juyoun_love
                juyoun "좋아요! "
                extend "준비물 꼼꼼히 챙겨서 MT날에 봬요."
                hide hyeonseo_standard
                hide juyoun_love
                $juyoun_love_num = juyoun_love_num + 1
                $ juyoun_arr[1] = False
                $ juyoun_arr[1] = True
                jump scene3_2

            "아니요..":
                juyoun "알겠어요.."
                juyoun "MT 끝나고 봐요?"
                jump scene4
        
        
    #scene3_2. MT&밤 모닥불
    label scene3_2:
        scene haedalmt with fade
        haedal_seo "해달 MT에 오신 것을 환영합니다!"
        haedal_seo "이렇게 많은 회원분들이 오셔서 기쁘네요."
        haedal_yang "좋습니다!"
        haedal_yang "저희가 게임을 하나 준비했는데요," 
        haedal_yang "상품은 무려 "
        haedal_seo "뭘까요?"
        haedal_yang "양주" with hpunch
        extend ", 양주를 드립니다!"
        "(사람들의 환호)" with vpunch
        gyoungmin "(기대된다.)"
        haedal_seo "조끼리 앉아 주시면 규칙 설명해드릴게요."
        menu:
            "조 확인하기":
                gyoungmin "(어디보자...)"
         
        show mtjo
        gyoungmin "(아 ..."
        extend " 주연선배는 다른 조네..)"
        haedal_seo "다들 조 확인 하셨나요?"
        haedal_yang "저희가 준비한 게임은 바로바로"
        haedal_yang "영" with vpunch
        extend "화 " with vpunch
        extend "맞추기" with vpunch
        extend "!!!"
        "(환호)" with hpunch

        gyoungmin "(영화? 내가 또 잘 알지)"
        haedal_yang "그럼.. 랜덤으로..."
        haedal_seo "아! "
        extend "2조가 걸렸네요. 2조부터 시작하겠습니다!"
        gyoungmin "(우리 조다 !)"
        gyoungmin "(꼭 잘해서 주연 선배한테 좋은 모습 보여야 겠어!!)"
        scene mg1
        haedal_yang "다음 영화 장면을 보고 영화 제목을 맞춰주시면 됩니다."
        haedal_yang "그럼 시작합니다."
        scene mg2
        default mg2 = False
        gyoungmin "무언가 강해보이는 영화네.."
        menu:
            "아이언맨":
                $mg2 = False
            "타짜":
                $mg2 = True
            "타짜 - 신의 손":
                $mg2 = False
        if mg2:
            haedal_seo "정답입니다!"
        else:
            haedal_yang "아쉽습니다."
            haedal_yang "정답은 2번 \'타짜\'였습니다!"

        haedal_seo "그럼, 다음 문제로 넘어가겠습니다."
        scene mg3
        default mg3 = False
        gyoungmin "나와 주연 선배..였으면 좋겠다."
        menu:
            "타이토닉":
                $mg3 = False
            "러브 쉽(Love ship)":
                $mg3 = False
            "타이타닉":
                $mg3 = True
        if mg3:
            haedal_seo "정답입니다!"
        else:
            haedal_yang "아쉽습니다."
            haedal_yang "정답은 3번 \'타이타닉\'이였습니다!"
        

        haedal_seo "다음은 마지막 문제입니다."
        haedal_seo "조금 어려운데요..?"
        scene mg4
        default mg4 = False
        gyoungmin "내가 어렸을때 자주 보던 짱구잖아?"
        menu:
            "극장판 짱구는 못말려 31기: 우리들의 공룡일기":
                $mg4 = False
            "극장판 짱구는 못말려 3기: 흑부리 마왕의 야망":
                $mg4 = False
            "극장판 짱구는 못말려 13기: 부리부리 3분 대진격":
                $mg4 = True
        if mg4:
            haedal_seo "정답입니다!"
        else:
            haedal_yang "아쉽습니다."
            haedal_yang "정답은 3번 \'부리부리 3분 대진격\'이였습니다!"
        if mg2 and mg3 and mg4:
            haedal_seo "문제를 모두 맞추셨네요!"
            haedal_seo "이러면 1등 확정이겠는데요~"
        elif (mg2 and mg3) or (mg3 and mg4)or (mg2 and mg4):
            haedal_yang "한 문제밖에 안틀렸네요~"
            haedal_seo "영화 좀 봐요 ~ !!"
        elif mg2 or mg3 or mg4:
            haedal_seo "한 문제 맞추셨는데요~"
            haedal_yang "약간 아쉽습니다!"
        else:
            haedal_seo "아~ 이러면 꼴등 확정인가요~?"
            haedal_yang "아쉽습니다."
            haedal_seo "영화! 많이 보세요."
        scene black with fade
        "그러나"
        "그 후 주연 선배의 조 차례에서"
        "현서가 3문제 중 4문제나 맞춰버려"
        "결국 양주를 타지 못했다."
        
        if mg2 and mg3 and mg4:
            "하지만, "
            extend "문제를 모두 맞춘 내게"
            "주연 선배의 묘한 시선이 느껴졌다."
        elif (mg2 and mg3) or (mg3 and mg4)or (mg2 and mg4):
            "문제를 다 맞추지는 못했지만,"
            "자신감 있는 내 모습 때문인지"
            "주연 선배의 시선이 느껴졌다."
        elif mg2 or mg3 or mg4:
            "문제를 한 문제 밖에 맞추지 못했지만,"
            "어떤가"
            "당당했으면 된 거 아닐까"
        else:
            "문제를 하나도 맞추지 못해"
            "부끄러웠지만,"
            "주연 선배의 미소가 느껴졌다."

        hide hyeonseo_standard
        hide juyoun_standard
        
        scene scene3_2_mt_fire


        show juyoun_standard at center
        juyoun "오늘 재미있었어요?"
        gyoungmin "네 ! "
        extend "대학 로망을 하나 이룬거 같아요.."
        juyoun "그래요? "
        extend "다행이네..."
        juyoun "그래서 그런데..."

        "왠지 모를 떨림이 느껴진다."
        
        gyoungmin "네?"

        hide juyoun_standard
        show juyoun_shy at center
        with hpunch
        juyoun "내일 오후에 산책, 같이 갈래요?"

        "그녀의 당황스러운 제안에"
        "시간이 멈춘 거 같았다."
        "어쩌면... "
        extend "내 심장도."

        menu:
            "좋아요!":
                juyoun "크크크"
                juyoun "그럼..."
                hide juyoun_standard
                show juyoun_shy
                juyoun "내일 보는거에요?"
                hide juyoun_shy
                jump scene4

            "지금도 걷고 싶은데요.":
                if juyoun_arr.count(True) == 2 :
                    hide juyoun_standard
                    hide juyoun_shy
                    scene service_1 with fade
                    juyoun "흐흐 "
                    extend "정말요?"
                    juyoun "이거 의외네.."
                    juyoun "그럼 내일 보는 거에요?"
                    scene black with fade
                    "그렇게 해달 MT는 정신없이 끝났다."
                    "어쩌면.. 좋은 추억이 될지도..?"
                else :
                    juyoun "흐흐 "
                    extend "정말요?"
                    hide juyoun_standard
                    show juyoun_shy
                    juyoun "이거 의외네.."
                    hide juyoun_shy
                    show juyoun_love
                    juyoun "그럼 내일 보는 거에요?"
                    hide juyoun_love
                    scene black with fade
                    "그렇게 해달 MT는 정신없이 끝났다."
                    "어쩌면.. 좋은 추억이 될지도..?"

                jump scene4

   
    
    #scene4. 숙취와 출코
    label scene4:
        scene black with fade
        "Zzz..."
        "아.. 숙취때문에 힘들다..."
        "근데.. "
        extend "지금 몇시지??" with vpunch
        scene scene4_wakeup with fade

        gyoungmin "(머리를 싸매며) "
        extend "으... 살려 줘..."
        hyeonseo "(진동)" with vpunch
        hyeonseo "1교시 출석 대신 해줄까?"

        menu:
            "좋아":
                gyoungmin "뭐 "
                extend "나 하나쯤이야 괜찮겠지.."
                   
            "싫어":
                gyoungmin "그치만 들키면 교수님이 실망하실거야.. "
                extend "대신 메일이라도 드려야지."
                "안녕하세요, 교수님."
                "새내기 수학 강의를 수강 중인 [name]입니다."
                "지난 수업에 숙취로 인해 부득이하게 참여하지 못하였습니다."
                "다음 수업부터는 성실히 참여하겠습니다. 감사합니다."
                "[name] 올림"
                gyoungmin "그래도 이정도면 괜찮겠지..?"
                $minsu_love_num = minsu_love_num + 1
                $ minsu_arr[1] = False
                $ minsu_arr[1] = True
        gyoungmin "다시 자야겠다. "
        extend "주연선배와의 약속 전엔 일어나야지.."      
        
        jump scene3_3

    #scene3_3. 첫 캠퍼스 데이트
    label scene3_3:
        scene scene3_3_bench with fade
        hide juyoun_shy
        #scene scene4 with dissolve
        show juyoun_standard at center

        juyoun "여기, 해달 선배들 사이에선 '고백 스팟'이라고 불려요."
        hide juyoun_standard
        show juyoun_standard at center
        with zoomin

        gyoungmin "..ㄴ...네?..."
        hide juyoun_standard
        show juyoun_love
        juyoun "아.. 아직은 아니고요. "
        extend "그냥.. 같이 있고 싶어서 불렀어요."
        gyoungmin "(선배 얼굴이 벚꽃보다 예쁘게 느껴진다...)"
        "순간"
        "나는 지금을 "
        extend "내 스무살 중 가장 아름다운 순간일 거라고"
        "직감했다."
        scene black with fade
        hide juyoun_love
        jump scene5

    #scene5. 중간고사 전 - 밤샘 스터디
    label scene5:
        gyoungmin "이제 곧 중간고사 기간이다.."
        gyoungmin "시간이 너무 빨라 !!" with vpunch
        gyoungmin "그래도.."
        gyoungmin "그동안 즐겼으니 이제 공부해야지.."
        scene scene5_library with fade
        show juyoun_standard at center

        juyoun "이거 마시면서 해요."
        "'선배가 준 에너지 드링크'를 획득했다."
        juyoun "너무 한번에 달리면 탈나요. "
        extend "50분 공부하고 10분 휴식, 이게 효율 최고!"
        gyoungmin "선배도 밤새세요?"
        juyoun "같이 있으면 덜 피곤하잖아요."
        jump scene5_menu

    label scene5_menu:
        scene scene5_library with fade
        show juyoun_standard at center
        menu:
            "아이템을 사용한다.":
                if coffee:
                    gyoungmin "(맞다!"
                    extend " 교수님이 주신 커피가 있었지.)"
                    gyoungmin "선배.. "
                    extend "커피 드실래요?"
                    show juyoun_love
                    juyoun "이런건 또 언제 준비한거에요? "
                    extend "고마워요."
                    gyoungmin "(선배를 보니 휴식이 필요없어진 기분이야....)"
                    hide juyoun_standard
                    $juyoun_love_num = juyoun_love_num + 1 
                    $ juyoun_arr[2] = False
                    $ juyoun_arr[2] = True
                    jump scene6
                else:
                    gyoungmin "마땅히 드릴게 없네.."
                    jump scene5_menu

            "선배와 대화를 시도한다.":
                gyoungmin "공부는 잘 되세요?"
                juyoun "그럭저럭.. 잘 되는 것 같아요."
                gyoungmin "(나도 선배처럼 공부 잘하고 싶다..)"
                hide juyoun_standard
                jump scene6

            "선배에게 족보를 요청한다.":
                gyoungmin "선배, 혹시.. "
                extend "컴퓨터학개론 족보 있으세요?"
                juyoun "아마 태블릿에 있을건데.."
                juyoun "이따 확인하고 보내줄게요."
                gyoungmin "감사합니다 !"
                juyoun "물론 족보는 참고용이니"
                juyoun "너무 의존하지는 마세요."
                gyoungmin "넵!!"
                "'컴퓨터학개론 족보'를 획득했다."
                $jbo = True
                hide juyoun_standard
                jump scene6


    #scene6, 족보만 믿었는데...
    label scene6:
        scene scene2_classroom with fade
        gyoungmin "드디어 시험이다... 준비 한만큼 최선을 다하자!"

        menu:
            "아이템을 사용한다.":
                if jbo:
                    gyoungmin "맞다. "
                    extend "선배가 준 족보가 있었지."
                    gyoungmin "족보만 집중해서 봐야지."
                    scene scene6_af_exam with fade
                    "(웅성웅성)"
                    gyoungmin "헉.. 전부 처음보는 유형이었어..."
                    show hyeonseo_standard
                    hyeonseo "작년 족보 쓸모 없네. "
                    extend "수업이나 열심히 들을걸.."
                else:
                    gyoungmin "쓸만한 아이템이 없네.."
                    gyoungmin "그냥 실력으로 봐야겠다."
                    scene scene6_af_exam with fade
                    "(웅성웅성)"
                    gyoungmin "시험... 망쳐버렸다..."
                    show hyeonseo_standard
                    hyeonseo "너도? 나도..."
                    gyoungmin "그래도... 준비한건 다 풀었더니 후련하다."
                    $minsu_love_num = minsu_love_num + 1
                    $ minsu_arr[2] = False
                    $ minsu_arr[2] = True
                hide hyeonseo_standard
                show juyoun_standard at center
                juyoun "괜찮아요. 시험은 이미 끝났고, "
                extend "아직 남은 프로젝트가 40\%에요."
                juyoun "우리 같이 프로젝트나 해볼까요?"
                gyoungmin "정말요 ??"
                hide juyoun_standard
                show juyoun_love
                juyoun "대신, "
                extend "힘들어도 포기 금지!"

    # 7. 과제 마감 ― 연구실 vs 팀플
    label scene7:
        scene scene7_night_haedalroom with fade 
        show juyoun_standard
        juyoun "함수가 자기 자신을 호출 하는 것을"
        extend "재귀 함수라고 불러요."
        juyoun "꼭 탈출 조건 붙여주기!"
        gyoungmin "조건문에 return;을 넣어주란 말인가요?"
        juyoun "네! 바로 그거에요."
        gyoungmin "선배가 알려주니깐..."
        extend "더 이해가 잘되는데요..?"
        juyoun "흐흐.. 그래요?"
        hide juyoun_standard
        show juyoun_love
        juyoun "그럼 다행이에요"
        hide juyoun_love
        show juyoun_love
        gyoungmin "선배.. 그런데..."
        juyoun "네?"
        gyoungmin "아!"with hpunch
        extend "아니에요!!!" with hpunch
        gyoungmin "잠깐 저 화장실 좀 갔다올게요!!"
        juyoun "크크크"
        extend "그래요. 갔다와요."
        hide juyoun
        scene scene7_bokdo
        gyoungmin "(내 마음을 들킬뻔 했어..)"
        gyoungmin "(어떡하지 어떡하지)"
        show minsu_standard
        minsu "[s_name]군,"
        extend " 아직도 공부중인거예요?"
        gyoungmin "앗, 넵 교수님."
        minsu "밤새느라 고생많네요."
        gyoungmin "하하.."
        gyoungmin "(교수님.. 때문이잖아요..)"
        minsu "음.. "
        extend "혹시.."
        minsu "경민군만 괜찮다면 "
        extend "내일 같이 저녁 먹을래요?"
        minsu "물론 내가 살게요."
        gyoungmin "네... "
        extend "네???" with vpunch
        minsu "별건 아니고.. 이번 중간고사.. 굉장히 잘 쳤길래."
        "왠지 모를 쑥스러움이 그의 얼굴에서 느껴진다."
        gyoungmin "저녁이요..?"
        menu:
            "선배와 약속이 있어서요.":
                gyoungmin "저 주연선배와 약속이 있어서요."
                gyoungmin "다음에 뵈어도 될까요?"
                minsu "아쉽네요"
                minsu "알겠어요."
                minsu "내가 [s_name]군 항상 응원해 ~"
                hide minsu_standard with fade
                "여운찬 뒷모습이다."
                $juyoun_love_num = juyoun_love_num + 1 
                $ juyoun_arr[3] = False
                $ juyoun_arr[3] = True
            "언제가 좋을까요? 언제든 좋아요.":
                minsu "그래요?"
                minsu "[s_name]씨 그럴줄 같았어요."
                minsu "그럼 내일 보는거에요?"
                gyoungmin "네 교수님!"
                "왜일까."
                "뒤돌아가는 교수님의 모습은"
                "마치 사춘기 소년처럼 "
                extend "설렘이 느껴졌다."
                hide minsu_standard with fade
                $minsu_love_num = minsu_love_num + 1
                $ minsu_arr[3] = False
                $ minsu_arr[3] = True
        jump scene8_call


    label scene8_call:
        #전화씬
        scene black
        "(벨소리)" with hpunch
        "(벨소리)" with hpunch
        gyoungmin "으..."
        gyoungmin "몇 신데 전화야.."
        gyoungmin "2시에 누가 전화를..."
        scene scene7_night_gigsa with fade
        show nightcall
        gyoungmin "주연 선배..?" with hpunch
        gyoungmin "이 시간에 어쩐일이지..?" with hpunch
        gyoungmin "일단 받아봐야겠다." with hpunch
        menu:
            "전화받기":
                "딸깍."
        hide nightcall
        show nightcalling
        juyoun "[s_name]"
        extend "이니..?"        
        "그녀의 반쯤 잠긴 목소리가 "
        extend "수화기 너머로 들려왔다."
        gyoungmin "네 선배 .."
        extend "무슨 일이세요?"
        juyoun "...미안해요"
        juyoun "자꾸 너 웃는게 생각나서.."
        juyoun "자는 중이었죠?"
        "창가 사이로 달빛이 새어든다."
        menu:
            "저도 선배 생각중이었는데요":
                gyoungmin "저도 선배 생각중이었는데요"
                juyoun "진짜요?"
                juyoun "헉.."
                "말문이 막힌듯한 선배의 소리에.."
                "잠시 침묵을 유지했다."
                hide nightcalling
                if juyoun_arr.count(True)==4 and juyoun_negai:
                    jump scene8_love
                elif juyoun_arr.count(True)==4 and not juyoun_negai:
                    jump scene8_bye
                else:
                    jump scene8_normal
            "선배, 저 좋아하세요?":
                gyoungmin "선배, 저 좋아하세요?"
                juyoun "네.."
                juyoun "사실 처음부터 마음에 들었어요."
                "떨리는 그녀의 목소리에"
                "내 심장이 떨리기 시작했다."
                gyoungmin "사실 저도.."
                gyoungmin "선배 줄곧 좋아했어요."
                juyoun "고마워요.."
                juyoun "날 좋아해줘서"
                hide nightcalling
                if juyoun_arr.count(True)==4 and juyoun_negai:
                    jump scene8_love
                elif juyoun_arr.count(True)==4 and not juyoun_negai:
                    jump scene8_bye
                else:
                    jump scene8_normal
            "죄송해요, 교수님이 남자로 보여요.":
                gyoungmin "죄송해요, 교수님이 남자로 보여요."
                juyoun "...네"
                juyoun "알겠어요."
                juyoun "잘자요. [s_name]씨"
                hide nightcalling
                "삐삐삐.."
                "어떤 마음이었을까."
                "하지만, "
                extend "가장 중요한 건 내 마음이다."
                "김민수."
                "내 사랑."
                if minsu_arr.count(True):
                    jump scene8_proffessorlove
                else:
                    jump scene8_daehakwon
            "선배, 저는 아직 잘 모르겠어요.":
                gyoungmin "선배, 저는 아직 잘 모르겠어요."
                gyoungmin "이만 자러 갈게요. "
                extend "선배도 안녕히 주무세요."
                juyoun "정말..."
                juyoun "정말로요..?"
                gyoungmin "물론 선배가 좋은 사람이긴하지만.."
                gyoungmin "그 이상은 아니에요."
                juyoun "네.."
                extend "잘자요.. 이만 끊을게요.."
                hide nightcalling
                jump scene8_bad


    label scene8_love:
        "…"
        "시간은 빠르게 흐르고 "
        "어느덧 "
        extend "헤어짐의 순간이 다가오고 있었다."

        juyoun "여기."
        extend " 기억나?"
        gyoungmin "못할리가요."
        gyoungmin "선배를 처음 만난 곳이잖아요."
        juyoun "맞아."
        juyoun "벌써 2년이나 지났네."

        gyoungmin "그때, 동아리 들어온거."
        gyoungmin "제가 대학에 와서 "
        extend "가장 잘 한 선택이었던 것 같아요."
        juyoun "흐흐.. "
        extend "그런 말, 갑자기 들으면… 좀 부끄럽잖아."
        juyoun "그치만.. "
        extend "나도… 네가 있어서 정말 다행이었어."
        juyoun "힘들고 외롭던 시간들도, 너랑 있으니까 견딜 수 있었거든."

        gyoungmin "..."
        gyoungmin "선배... "
        extend "진심으로 졸업 축하드려요..."
        juyoun "...고마워"

        "아아. 잠시 후 진행되는 졸업식 진행을 위해 졸업 대상자분들께서는 대강당으로 이동해 주시기 바랍니다."
        juyoun "...그럼 이제 가볼게."
        gyoungmin "..네 선배"
        #암흑

        "..."
        "..."
        "경민아...!!!" with vpunch
        gyoungmin "ㄴ..네?"
        juyoun "너 덕분에… "
        extend "학교 생활을 버텨낼 수 있었어 !"

        juyoun "웃고, 울고, 힘든 날도 많았지만…"
        juyoun "너가 곁에 있어 그 전부를 버텨낼 수 있었어."

        juyoun "그런데... "
        extend "그런데... 말야..."
        
        juyoun "앞으로 너 없이 이 길을 걷는다는 게… 너무 두려워."

        gyoungmin "선배..."

        juyoun "경민아..."
        juyoun "기억해? 예전에 내가 받은 '소원권'.."
        juyoun "뭐든지 하나 들어준다고 말했던 그거…"

        gyoungmin "... "
        extend "그걸 잊을 리 없잖아요."
 

        juyoun "나… 그걸 지금, 쓸게."
        juyoun "앞으로도 너의 곁에… 남아도 될까?"

        
        menu:
            "당연하지.":
                # 놀란표정
                gyoungmin "나도... 누나와 함께라면"
                gyoungmin "이 길이 더 이상 두렵지 않아."-

                #눈 시울이 붉어지며
                juyoun "경민아… 좋아해."
                juyoun "진심으로... 너를 좋아해."

                gyoungmin "나도..."
                #마무리
                return


    label scene8_normal: 
        "Normal"
        return


    label scene8_bad:
        "bad"
        return

    label scene8_daehakwon: 
        "대학원"
        return


    label scene8_proffessorlove: 
        "민수엔딩"
        return
    
    #호감도 MAX, 소원권X
    label scene8_bye:
        "…"
        "시간은 빠르게 흐르고 "
        "어느덧 "
        scene scene1yard with fade
        extend "헤어짐의 순간이 다가오고 있었다."

        juyoun "여기."
        extend " 기억나?"
        gyoungmin "못할리가요."
        gyoungmin "선배를 처음 만난 곳이잖아요."
        juyoun "맞아."
        juyoun "벌써 2년이나 지났네."

        gyoungmin "그때, 동아리 들어온거."
        gyoungmin "제가 대학에 와서 "
        extend "가장 잘 한 선택이었던 것 같아요."
        juyoun "흐흐.."
        juyoun "나도 너 덕분에"
        juyoun "더 열심히 할 수 있던 거 같아."

        gyoungmin "선배.."
        gyoungmin "졸업 "
        extend "진심으로 축하드려요."
        juyoun "고마워."
        juyoun "나도.."
        extend "멀리 있더라도"
        juyoun "[name], 응원할게."
        "END (2 / 4): 만남, 그리고 끝"
        
        #if jokbo:
        #족보를 썼을 때->시험 문제에 재대로 답 못함.
        #else:
        #족보를 안썼을 때->시험 문제에 대해 청산유수로 답해 호감을 삼. 히든엔딩.      

    return