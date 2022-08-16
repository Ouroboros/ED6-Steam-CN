import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0130_1_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0130_1 ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'C0403.x'
    header.mapIndex       = 1
    header.bgm            = 10
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0130_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
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

# id: 0x10000 offset: 0xA8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
    ]

# id: 0x10001 offset: 0xA8
@scena.NpcData('NpcData')
def NpcData():
    return (
    )

# id: 0x10002 offset: 0xA8
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xA8
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xA8
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0xA8
@scena.Code('Init')
def Init():
    EventBegin(0x00)
    Fade(1000)
    Call(1, 0x0004)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_17A',
    )

    ChrTalk(
        0x00FE,
        (
            '#3420460417V嗯～…………\n',
            '虽然大圣堂也很有吸引力，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3420460418V但结婚仪式还是\n',
            '在家乡洛连特举办最好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3420460419V在初次相遇的地方进行爱的宣誓… \n',
            '真有种神圣又纯粹的感觉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_315')

    def _loc_17A(): pass

    label('loc_17A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_1E9',
    )

    ChrTalk(
        0x00FE,
        (
            '#3420460420V啊啊～～我可爱的艾娅莉啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3420460421V我要像浓雾包裹城镇那样\n',
            '将你紧紧抱住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_315')

    def _loc_1E9(): pass

    label('loc_1E9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_23F',
    )

    ChrTalk(
        0x00FE,
        (
            '#3420460422V再离我近一点，艾娅莉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3420460423V我只想看你的笑脸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_315')

    def _loc_23F(): pass

    label('loc_23F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_315',
    )

    ChrTalk(
        0x00FE,
        (
            '#3420460424V啊啊！！美丽的诞辰庆典之夜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3420460425V艾娅莉……每次看到你的脸\n',
            '就会想起那个美妙的夜晚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3420460426V在星空和花火的映衬下，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3420460427V我鼓起勇气向你袒露\n',
            '心意的那个夜晚… ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_315(): pass

    label('loc_315')

    ChrTalk(
        0x0101,
        (
            '#0010460428V#1007F#3P打、打扰了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460429V请问现在方便吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x000F,
        (
            '#3420460430V嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0393')
    def lambda_0393():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0393)

    Sleep(250)

    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#3430460431V#2P……啊，是谁？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460432V#1000F#3P我们是游击士协会的人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460433V您就是阿鲁姆先生吗？\n',
            '我们是看了告示板上的委托而来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460434V哇～终于来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460435V太好了！\n',
            '我等你们好久了！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x000F, 400)

    ChrTalk(
        0x0010,
        (
            '#3430460436V#2P太好了！阿鲁姆！\n',
            '我好高兴啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0010, 400)

    ChrTalk(
        0x000F,
        (
            '#3420460437V啊啊～艾娅莉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460438V你的心灵为什么\n',
            '这样美丽？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460439V明明让你痛苦\n',
            '的人就是我…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#3430460440V#2P不要那么说，阿鲁姆。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#3430460441V#2P你心中的痛苦\n',
            '我全都明白！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#3430460442V#2P那一夜，咱们不是约定好了吗？\n',
            '不管到什么时候，你和我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460443V……也要携手\n',
            '走完一生…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460444V啊啊！！艾娅莉！我爱你！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#3430460445V#2P我也是啊！阿鲁姆！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0029, 0x00000000, 1700, 0x0A, 0x0B, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    Sleep(1500)

    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(150)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6D8',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_716')

    def _loc_6D8(): pass

    label('loc_6D8')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6FF',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_716')

    def _loc_6FF(): pass

    label('loc_6FF')

    OP_62(0x00F8, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    def _loc_716(): pass

    label('loc_716')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_73D',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_77B')

    def _loc_73D(): pass

    label('loc_73D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_764',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_77B')

    def _loc_764(): pass

    label('loc_764')

    OP_62(0x00F9, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    def _loc_77B(): pass

    label('loc_77B')

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010460446V#1016F#3P那、那个～……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460447V您有什么\n',
            '请求呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(400)

    ChrTalk(
        0x000F,
        (
            '#3420460448V啊……！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#3430460449V#2P对了！委托！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0824')
    def lambda_0824():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0824)

    Sleep(150)

    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x000F,
        (
            '#3420460450V其、其实是一件关系到我们两个\n',
            '将来的重要事件！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460451V希望你们马上就开始调查，\n',
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
        'loc_904',
    )

    Call(1, 0x0002)

    Jump('loc_AA4')

    def _loc_904(): pass

    label('loc_904')

    ChrTalk(
        0x0101,
        (
            '#0010460452V#1015F#3P啊～抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460453V马上开始的话\n',
            '可能有些困难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460454V怎、怎么会…\n',
            '请不要抛弃我们啊！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#3430460455V#2P求你们了……\n',
            '这件事真的很重要！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460456V#020F没关系，\n',
            '我们会回来的，放心吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460457V#1000F#3P嗯，等我们有空的时候\n',
            '一定回来仔细听你们说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460458V真、真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460459V好、好… \n',
            '我相信你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#3430460460V#2P一定要再来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0072, 0x01, 0x8000)

    def _loc_AA4(): pass

    label('loc_AA4')

    ChrTurnDirection(0x0010, 0x000F, 0)
    ChrTurnDirection(0x000F, 0x0010, 0)
    OP_4B(0x000F, 255)
    OP_4B(0x0010, 255)
    EventEnd(0x00)

    Return()

# id: 0x0001 offset: 0xABD
@scena.Code('func_01_ABD')
def func_01_ABD():
    EventBegin(0x00)
    Fade(1000)
    Call(1, 0x0004)
    ChrSetDirection(0x000F, 270, 0)
    ChrSetDirection(0x0010, 270, 0)
    OP_0D()

    ChrTalk(
        0x000F,
        (
            '#3420460497V那个、各位游击士……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460498V你们..可以接受\n',
            '我的委托吗？',
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
        'loc_B82',
    )

    Call(1, 0x0002)

    Jump('loc_C30')

    def _loc_B82(): pass

    label('loc_B82')

    ChrTalk(
        0x0101,
        (
            '#0010460499V#1007F呼、呼……\n',
            '现在确实还有点为难呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460500V怎、怎么会…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460501V#1016F抱歉抱歉。\n',
            '下次再来听你们说明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#3430460502V嗯，会再来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C30(): pass

    label('loc_C30')

    ChrTurnDirection(0x0010, 0x000F, 0)
    ChrTurnDirection(0x000F, 0x0010, 0)
    OP_4B(0x000F, 255)
    OP_4B(0x0010, 255)
    EventEnd(0x00)

    Return()

# id: 0x0002 offset: 0xC49
@scena.Code('func_02_C49')
def func_02_C49():
    ChrTalk(
        0x0101,
        (
            '#0010460509V#1006F啊，嗯。\n',
            '没问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_D6F',
    )

    ChrTalk(
        0x000F,
        (
            '#3420460510V真、真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460511V#020F只是，既然很急的话，\n',
            '就麻烦您长话短说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460512V啊啊～那个倒无所谓！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460513V呀～不管怎样，\n',
            '多谢你们了，游击士！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460514V你们能来……\n',
            '真是救了我们一命啊！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DC0')

    def _loc_D6F(): pass

    label('loc_D6F')

    ChrTalk(
        0x000F,
        (
            '#3420460510V真、真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460516V太感谢了！！\n',
            '谢谢了！！游击士！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_DC0(): pass

    label('loc_DC0')

    ChrTurnDirection(0x0010, 0x000F, 400)

    ChrTalk(
        0x0010,
        (
            '#3430460436V#2P太好了！阿鲁姆！\n',
            '我好高兴啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0010, 400)

    ChrTalk(
        0x000F,
        (
            '#3420460437V啊啊～艾娅莉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460519V为什么你的心灵\n',
            '这样美丽？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#3430460520V#2P啊啊～阿鲁姆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010460521V#1019F#4S……#2S',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460522V……我说委托的事……～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0EC3')
    def lambda_0EC3():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_0EC3)

    Sleep(150)

    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x000F,
        (
            '#3420460523V……失礼了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460524V那么，请听我说吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460525V#020F嗯，可能的话，请您尽量说简洁点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460526V想委托各位帮忙的事情并不是别的，\n',
            '就是寻找我们的结婚戒指。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460527V我拼命攒钱，好不容易\n',
            '买到了那个高档戒指，可是… ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460528V那、那只可恨的小偷乌鸦，\n',
            '竟然把它给偷走了！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010460529V#1004F#3P乌、乌鸦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_109D',
    )

    ChrTalk(
        0x0107,
        (
            '#0070460530V#064F乌鸦……是那只鸟吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_115A')

    def _loc_109D(): pass

    label('loc_109D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_10DD',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460531V#044F乌鸦吗……难道是那只鸟？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_115A')

    def _loc_10DD(): pass

    label('loc_10DD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1121',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460532V#033F所谓的乌鸦……是指那只鸟吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_115A')

    def _loc_1121(): pass

    label('loc_1121')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_115A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460533V#052F乌鸦……是那只鸟吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_115A(): pass

    label('loc_115A')

    ChrTalk(
        0x000F,
        (
            '#3420460534V对！总之就是那个哇哇叫的混帐了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460535V那个可恶的家伙竟然\n',
            '把我们的结婚戒指给叼跑了！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x01, 0x4000)"),
            (Expr.Eval, "OP_40(0x0234, 0x00)"),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_16D1',
    )

    ChrTalk(
        0x0103,
        (
            '#0030460536V#026F确实，乌鸦的习性就是\n',
            '喜欢收集闪光的东西呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460537V#027F话虽如此……\n',
            '戒指被乌鸦偷走，还真是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010460538V#1011F啊、难道说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460539V雪拉姐也\n',
            '想起那个戒指了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460540V#020F嗯，保险起见，\n',
            '最好是给他看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460541V？？？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460542V有什么线索吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010460543V#1002F阿鲁姆先生，请您\n',
            '看一下这只戒指可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460544V#6A嗯、当然……',
            TxtCtl.Enter,
        ),
    )

    Call(1, 0x0005)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010460545V#1004F咦咦！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1415',
    )

    ChrTalk(
        0x0107,
        (
            '#0070460546V#064F那个那个……\n',
            '确实就是这只戒指吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14F0')

    def _loc_1415(): pass

    label('loc_1415')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_144D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460547V#044F没、没搞错吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14F0')

    def _loc_144D(): pass

    label('loc_144D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1485',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460548V#033F那个、没弄错吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14F0')

    def _loc_1485(): pass

    label('loc_1485')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14C1',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460549V#055F喂喂、不会是真的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14F0')

    def _loc_14C1(): pass

    label('loc_14C1')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_14F0',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460550V#073F没弄错吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14F0(): pass

    label('loc_14F0')

    ChrTalk(
        0x000F,
        (
            '#3420460551V嗯、嗯……绝对没错！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460552V这就是我们的戒指！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#3430460553V#2P啊啊！！女神啊……\n',
            '衷心感谢您的恩德！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460554V#021F呵呵，没想到\n',
            '会这么巧啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_15E6',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460555V#073F真是惊人的巧合呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_169E')

    def _loc_15E6(): pass

    label('loc_15E6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1622',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460556V#052F真是好惊人的巧合呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_169E')

    def _loc_1622(): pass

    label('loc_1622')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1665',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460557V#031F哈哈哈。\n',
            '真是惊人的巧合啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_169E')

    def _loc_1665(): pass

    label('loc_1665')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_169E',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460558V#044F好、好惊人的巧合啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_169E(): pass

    label('loc_169E')

    Call(1, 0x0006)
    OP_28(0x0072, 0x01, 0x0008)
    OP_28(0x0072, 0x01, 0x0010)
    OP_28(0x0072, 0x04, 0x10)
    ChrTurnDirection(0x0010, 0x000F, 0)
    ChrTurnDirection(0x000F, 0x0010, 0)
    OP_63(0x0029)
    OP_4B(0x000F, 255)
    OP_4B(0x0010, 255)
    EventEnd(0x00)

    Jump('loc_1EA7')

    def _loc_16D1(): pass

    label('loc_16D1')

    ChrTalk(
        0x0103,
        (
            '#0030460559V#027F确实、乌鸦具有\n',
            '喜欢收集闪亮东西的习性。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460560V所以会对戒指这种东西\n',
            '感兴趣的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460561V#1015F#3P那么、戒指现在\n',
            '应该在它们的巢中吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460562V#1002F是让我们来找那戒指的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460563V嗯、那就是我们\n',
            '想委托你们办的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460564V虽然我明白，\n',
            '这件事很困难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460565V但即使如此，\n',
            '也拜托你们尽力帮我们吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460566V#1007F#3P嗯，我们肯定\n',
            '会尽力而为，不过…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460567V以现有的情报来说，\n',
            '实在是不容易找到。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460568V#1002F……能不能再提供给我们一些线索呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460569V啊啊，是要寻找\n',
            '乌鸦的巢穴了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460570V大概在洛连特北部吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460571V那家伙飞向玛鲁加山道\n',
            '那边去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460572V再加上现在起了大雾，\n',
            '能追上的可能性不大了吧…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_29(0x0072, 0x01, 0x4000)"),
            (Expr.Eval, "OP_40(0x0234, 0x00)"),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1B01',
    )

    ChrTalk(
        0x0101,
        (
            '#0010460573V#1015F#3P原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460574V巢穴大概在北边吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460575V…啊？北边？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    OP_63(0x0101)

    ChrTalk(
        0x0101,
        (
            '#0010460576V#1019F#3P（难、难道说……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460577V（在塔顶上\n',
            '  发现的那个戒指…）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460578V嗯？怎么啦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460579V#1016F#3P呼、呼呼。没什么。\n',
            '（一定只是心理作用吧～）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B48')

    def _loc_1B01(): pass

    label('loc_1B01')

    ChrTalk(
        0x0101,
        (
            '#0010460573V#1015F#3P原来如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460581V巢穴大概在北边吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B48(): pass

    label('loc_1B48')

    ChrTalk(
        0x0103,
        (
            '#0030460582V#026F……我们会做个参考的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460583V不管怎样，巢穴肯定\n',
            '是在高处就对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C0F',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460584V#075F啊，那肯定没错的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080460585V真是的……\n',
            '这真是个麻烦的工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D14')

    def _loc_1C0F(): pass

    label('loc_1C0F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1C76',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460586V#551F嗯，那肯定没错。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050460587V真是的……\n',
            '还真是个麻烦的工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D14')

    def _loc_1C76(): pass

    label('loc_1C76')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1CDD',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460588V#034F嗯，那是肯定的啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040460589V呼～还真是件\n',
            '超级麻烦的工作啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D14')

    def _loc_1CDD(): pass

    label('loc_1CDD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1D14',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460590V#047F嗯，确实比较麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D14(): pass

    label('loc_1D14')

    ChrTalk(
        0x000F,
        (
            '#3420460591V除了协会之外，\n',
            '我们再也找不到人可以拜托了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460592V所以无论如何\n',
            '你们也要帮帮忙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#3430460593V#2P你们是我们唯一的希望了。\n',
            '无论如何也请帮忙找找吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460594V#1006F#3P嗯……\n',
            '我们会努力找找看的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460595V#020F那么，有什么发现的话，\n',
            '我们会再来报告给您。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460596V期待大家！我们会一直等的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#3430460597V#2P加油哦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0072, 0x04, 0x04)
    OP_28(0x0072, 0x04, 0x08)
    OP_28(0x0072, 0x01, 0x0001)
    OP_28(0x0072, 0x01, 0x0002)
    SetScenaFlags(ScenaFlag(0x0001, 3, 0xB))
    ChrClearFlags(0x000F, 0x0010)
    def _loc_1EA7(): pass

    label('loc_1EA7')

    Return()

# id: 0x0003 offset: 0x1EA8
@scena.Code('func_03_1EA8')
def func_03_1EA8():
    EventBegin(0x00)
    Fade(1000)
    Call(1, 0x0004)
    OP_0D()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0340, 0, 0x1A00)),
            Expr.Return,
        ),
        'loc_1F7A',
    )

    ChrTalk(
        0x00FE,
        (
            '#3420460417V嗯～…………\n',
            '虽然大圣堂也很有吸引力，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3420460418V但结婚仪式还是\n',
            '在家乡洛连特举办最好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3420460419V在初次相遇的地方进行爱的宣誓… \n',
            '真有种神圣又纯粹的感觉啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2115')

    def _loc_1F7A(): pass

    label('loc_1F7A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0304, 2, 0x1822)),
            Expr.Return,
        ),
        'loc_1FE9',
    )

    ChrTalk(
        0x00FE,
        (
            '#3420460420V啊啊～～我可爱的艾娅莉啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3420460421V我要像浓雾包裹城镇那样\n',
            '将你紧紧抱住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2115')

    def _loc_1FE9(): pass

    label('loc_1FE9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0303, 4, 0x181C)),
            Expr.Return,
        ),
        'loc_203F',
    )

    ChrTalk(
        0x00FE,
        (
            '#3420460422V再离我近一点，艾娅莉！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3420460423V我只想看你的笑脸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2115')

    def _loc_203F(): pass

    label('loc_203F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0301, 4, 0x180C)),
            Expr.Return,
        ),
        'loc_2115',
    )

    ChrTalk(
        0x00FE,
        (
            '#3420460424V啊啊！！美丽的诞辰庆典之夜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3420460425V艾娅莉……每次看到你的脸\n',
            '就会想起那个美妙的夜晚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3420460426V在星空和花火的映衬下，',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#3420460427V我鼓起勇气向你袒露\n',
            '心意的那个夜晚… ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2115(): pass

    label('loc_2115')

    ChrTalk(
        0x0101,
        (
            '#0010460698V#1007F（还、还没停啊……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460430V嗯……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2161')
    def lambda_2161():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_2161)

    Sleep(250)

    ChrTurnDirection(0x0010, 0x0101, 400)

    ChrTalk(
        0x0010,
        (
            '#3430460700V#2P……啊，游击士啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000F, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    OP_63(0x000F)

    ChrTalk(
        0x000F,
        (
            '#3420460701V难、难道\n',
            '你们找到戒指了！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460702V#020F嗯，找到了一只符合您\n',
            '说明的戒指。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460703V但不知道是不是您\n',
            '丢失的那个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460704V#1000F所以\n',
            '希望您能确认一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460705V阿鲁姆先生，\n',
            '看一下这只戒指可以吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460706V#6A嗯、当然……',
            TxtCtl.Enter,
        ),
    )

    Call(1, 0x0005)

    ChrTalk(
        0x0101,
        (
            '#0010460710V#1004F真、真的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2337',
    )

    ChrTalk(
        0x0107,
        (
            '#0070460546V#064F那个那个……\n',
            '确实就是这只戒指吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2412')

    def _loc_2337(): pass

    label('loc_2337')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_236F',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460547V#044F没、没搞错吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2412')

    def _loc_236F(): pass

    label('loc_236F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23A7',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460548V#033F那个、没弄错吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2412')

    def _loc_23A7(): pass

    label('loc_23A7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23E3',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460549V#055F喂喂、不会是真的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2412')

    def _loc_23E3(): pass

    label('loc_23E3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2412',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460550V#073F没弄错吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2412(): pass

    label('loc_2412')

    ChrTalk(
        0x000F,
        (
            '#3420460551V嗯、嗯……绝对没错！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460552V这就是我们的戒指！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#3430460553V#2P啊啊！！女神啊……\n',
            '衷心感谢您的恩德！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460719V#021F呵呵，太好了。\n',
            '终于物归原主了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2535',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460720V#070F呼，真是没想到啊，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080460721V竟然会在那种\n',
            '地方找到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_268D')

    def _loc_2535(): pass

    label('loc_2535')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25B3',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460722V#040F太好了……\n',
            '这样的话事情也就解决了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060460723V真是做梦也想不到会在\n',
            '那种地方找到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_268D')

    def _loc_25B3(): pass

    label('loc_25B3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2627',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460724V#051F啊啊，总算是解决了，\n',
            '松了口气。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050460725V真是没想到会在\n',
            '那种地方找到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_268D')

    def _loc_2627(): pass

    label('loc_2627')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_268D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460726V#030F呼～真是不容易啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040460727V真没想到竟然会在\n',
            '那种地方找到啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_268D(): pass

    label('loc_268D')

    Call(1, 0x0006)
    OP_28(0x0072, 0x01, 0x0010)
    OP_28(0x0072, 0x04, 0x10)
    ChrTurnDirection(0x0010, 0x000F, 0)
    ChrTurnDirection(0x000F, 0x0010, 0)
    OP_63(0x0029)
    OP_4B(0x000F, 255)
    OP_4B(0x0010, 255)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x26B8
@scena.Code('func_04_26B8')
def func_04_26B8():
    OP_4A(0x000F, 255)
    OP_4A(0x0010, 255)
    ChrSetPos(0x0101, 62800, 0, 47270, 90)
    ChrSetPos(0x0103, 61790, 0, 46800, 90)
    ChrSetPos(0x00F8, 61270, 0, 47980, 90)
    ChrSetPos(0x00F9, 60320, 0, 47290, 90)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2733',
    )

    ChrSetPos(0x00F9, 61270, 0, 47980, 90)
    ChrSetPos(0x00F8, 60320, 0, 47290, 90)

    def _loc_2733(): pass

    label('loc_2733')

    CameraMove(61800, 0, 48260, 0)
    OP_67(0, 6130, -10000, 0)
    CameraSetDistance(2870, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)

    ExecExpressionWithValue(
        0x0029,
        0x01,
        (
            (Expr.GetChrWork, 0xF, 0x1),
            (Expr.GetChrWork, 0x10, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0029,
        0x02,
        (
            (Expr.GetChrWork, 0xF, 0x2),
            (Expr.GetChrWork, 0x10, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x0029,
        0x03,
        (
            (Expr.GetChrWork, 0xF, 0x3),
            (Expr.GetChrWork, 0x10, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0005 offset: 0x27B0
@scena.Code('func_05_27B0')
def func_05_27B0():
    OP_94(0x01, 0x000F, 0x0000, 0x000000C8, 0x000003E8, 0x00)
    OP_56(0x00)
    OP_59()
    OP_62(0x000F, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(100)

    @scena.Lambda('lambda_27E4')
    def lambda_27E4():
        ChrJumpToRelative(0x00FE, 0, 0, 0, 400, 4000)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_27E4)

    Sleep(900)

    OP_63(0x000F)
    WaitForThreadExit(0x000F, 0x0001)

    ChrTalk(
        0x000F,
        (
            '#3420460707V#3S……啊啊啊啊啊啊啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460708V那那那、那个戒指！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460709V#3S那不就是我、我们的结婚戒指吗！！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 500, 3000, 100)
    CloseMessageWindow()

    Return()

# id: 0x0006 offset: 0x28A1
@scena.Code('func_06_28A1')
def func_06_28A1():
    ChrTalk(
        0x0101,
        (
            '#0010460761V#1015F呼、真是无话可说了…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460762V城镇市民的戒指\n',
            '最后竟然在塔顶找到…',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460763V#1000F……呵呵～不过还是\n',
            '先把戒指还给他吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.Item, ItemTable['白金戒指']),
            (TxtCtl.SetColor, 0x0),
            '交出了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    RemoveItem(ItemTable['白金戒指'], 1)
    OP_94(0x01, 0x000F, 0x00B4, 0x000000C8, 0x000003E8, 0x00)

    ChrTalk(
        0x000F,
        (
            '#3420460764V啊、谢谢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460765V真是感激不尽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#3430460766V#2P呵呵，相信游击士\n',
            '果然没有错㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460767V#1017F哪里哪里，没什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030460768V#020F马上就要\n',
            '结婚了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030460769V#525F祝你们幸福哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0010, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    Sleep(1000)

    ChrTalk(
        0x0010,
        (
            '#3430460770V#2P喔…………\n',
            '啊、谢谢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#3430460771V#2P感、感觉真好啊！\n',
            '被人祝福的感觉…',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000F, 0x0010, 400)

    ChrTalk(
        0x000F,
        (
            '#3420460772V不过我们会尽快习惯的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460773V我们的未来一定会\n',
            '得到无数的祝福的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0010, 0x000F, 400)

    ChrTalk(
        0x0010,
        (
            '#3430460520V#2P啊啊～阿鲁姆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#3420460775V艾娅莉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0029, 0x00000000, 1800, 0x0A, 0x0B, 0x000000FA, 0x00)
    Sleep(1000)

    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0103, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(100)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C03',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_2C41')

    def _loc_2C03(): pass

    label('loc_2C03')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C2A',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_2C41')

    def _loc_2C2A(): pass

    label('loc_2C2A')

    OP_62(0x00F8, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    def _loc_2C41(): pass

    label('loc_2C41')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C68',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_2CA6')

    def _loc_2C68(): pass

    label('loc_2C68')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2C8F',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    Jump('loc_2CA6')

    def _loc_2C8F(): pass

    label('loc_2C8F')

    OP_62(0x00F9, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    def _loc_2CA6(): pass

    label('loc_2CA6')

    Sleep(1000)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2CFD',
    )

    ChrTalk(
        0x0107,
        (
            '#0070460776V#067F（啊哈～……\n',
            '　完全沉浸在二人世界中了啊。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DD2')

    def _loc_2CFD(): pass

    label('loc_2CFD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D47',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460777V#540F（完、完全沉浸在二人世界中了啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DD2')

    def _loc_2D47(): pass

    label('loc_2D47')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2D91',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460778V#030F（呼～彻底沉浸在二人世界里了啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2DD2')

    def _loc_2D91(): pass

    label('loc_2D91')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2DD2',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460779V#070F（这就是所谓的二人世界吗。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2DD2(): pass

    label('loc_2DD2')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2E18',
    )

    ChrTalk(
        0x0106,
        (
            '#0050460780V#552F（好像完全无视我们的存在呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EDF')

    def _loc_2E18(): pass

    label('loc_2E18')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2E5E',
    )

    ChrTalk(
        0x0108,
        (
            '#0080460781V#071F（哈哈，恋爱果然是盲目的呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EDF')

    def _loc_2E5E(): pass

    label('loc_2E5E')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2EA4',
    )

    ChrTalk(
        0x0104,
        (
            '#0040460782V#031F（呵呵，恋爱果然是盲目的啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2EDF')

    def _loc_2EA4(): pass

    label('loc_2EA4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2EDF',
    )

    ChrTalk(
        0x0105,
        (
            '#0060460783V#048F（不过……真不错呢。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2EDF(): pass

    label('loc_2EDF')

    ChrTalk(
        0x0103,
        (
            '#0030460784V#020F（咱们好像太打扰他们了……\n',
            '　还是赶快离开吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010460785V#1013F（说、说的是啊。）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010460786V#1016F那、那么、\n',
            '我们这就走了哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    TalkSetChrName('')
    PlaySE(23, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x2),
            '任务【消失在天空的定婚戒指】',
            (TxtCtl.SetColor, 0x0),
            '完成了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    ChrSetFlags(0x000F, 0x0010)
    ChrSetFlags(0x0010, 0x0010)
    SetScenaFlags(ScenaFlag(0x0001, 4, 0xC))

    Return()

# id: 0x0007 offset: 0x2FE5
@scena.Code('func_07_2FE5')
def func_07_2FE5():
    EventBegin(0x00)
    UnlockAchievement(0x01, 0x0003, 0x00)
    LoadChip('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP', 8)
    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0008, -17310, 0, 42890, 270)
    ChrSetPos(0x0011, -15330, 0, 42890, 270)
    ChrSetPos(0x0101, -16070, 0, 44880, 180)
    ChrSetPos(0x0103, -15100, 0, 45270, 180)
    ChrSetPos(0x00F8, -16480, 0, 46150, 180)
    ChrSetPos(0x00F9, -15220, 0, 46480, 180)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3090',
    )

    ChrSetPos(0x00F9, -16480, 0, 46150, 180)
    ChrSetPos(0x00F8, -15220, 0, 46480, 180)

    def _loc_3090(): pass

    label('loc_3090')

    CameraMove(-17110, 0, 44470, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_4A(0x0008, 255)
    ChrSetFlags(0x0009, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    Sleep(2000)

    ChrMoveTo(0x0008, -16830, 0, 42890, 1000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#1080470646V──嗯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0011, 400)

    ChrTalk(
        0x0008,
        (
            '#1080470647V让您久等了。\n',
            '药已经做完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080470648V请拿去吧。\n',
            '这就是『千杯不醉的秘药』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0011, -15710, 0, 42890, 1000, 0x00)

    ChrTalk(
        0x0011,
        (
            '#3600470649V咕、咕噜……（吞口水）\n',
            '这就是我一直苦苦寻找的秘药……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3600470650V服下之后不管怎么喝酒\n',
            '也绝不会喝醉的秘药吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080470651V对，没错，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080470652V要想让药生效的话，必须要严格遵照\n',
            '规定的用法和用量……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3600470653V#10A#3S呀呵───！！！\n',
            '终于到手啦───！！！',
            TxtCtl.Enter,
        ),
    )

    ChrSetFlags(0x0011, 0x0020)

    @scena.Lambda('lambda_32CD')
    def lambda_32CD():
        ChrJumpToRelative(0x00FE, 0, 0, 0, 2000, 1000)

        ExitThread()

    DispatchAsync(0x0011, 0x0000, lambda_32CD)

    ChrSetDirection(0x0011, 0, 1600)
    ChrSetDirection(0x0011, 90, 1600)
    ChrSetDirection(0x0011, 180, 1600)
    ChrSetDirection(0x0011, 270, 1600)
    ChrSetDirection(0x0011, 0, 1600)
    ChrSetDirection(0x0011, 90, 1600)
    ChrSetDirection(0x0011, 180, 1600)
    ChrSetDirection(0x0011, 270, 1600)
    WaitForThreadExit(0x0011, 0x0000)
    ChrClearFlags(0x0011, 0x0020)
    Sleep(500)

    ChrTalk(
        0x0011,
        (
            '#3600470654V#3S这、这样的话我终于可以挺起\n',
            '胸膛向爱娜小姐告白了──！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_CB(0xF6)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_339D',
    )

    OP_62(0x00F6, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_33DB')

    def _loc_339D(): pass

    label('loc_339D')

    If(
        (
            (Expr.Eval, "OP_CB(0xF6)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_33C4',
    )

    OP_62(0x00F6, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_33DB')

    def _loc_33C4(): pass

    label('loc_33C4')

    OP_62(0x00F6, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_33DB(): pass

    label('loc_33DB')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3402',
    )

    OP_62(0x00F9, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_3440')

    def _loc_3402(): pass

    label('loc_3402')

    If(
        (
            (Expr.Eval, "OP_CB(0xF9)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3429',
    )

    OP_62(0x00F9, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_3440')

    def _loc_3429(): pass

    label('loc_3429')

    OP_62(0x00F9, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_3440(): pass

    label('loc_3440')

    Sleep(120)

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_346C',
    )

    OP_62(0x00F7, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_34AA')

    def _loc_346C(): pass

    label('loc_346C')

    If(
        (
            (Expr.Eval, "OP_CB(0xF7)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3493',
    )

    OP_62(0x00F7, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_34AA')

    def _loc_3493(): pass

    label('loc_3493')

    OP_62(0x00F7, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_34AA(): pass

    label('loc_34AA')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34D1',
    )

    OP_62(0x00F8, 0x00000000, 2300, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_350F')

    def _loc_34D1(): pass

    label('loc_34D1')

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_34F8',
    )

    OP_62(0x00F8, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    Jump('loc_350F')

    def _loc_34F8(): pass

    label('loc_34F8')

    OP_62(0x00F8, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    def _loc_350F(): pass

    label('loc_350F')

    Sleep(800)

    ChrTalk(
        0x0101,
        (
            '#0010470655V#1004F#1P#3S──哎哎哎哎哎哎？！？！？！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_357F',
    )

    ChrTalk(
        0x0107,
        (
            '#0070470656V#064F什、什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_357F(): pass

    label('loc_357F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_35AE',
    )

    ChrTalk(
        0x0105,
        (
            '#0060211163V#044F这……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_35AE(): pass

    label('loc_35AE')

    ChrTalk(
        0x0103,
        (
            '#0030470658V#023F他、他刚才、说的是爱娜？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3620',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470659V#052F……啊啊～我听到的确实是那样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3620(): pass

    label('loc_3620')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3661',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470660V#073F嗯，他说的确实是『爱娜』啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3661(): pass

    label('loc_3661')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_36A1',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470661V#032F嗯嗯……\n',
            '这真是出乎意料啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_36A1(): pass

    label('loc_36A1')

    ChrTurnDirection(0x0011, 0x0101, 400)

    ChrTalk(
        0x0011,
        (
            '#3600470662V啊，就是游击士协会的\n',
            '那位美丽的女子！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3600470663V虽然听说过她是酒豪，\n',
            '但这次我有备而去就不怕了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3600470664V只要服下这副药，\n',
            '我就可以堂堂正正地约她出来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470665V#1020F#1P原来你是为了邀约爱娜姐\n',
            '才想要这个药的吗……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470666V#1007F虽然胆量和精神值得佩服，\n',
            '不过、实在太可怜了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3887',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470667V#032F不过，仔细想一想的话，\n',
            '这也是个千载难逢的好机会呀。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470668V如果错失了这个机会，\n',
            '想把爱娜灌醉就是不可能的了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3887(): pass

    label('loc_3887')

    ChrTalk(
        0x0103,
        (
            '#0030470669V#021F呵呵～还真是个有趣的计划啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470670V爱娜酊酩大醉的样子，\n',
            '我也很想看一次呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3600470671V噢噢！这样说的话，\n',
            '难道你们愿意帮我吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3600470672V其实我也很想让大家帮我把她\n',
            '从协会里约出来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3A44',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470673V#035F呵呵，那么\n',
            '我就来助你一臂之力吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040470674V#030F……约见地点就定在\n',
            '那间酒馆如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030470675V#020F嗯，在那里就好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470676V只要提出拼酒的话，\n',
            '爱娜一定会出来应战的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3AAF')

    def _loc_3A44(): pass

    label('loc_3A44')

    ChrTalk(
        0x0103,
        (
            '#0030470677V#020F好！那你们就先去\n',
            '酒馆等着吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470676V只要提出拼酒的话，\n',
            '爱娜一定会出来应战的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3AAF(): pass

    label('loc_3AAF')

    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010470679V#1020F#1P等、等一下啊雪拉姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030470680V#525F哈哈～没事啦。\n',
            '顺水推舟也未尝不可，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470681V既然是委托人的愿望，\n',
            '我们自然应该全力帮忙嘛㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470682V#1015F#1P话是这么说……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470683V#1007F（但其实就是\n',
            '　你自己也想喝酒吧……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3600470684V喔喔！不愧是游击士啊！\n',
            '连服务都这么到位。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#3600470685V那我就去酒馆里等了，\n',
            '把爱娜小姐约出来的事就拜托啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3C86',
    )

    ChrTalk(
        0x0104,
        (
            '#0040470686V#031F喔喔～～那我们就快走吧，老兄！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3C86(): pass

    label('loc_3C86')

    @scena.Lambda('lambda_3C8C')
    def lambda_3C8C():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_3C8C')

    DispatchAsync2(0x00F8, 0x0003, lambda_3C8C)

    @scena.Lambda('lambda_3C9D')
    def lambda_3C9D():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_3C9D')

    DispatchAsync2(0x00F9, 0x0003, lambda_3C9D)

    @scena.Lambda('lambda_3CAE')
    def lambda_3CAE():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_3CAE')

    DispatchAsync2(0x0008, 0x0003, lambda_3CAE)

    @scena.Lambda('lambda_3CBF')
    def lambda_3CBF():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_3CBF')

    DispatchAsync2(0x0101, 0x0003, lambda_3CBF)

    @scena.Lambda('lambda_3CD0')
    def lambda_3CD0():
        ChrWalkTo(0x00FE, -15680, 0, 45490, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0103, 0x0000, lambda_3CD0)

    CreateThread(0x0011, 0x00, 0x01, 0x0008)
    WaitForThreadExit(0x0103, 0x0000)
    TerminateThread(0x0101, 0x03)

    @scena.Lambda('lambda_3CFB')
    def lambda_3CFB():
        CameraMove(-14180, 0, 46960, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_3CFB)

    @scena.Lambda('lambda_3D13')
    def lambda_3D13():
        ChrTurnDirection(0x00FE, 0x0011, 400)
        Yield()

        Jump('lambda_3D13')

    DispatchAsync2(0x0103, 0x0003, lambda_3D13)

    WaitForThreadExit(0x0011, 0x0000)
    TerminateThread(0x0103, 0x03)
    TerminateThread(0x00F8, 0x03)
    TerminateThread(0x00F9, 0x03)
    TerminateThread(0x0008, 0x03)
    ChrSetFlags(0x0011, 0x0080)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3D71',
    )

    OP_62(0x0104, 0x00000000, 2000, 0x08, 0x09, 0x000000FA, 0x02)
    PlaySE(15, 0x00, 0x64)
    CreateThread(0x0104, 0x00, 0x01, 0x0009)
    WaitForThreadExit(0x0104, 0x0000)
    ChrSetFlags(0x0104, 0x0080)

    Jump('loc_3D76')

    def _loc_3D71(): pass

    label('loc_3D71')

    Sleep(1000)

    def _loc_3D76(): pass

    label('loc_3D76')

    CameraMove(-17110, 0, 44470, 2000)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3DBD',
    )

    ChrTalk(
        0x0107,
        (
            '#0070470687V#561F走、走了呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E62')

    def _loc_3DBD(): pass

    label('loc_3DBD')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3DF7',
    )

    ChrTalk(
        0x0105,
        (
            '#0060470688V#045F他、他们走了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E62')

    def _loc_3DF7(): pass

    label('loc_3DF7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3E31',
    )

    ChrTalk(
        0x0108,
        (
            '#0080470689V#075F呼，这就走了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3E62')

    def _loc_3E31(): pass

    label('loc_3E31')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3E62',
    )

    ChrTalk(
        0x0106,
        (
            '#0050470690V#552F这就走了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3E62(): pass

    label('loc_3E62')

    ChrTalk(
        0x0008,
        (
            '#1080470691V哎呀呀，还真是急性子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#1080470692V我还没把药的使用说明\n',
            '讲完啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010470693V#1015F#1P嗯、嗯……\n',
            '不过也没关系啦，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010470694V如果是爱娜姐的话，\n',
            '应该不会这么简单\n',
            '就被约出来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0103, 180, 400)

    ChrTalk(
        0x0103,
        (
            '#0030470695V#021F呵呵～你太小看姐姐了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470696V算啦，要是有兴趣的话，\n',
            '就去酒馆里等着吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030470697V我随后就会把爱娜\n',
            '给拉来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    NewScene('ED6_DT21/T0131._SN', 101, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0x3FD9
@scena.Code('func_08_3FD9')
def func_08_3FD9():
    ChrWalkTo(0x00FE, -13930, 0, 46920, 3000, 0x00)
    ChrWalkTo(0x00FE, -12800, 0, 46920, 3000, 0x00)

    @scena.Lambda('lambda_4007')
    def lambda_4007():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_4007)

    ChrWalkTo(0x00FE, -11420, 0, 46920, 3000, 0x00)

    Return()

# id: 0x0009 offset: 0x4028
@scena.Code('func_09_4028')
def func_09_4028():
    ChrSetFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -12800, 0, 46920, 5000, 0x00)

    @scena.Lambda('lambda_4047')
    def lambda_4047():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 400)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_4047)

    ChrWalkTo(0x00FE, -11420, 0, 46920, 5000, 0x00)
    ChrClearFlags(0x00FE, 0x0040)
    OP_63(0x0104)

    Return()

# id: 0x000A offset: 0x4070
@scena.Code('func_0A_4070')
def func_0A_4070():
    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 52230, 5000, 51080, 0)
    ChrSetPos(0x0103, 51500, 5000, 50530, 0)
    ChrSetPos(0x00F8, 52220, 5000, 49650, 0)
    ChrSetPos(0x00F9, 52230, 5000, 48630, 0)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_40EA',
    )

    ChrSetPos(0x00F9, 52220, 5000, 49650, 0)
    ChrSetPos(0x00F8, 52230, 5000, 48630, 0)

    def _loc_40EA(): pass

    label('loc_40EA')

    CameraMove(51850, 5000, 50700, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010471127V#1002F这把椅子……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471128V正好放在礼拜堂\n',
            '的这个位置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_41D8',
    )

    ChrTalk(
        0x0105,
        (
            '#0060471129V#042F『坐在女神旁边的人』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060471130V也许…\n',
            '就是指这个吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4307')

    def _loc_41D8(): pass

    label('loc_41D8')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_423D',
    )

    ChrTalk(
        0x0104,
        (
            '#0040471131V#032F『坐在女神旁边的人』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040471132V说不定…\n',
            '就是指这个吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4307')

    def _loc_423D(): pass

    label('loc_423D')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_42A7',
    )

    ChrTalk(
        0x0106,
        (
            '#0050471133V#053F『坐在女神旁边的人』吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050471134V#050F有可能\n',
            '说的就是它吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4307')

    def _loc_42A7(): pass

    label('loc_42A7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_4307',
    )

    ChrTalk(
        0x0108,
        (
            '#0080471135V#072F『坐在女神旁边的人』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080471136V也许…\n',
            '指的就是它吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4307(): pass

    label('loc_4307')

    ChrTalk(
        0x0101,
        (
            '#0010471137V#1002F嗯……调查看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_94(0x01, 0x0101, 0x0000, 0x000000C8, 0x000003E8, 0x00)
    Fade(250)
    ChrSetChipByIndex(0x0101, 10)
    ChrSetSubChip(0x0101, 0)
    OP_0D()
    Sleep(500)

    Sleep(1000)

    OP_62(0x0101, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010471138V#1002F果然……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471139V有张卡片。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(250)
    ChrSetChipByIndex(0x0101, 65535)
    OP_0D()
    Sleep(500)

    ChrSetDirection(0x0101, 180, 400)
    Fade(1000)
    ChrSetChipByIndex(0x0101, 32)
    OP_0D()
    Sleep(1000)

    FadeOut(300, 0, 100)
    OP_AD('ED6_DT24/C_VIS124._CH', 0x00BE, 0x0064, 0x000001F4)
    Sleep(1000)

    SetMessageWindowPos(-1, 300, -1, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '#0170471140V 第二个试炼是魔方阵，\n',
            ' 　　　　 ■■　　　　　 \n',
            ' 　　　  ■■■ 　　　　 ',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0170471141V  ■是森林中的东西。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    OP_AE(0x000001F4)
    Sleep(1000)

    Fade(1000)
    ChrSetChipByIndex(0x0101, 65535)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010471142V#1001F很好！猜对了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010471143V#1007F嗯……虽然解开了谜题\n',
            '值得高兴，可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030471144V#025F……这次的暗示好像\n',
            '和之前的完全不同啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030471145V到底是什么意思呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_45A4',
    )

    ChrTalk(
        0x0107,
        (
            '#0070471146V#063F嗯……难道是表示\n',
            '某个场所吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_466A')

    def _loc_45A4(): pass

    label('loc_45A4')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_45E7',
    )

    ChrTalk(
        0x0105,
        (
            '#0060471147V#042F这个也是代表\n',
            '某个地方吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_466A')

    def _loc_45E7(): pass

    label('loc_45E7')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_462C',
    )

    ChrTalk(
        0x0104,
        (
            '#0040471148V#032F这应该也是代表\n',
            '某一个场所吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_466A')

    def _loc_462C(): pass

    label('loc_462C')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_466A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050471149V#050F这应该也是指\n',
            '某个地方吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_466A(): pass

    label('loc_466A')

    ChrTalk(
        0x0101,
        (
            '#0010471150V#1015F根据以往的经验，\n',
            '应该没错吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030471151V#020F嗯～应该就是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030471152V在城里好好调查一下吧，找找\n',
            '有什么东西和暗示上的图形相似。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0077, 0x01, 0x0008)
    OP_28(0x0077, 0x01, 0x0010)
    OP_64(0x01, 0x0001)
    EventEnd(0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
