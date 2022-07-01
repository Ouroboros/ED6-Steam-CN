import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4135_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4135_1 ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4135.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T4135_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xE1F
@scena.StringTable('StringTable')
def StringTable():
    return stringTable

# id: 0x10000 offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x00000000,
            dword_04        = 0x00000000,
            dword_08        = 0x00001770,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 9500,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2800,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 0,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10001 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10002 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('PreInit')
def PreInit():
    EventBegin(0x00)
    Fade(500)
    OP_6D(7120, 4000, -2220, 0)
    OP_67(0, 6860, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(52000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 6870, 4000, -2400, 192)
    SetChrPos(0x0105, 6210, 4000, -1560, 181)
    SetChrPos(0x0104, 7220, 4000, -1410, 180)
    SetChrPos(0x0108, 6750, 4000, -500, 197)
    SetChrPos(0x0009, 7000, 4000, -3740, 0)
    SetChrSubChip(0x0009, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#3260460282V啊，你们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460283V#1000F你好，我们是游击士协会的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460284V看了公告板上的任务委托\n',
            '而来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3260460285V哦哦，正等着呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3260460286V我这就说明委托的事\n',
            '可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_271',
    )

    Call(1, 0x0002)

    Jump('loc_304')

    def _loc_271(): pass

    label('loc_271')

    ChrTalk(
        0x0101,
        (
            '#0010460287V#1016F嗯～对不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460288V现在暂时手头没空。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3260460289V是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3260460290V那么下次有机会\n',
            '麻烦再来好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x00C4, 0x01, 0x8000)

    def _loc_304(): pass

    label('loc_304')

    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0x307
@scena.Code('Init')
def Init():
    EventBegin(0x00)
    Fade(500)
    OP_6D(7120, 4000, -2220, 0)
    OP_67(0, 6860, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(52000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 6870, 4000, -2400, 192)
    SetChrPos(0x0105, 6210, 4000, -1560, 181)
    SetChrPos(0x0104, 7220, 4000, -1410, 180)
    SetChrPos(0x0108, 6750, 4000, -500, 197)
    SetChrPos(0x0009, 7000, 4000, -3740, 0)
    SetChrSubChip(0x0009, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#3260460291V哎呀，可以\n',
            '听我的委托了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Menu(
        0,
        10,
        100,
        0,
        (
            TXT(0x00, '【是】\n'),
            TXT(0x01, '【否】\n'),
        ),
    )

    MenuEnd(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_5F(0x0000)
    OP_56(0x00)
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_42B',
    )

    Call(1, 0x0002)

    Jump('loc_4BE')

    def _loc_42B(): pass

    label('loc_42B')

    ChrTalk(
        0x0101,
        (
            '#0010460287V#1016F嗯～对不起。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460288V现在暂时手头没空。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3260460289V是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3260460290V那么下次有机会\n',
            '麻烦再来好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x00C4, 0x01, 0x8000)

    def _loc_4BE(): pass

    label('loc_4BE')

    EventEnd(0x00)

    Return()

# id: 0x0002 offset: 0x4C1
@scena.Code('ReInit')
def ReInit():
    ChrTalk(
        0x0101,
        (
            '#0010460296V#1000F嗯嗯，没问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460297V#1002F那么……\n',
            '到底是什么被偷了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3260460298V这可怎么说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0009, 90, 400)

    ChrTalk(
        0x0009,
        (
            '#3260460299V你们看这附近\n',
            '不觉得有什么不协调吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_057C')
    def lambda_057C():
        OP_8C(0x0101, 135, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_057C)

    Sleep(100)

    @scena.Lambda('lambda_058F')
    def lambda_058F():
        OP_8C(0x0105, 135, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_058F)

    Sleep(100)

    @scena.Lambda('lambda_05A2')
    def lambda_05A2():
        OP_8C(0x0104, 135, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_05A2)

    Sleep(50)

    @scena.Lambda('lambda_05B5')
    def lambda_05B5():
        OP_8C(0x0108, 135, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_05B5)

    WaitForThreadExit(0x0108, 0x0002)

    ChrTalk(
        0x0101,
        (
            '#0010460300V#1015F不协调……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460301V这里是展示\n',
            '飞船照片的展馆吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460302V嗯～你这么一说\n',
            '是感觉少了点什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060460303V#042F……明白了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060460304V记得那边的墙壁上\n',
            '本来是装饰着\n',
            '『埃尔赛尤』的照片的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    OP_22(0x0027, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010460305V#1004F啊，这么说来……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040460306V#030F唔，我在参观王都时，\n',
            '也记得在这里见过照片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080460307V#072F这么说，被盗的\n',
            '就是那幅埃尔赛尤的照片吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0009, 0, 400)

    ChrTalk(
        0x0009,
        (
            '#3260460308V唔，你观察得没错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_07A0')
    def lambda_07A0():
        OP_8C(0x0101, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_07A0)

    Sleep(100)

    @scena.Lambda('lambda_07B3')
    def lambda_07B3():
        OP_8C(0x0105, 180, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0002, lambda_07B3)

    Sleep(100)

    @scena.Lambda('lambda_07C6')
    def lambda_07C6():
        OP_8C(0x0104, 180, 400)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_07C6)

    Sleep(50)

    @scena.Lambda('lambda_07D9')
    def lambda_07D9():
        OP_8C(0x0108, 180, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_07D9)

    WaitForThreadExit(0x0108, 0x0002)

    ChrTalk(
        0x0009,
        (
            '#3260460309V早上确实还在的\n',
            '过了中午，不知\n',
            '什么时候就不见了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3260460310V取而代之的是这张卡\n',
            '贴在墙上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    OP_AD(0x00240093, 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170460311V　　美丽的公主及其随从啊。　　\n',
            '　　 高尚的白鹰的剪影画\n',
            '　　    飘落在我手中。　　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170460312V　　  如果就想要寻求它\n',
            '　　  就要回应我的挑战。 　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170460313V　  第一把钥匙在老将之居。　　\n',
            '　 探索『时间的旁观者』吧。　　',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010460314V#1007F哦……\n',
            '又是那家伙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060460315V#045F伤、伤脑筋啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040460316V#035F呼，看来他已经\n',
            '燃起了针对我的抗争心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080460317V#073F怪盗绅士布卢布兰……\n',
            '『噬身之蛇』的执行者吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080460318V#072F传闻倒是听过，\n',
            '好像是个相当特立独行的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3260460319V嗬，已经有\n',
            '犯人的线索了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3260460320V这真令人振奋。\n',
            '就拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460321V#1000F嗯，知道了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460322V那么马上就去\n',
            '调查如何呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x00C4, 0x04, 0x04)
    OP_28(0x00C4, 0x04, 0x08)
    OP_28(0x00C4, 0x01, 0x0001)
    OP_28(0x00C4, 0x01, 0x0002)

    Return()

# id: 0x0003 offset: 0xB52
@scena.Code('func_03_B52')
def func_03_B52():
    EventBegin(0x00)
    FadeOut(0, 0, -1)
    OP_6D(7120, 4000, 4420, 0)
    OP_67(0, 6860, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(52000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 6870, 4000, -2400, 192)
    SetChrPos(0x0105, 6210, 4000, -1560, 181)
    SetChrPos(0x0104, 7220, 4000, -1410, 180)
    SetChrPos(0x0108, 6750, 4000, -500, 197)
    SetChrPos(0x0009, 7000, 4000, -3740, 0)
    SetChrSubChip(0x0009, 0)
    OP_4A(0x0009, 255)
    OP_72(0x0001, 0x0004)
    FadeIn(1000, 0)
    OP_6D(7120, 4000, -2220, 4000)

    ChrTalk(
        0x0009,
        (
            '#3260460410V呀，真是帮大忙了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3260460411V可是，那个怪盗什么的\n',
            '为什么要偷埃尔赛尤的照片\n',
            '这种东西呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3260460412V虽然是很棒，但也不过是照片，\n',
            '也没多大价值嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460413V#1015F唉，一定要说的话\n',
            '就是算是故意\n',
            '怄我们生气吧……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460414V#1013F因为这个，实在抱歉。\n',
            '或许是把您卷进来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3260460415V哈哈，不必道歉。\n',
            '又不是你们干的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#3260460416V总之真是辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName('')
    OP_22(0x0017, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【消失的展览品】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_28(0x00C4, 0x04, 0x10)
    OP_28(0x00C4, 0x01, 0x0200)
    OP_A2(0x0003)
    OP_4B(0x0009, 255)
    SetChrPos(0x0009, 7000, 4000, -3740, 90)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
