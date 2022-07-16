import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4301_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4301   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '凯诺娜上尉'),
    TXT(0x02, '拉赛尔博士'),
    TXT(0x03, '基库'),
    TXT(0x04, '机器'),
    TXT(0x05, '机器'),
    TXT(0x06, '雪拉扎德'),
    TXT(0x07, '奥利维尔'),
    TXT(0x08, '科洛丝'),
    TXT(0x09, '阿加特'),
    TXT(0x0A, '提妲'),
    TXT(0x0B, '金'),
    TXT(0x0C, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'C4301.x'
    header.mapIndex       = 216
    header.bgm            = 35
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x2EDB
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
        ('ED6_DT07/CH00280._CH', 'ED6_DT07/CH00280P._CP'),
        ('ED6_DT09/CH10990._CH', 'ED6_DT09/CH10990P._CP'),
        ('ED6_DT07/CH02020._CH', 'ED6_DT07/CH02020P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00120._CH', 'ED6_DT07/CH00120P._CP'),
        ('ED6_DT07/CH00121._CH', 'ED6_DT07/CH00121P._CP'),
        ('ED6_DT07/CH00130._CH', 'ED6_DT07/CH00130P._CP'),
        ('ED6_DT07/CH00131._CH', 'ED6_DT07/CH00131P._CP'),
        ('ED6_DT07/CH00140._CH', 'ED6_DT07/CH00140P._CP'),
        ('ED6_DT07/CH00141._CH', 'ED6_DT07/CH00141P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
        ('ED6_DT09/CH10991._CH', 'ED6_DT09/CH10991P._CP'),
        ('ED6_DT06/CH20040._CH', 'ED6_DT06/CH20040P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT06/CH20053._CH', 'ED6_DT06/CH20053P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00070._CH', 'ED6_DT07/CH00070P._CP'),
    ]

# id: 0x10002 offset: 0x18A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 22,
            chipIndex           = 22,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 24,
            chipIndex           = 24,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 25,
            chipIndex           = 25,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 26,
            chipIndex           = 26,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 27,
            chipIndex           = 27,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
    )

# id: 0x10003 offset: 0x2EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x2EA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 46000,
            y           = -1000,
            z           = -10460,
            range       = 49420,
            dword_10    = 0x000003E8,
            dword_14    = 0xFFFFB884,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000C,
        ),
    )

# id: 0x10005 offset: 0x30A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 62990,
            triggerZ            = 0,
            triggerY            = -2920,
            triggerRange        = 1000,
            actorX              = 62990,
            actorZ              = 1200,
            actorY              = -2920,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x32E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_345',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x5C),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x000F)

    def _loc_345(): pass

    label('loc_345')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 0, 0x668)),
            Expr.Return,
        ),
        'loc_350',
    )

    Call(0, 0x000E)

    def _loc_350(): pass

    label('loc_350')

    ExecExpressionWithValue(
        0x000A,
        0x28,
        (
            (Expr.PushLong, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Or,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0001 offset: 0x362
@scena.Code('Init')
def Init():
    LoadEffect(0x05, 'map\\\\mp027_00.eff')
    PlayEffect(0x05, 0x06, 0x00FF, 62990, 1200, -2920, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x0002 offset: 0x3AC
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3C1',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_3C1(): pass

    label('loc_3C1')

    Return()

# id: 0x0003 offset: 0x3C2
@scena.Code('func_03_3C2')
def func_03_3C2():
    TalkBegin(0x000D)

    ChrTalk(
        0x000D,
        (
            '#0030140139V#020F艾丝蒂尔，\n',
            '不要太过蛮干哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030140140V前面的路还长，切忌焦躁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000D)

    Return()

# id: 0x0004 offset: 0x417
@scena.Code('func_04_417')
def func_04_417():
    TalkBegin(0x000E)

    ChrTalk(
        0x000E,
        (
            '#0040140136V#030F王城的地下还有\n',
            '如此巨大的上古遗迹啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040140137V呵呵，这真是一个\n',
            '让我的灵感爆发的时刻啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040140138V不过还要再等等，\n',
            '因为那些军人和机械魔兽\n',
            '让人有些扫兴。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000E)

    Return()

# id: 0x0005 offset: 0x4C8
@scena.Code('func_05_4C8')
def func_05_4C8():
    TalkBegin(0x000F)

    ChrTalk(
        0x000F,
        (
            '#0060140134V#042F『辉之环』……\n',
            '既然被封印在这里，\n',
            '就肯定有什么原因。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060140135V理查德上校究竟\n',
            '知道了些什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000F)

    Return()

# id: 0x0006 offset: 0x53D
@scena.Code('func_06_53D')
def func_06_53D():
    TalkBegin(0x0010)

    ChrTalk(
        0x0010,
        (
            '#0050140132V#050F往下走了那么久，\n',
            '竟然只赶了一半的路。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050140133V真是的……\n',
            '#057F到最后也要这么麻烦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0010)

    Return()

# id: 0x0007 offset: 0x5A8
@scena.Code('func_07_5A8')
def func_07_5A8():
    TalkBegin(0x0011)

    ChrTalk(
        0x0011,
        (
            '#0070140130V#062F那些魔兽难道也是\n',
            '用导力来驱动的吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070140131V这么说来的话，\n',
            '这个遗迹果然是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0011)

    Return()

# id: 0x0008 offset: 0x60E
@scena.Code('func_08_60E')
def func_08_60E():
    TalkBegin(0x0012)

    ChrTalk(
        0x0012,
        (
            '#0080140128V#070F这里的魔兽\n',
            '很有挑战性。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080140129V我已经跃跃欲试了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0012)

    Return()

# id: 0x0009 offset: 0x659
@scena.Code('func_09_659')
def func_09_659():
    TalkBegin(0x0009)
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
        1,
        (
            TXT(0x00, '对话\n'),
            TXT(0x01, '改造·换钱\n'),
            TXT(0x02, '购买道具\n'),
            TXT(0x03, '更换队员\n'),
            TXT(0x04, '取消\n'),
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
    FadeIn(300, 0)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6CE',
    )

    Call(0, 0x000A)
    OP_56(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_6CE(): pass

    label('loc_6CE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_6E5',
    )

    Call(0, 0x000B)
    OP_56(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_6E5(): pass

    label('loc_6E5')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_736',
    )

    EventBegin(0x00)
    OP_4A(0x0009, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x000E, 255)
    OP_4A(0x000F, 255)
    OP_4A(0x0010, 255)
    OP_4A(0x0011, 255)
    OP_4A(0x0012, 255)
    Call(0, 0x000D)
    OP_4B(0x0009, 255)
    OP_4B(0x000D, 255)
    OP_4B(0x000E, 255)
    OP_4B(0x000F, 255)
    OP_4B(0x0010, 255)
    OP_4B(0x0011, 255)
    OP_4B(0x0012, 255)
    EventEnd(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_736(): pass

    label('loc_736')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_747',
    )

    TalkEnd(0x0009)

    Return()

    def _loc_747(): pass

    label('loc_747')

    ChrTalk(
        0x0009,
        (
            '#0540140126V#104F一定要坚持下去啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540140123V#102F随时可能会和上校开战，\n',
            '做好万全的准备再前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0009)

    Return()

# id: 0x000A offset: 0x7AC
@scena.Code('func_0A_7AC')
def func_0A_7AC():
    ChrTalk(
        0x0009,
        (
            '#0540140055V#100F来吧，我会给你们\n',
            '比这边的工房更好的服务。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_0D()
    OP_A9(0x6A)

    Return()

# id: 0x000B offset: 0x7EB
@scena.Code('func_0B_7EB')
def func_0B_7EB():
    ChrTalk(
        0x0009,
        (
            '#0540140054V#100F有什么需要的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_0D()
    OP_A9(0x6B)

    Return()

# id: 0x000C offset: 0x811
@scena.Code('func_0C_811')
def func_0C_811():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 0, 0x668)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 7, 0x667)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_81E',
    )

    Return()

    def _loc_81E(): pass

    label('loc_81E')

    SetScenaFlags(ScenaFlag(0x00CD, 0, 0x668))
    EventBegin(0x00)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrFlags(0x000B, 0x0004)
    SetChrFlags(0x000C, 0x0004)
    ChrSetRGBAMask(0x000B, 255, 0, 0, 0, 0)
    ChrSetRGBAMask(0x000C, 255, 0, 0, 0, 0)
    SetChrPos(0x0008, 61000, 0, -13970, 270)
    SetChrPos(0x000B, 59250, 6000, -11650, 270)
    SetChrPos(0x000C, 59250, 6000, -16329, 270)

    NpcTalk(
        0x0008,
        '女人的声音',
        (
            '#0610140070V你们这些捣乱分子，\n',
            '果然还是不自量力地追来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0001, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0002, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0003, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_0933')
    def lambda_0933():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0933)

    @scena.Lambda('lambda_0941')
    def lambda_0941():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0941)

    @scena.Lambda('lambda_094F')
    def lambda_094F():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_094F)

    @scena.Lambda('lambda_095D')
    def lambda_095D():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_095D)

    @scena.Lambda('lambda_096B')
    def lambda_096B():
        OP_67(0, 8170, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_096B)

    @scena.Lambda('lambda_0983')
    def lambda_0983():
        OP_6C(37000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0983)

    CameraMove(57560, 0, -13380, 2000)
    SetChrChipByIndex(0x0101, 4)
    SetChrChipByIndex(0x0102, 6)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9BB',
    )

    SetChrChipByIndex(0x0103, 8)

    def _loc_9BB(): pass

    label('loc_9BB')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9CE',
    )

    SetChrChipByIndex(0x0104, 10)

    def _loc_9CE(): pass

    label('loc_9CE')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9E1',
    )

    SetChrChipByIndex(0x0106, 14)

    def _loc_9E1(): pass

    label('loc_9E1')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9F4',
    )

    SetChrChipByIndex(0x0105, 12)

    def _loc_9F4(): pass

    label('loc_9F4')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A07',
    )

    SetChrChipByIndex(0x0107, 16)

    def _loc_A07(): pass

    label('loc_A07')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A1A',
    )

    SetChrChipByIndex(0x0108, 18)

    def _loc_A1A(): pass

    label('loc_A1A')

    SetChrPos(0x0000, 45670, 0, -14030, 90)
    SetChrPos(0x0001, 45670, 0, -14030, 90)
    SetChrPos(0x0002, 45670, 0, -14030, 90)
    SetChrPos(0x0003, 45670, 0, -14030, 90)

    @scena.Lambda('lambda_0A64')
    def lambda_0A64():
        ChrWalkTo(0x00FE, 53520, 0, -13400, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0A64)

    Sleep(500)

    @scena.Lambda('lambda_0A84')
    def lambda_0A84():
        ChrWalkTo(0x00FE, 53520, 0, -14710, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_0A84)

    Sleep(500)

    ClearScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_AFE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_AE0',
    )

    Sleep(500)

    @scena.Lambda('lambda_0AC8')
    def lambda_0AC8():
        ChrWalkTo(0x00FE, 52890, 0, -16059, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0AC8)

    Jump('loc_AFB')

    def _loc_AE0(): pass

    label('loc_AE0')

    @scena.Lambda('lambda_0AE6')
    def lambda_0AE6():
        ChrWalkTo(0x00FE, 52860, 0, -12160, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0AE6)

    def _loc_AFB(): pass

    label('loc_AFB')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_AFE(): pass

    label('loc_AFE')

    If(
        (
            (Expr.PushValueByIndex, 0xB),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xB),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_B5B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_B3D',
    )

    Sleep(500)

    @scena.Lambda('lambda_0B25')
    def lambda_0B25():
        ChrWalkTo(0x00FE, 52890, 0, -16059, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_0B25)

    Jump('loc_B58')

    def _loc_B3D(): pass

    label('loc_B3D')

    @scena.Lambda('lambda_0B43')
    def lambda_0B43():
        ChrWalkTo(0x00FE, 52860, 0, -12160, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_0B43)

    def _loc_B58(): pass

    label('loc_B58')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_B5B(): pass

    label('loc_B5B')

    If(
        (
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_BB8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_B9A',
    )

    Sleep(500)

    @scena.Lambda('lambda_0B82')
    def lambda_0B82():
        ChrWalkTo(0x00FE, 52890, 0, -16059, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0000, lambda_0B82)

    Jump('loc_BB5')

    def _loc_B9A(): pass

    label('loc_B9A')

    @scena.Lambda('lambda_0BA0')
    def lambda_0BA0():
        ChrWalkTo(0x00FE, 52860, 0, -12160, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0000, lambda_0BA0)

    def _loc_BB5(): pass

    label('loc_BB5')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_BB8(): pass

    label('loc_BB8')

    If(
        (
            (Expr.PushValueByIndex, 0xD),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xD),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_C15',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_BF7',
    )

    Sleep(500)

    @scena.Lambda('lambda_0BDF')
    def lambda_0BDF():
        ChrWalkTo(0x00FE, 52890, 0, -16059, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0000, lambda_0BDF)

    Jump('loc_C12')

    def _loc_BF7(): pass

    label('loc_BF7')

    @scena.Lambda('lambda_0BFD')
    def lambda_0BFD():
        ChrWalkTo(0x00FE, 52860, 0, -12160, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0000, lambda_0BFD)

    def _loc_C12(): pass

    label('loc_C12')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_C15(): pass

    label('loc_C15')

    WaitForThreadExit(0x0000, 0x0000)
    SetChrDirection(0x0000, 90, 0)
    WaitForThreadExit(0x0001, 0x0000)
    SetChrDirection(0x0001, 90, 0)
    WaitForThreadExit(0x0002, 0x0000)
    SetChrDirection(0x0002, 90, 0)
    WaitForThreadExit(0x0003, 0x0000)
    SetChrDirection(0x0003, 90, 0)

    ChrTalk(
        0x0102,
        (
            '#0020121481V#012F凯诺娜上尉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010140072V#004F怎、怎么她还会出现在这里！？\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140073V不是已经在空中庭园被打昏了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610140074V#180F哼，你们太小看我了。\n',
            '我才不会被那种程度的攻击所打倒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610140075V#181F虽然我已经拼尽全力守护，\n',
            '格兰赛尔城最后还是被夺走了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610140076V#188F不过，只要上校得到了『辉之环』，\n',
            '必定可以随时将王城夺回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E22',
    )

    ChrTalk(
        0x0103,
        (
            '#0030140077V#025F#5P该怎么说好呢……\n',
            '真是不知悔改的性格啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030140078V#027F与其说是母狐狸，\n',
            '倒不如说她是蛇更加贴切呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_106E')

    def _loc_E22(): pass

    label('loc_E22')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_E96',
    )

    ChrTalk(
        0x0104,
        (
            '#0040140079V#035F#5P哼，被逼到走投无路的人\n',
            '还沉醉在泡沫般的美梦里……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040140080V#030F真是可悲啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_106E')

    def _loc_E96(): pass

    label('loc_E96')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F04',
    )

    ChrTalk(
        0x0106,
        (
            '#0050140081V#053F#5P母狐狸……\n',
            '这绰号的确和你很相配……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050140082V#057F做你的千秋大梦去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_106E')

    def _loc_F04(): pass

    label('loc_F04')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F6D',
    )

    ChrTalk(
        0x0107,
        (
            '#0070140083V#065F#5P做、做这样的事情，\n',
            '到底是为了什么啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070140084V我……实在不明白。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    Jump('loc_106E')

    def _loc_F6D(): pass

    label('loc_F6D')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_FE5',
    )

    ChrTalk(
        0x0108,
        (
            '#0080140085V#075F#5P哎呀哎呀，我说。\n',
            '你这女人也太过嚣张了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080140086V#070F真是和你的美貌不相配呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    Jump('loc_106E')

    def _loc_FE5(): pass

    label('loc_FE5')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_106E',
    )

    ChrTalk(
        0x0105,
        (
            '#0060140087V#043F#5P『辉之环』……\n',
            '真的是人类可以控制住的东西吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060140088V况且我们还不知道\n',
            '为什么它会被封印在这里啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    def _loc_106E(): pass

    label('loc_106E')

    ChrTalk(
        0x0008,
        (
            '#0610140089V#186F可恶，给我闭嘴！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610140090V我是绝对不会让你们去干扰上校的！\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610140091V#185F出来吧，人形机器！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_10E2')
    def lambda_10E2():
        ChrJumpTo(0x00FE, 59250, 0, -11650, 1000, 5000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_10E2)

    ChrSetRGBAMask(0x000B, 100, 100, 255, 255, 100)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 255, 100)
    WaitForThreadExit(0x000B, 0x0001)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 500, 3000, 100)

    @scena.Lambda('lambda_1131')
    def lambda_1131():
        OP_99(0x00FE, 0x00, 0x07, 2000)
        Yield()

        Jump('lambda_1131')

    DispatchAsync2(0x000B, 0x0001, lambda_1131)

    @scena.Lambda('lambda_1144')
    def lambda_1144():
        ChrJumpTo(0x00FE, 59250, 0, -16329, 1000, 5000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1144)

    ChrSetRGBAMask(0x000C, 100, 100, 255, 255, 100)
    ChrSetRGBAMask(0x000C, 255, 255, 255, 255, 100)
    WaitForThreadExit(0x000C, 0x0001)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 500, 3000, 100)

    @scena.Lambda('lambda_1193')
    def lambda_1193():
        OP_99(0x00FE, 0x00, 0x07, 2000)
        Yield()

        Jump('lambda_1193')

    DispatchAsync2(0x000C, 0x0001, lambda_1193)

    ChrTalk(
        0x0101,
        (
            '#0010140092V#580F哇啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140093V#012F可以操纵古代的机械……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610140094V#188F哼哼，见识到我们的实力，\n',
            '你们已经感到气馁了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610140095V在对这里展开调查之前\n',
            '我们就已经收集了足够的资料。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610140096V通过那些资料来看，\n',
            '操纵这些强大的人形兵器也并非不可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_12E9',
    )

    ChrTalk(
        0x0103,
        (
            '#0030140097V#025F#5P呼……\n',
            '我就讨厌这种固执的女人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_144D')

    def _loc_12E9(): pass

    label('loc_12E9')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1331',
    )

    ChrTalk(
        0x0104,
        (
            '#0040140098V#035F#5P呵……\n',
            '真是可歌可泣的努力啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_144D')

    def _loc_1331(): pass

    label('loc_1331')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1370',
    )

    ChrTalk(
        0x0106,
        (
            '#0050140099V#057F#5P嘁……不要开玩笑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_144D')

    def _loc_1370(): pass

    label('loc_1370')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_13D2',
    )

    ChrTalk(
        0x0107,
        (
            '#0070140100V#063F#5P既、既然存在这样的技术，\n',
            '就应该将它用于正途才合适啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_144D')

    def _loc_13D2(): pass

    label('loc_13D2')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1413',
    )

    ChrTalk(
        0x0108,
        (
            '#0080140101V#075F#5P喂喂，你不要命了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_144D')

    def _loc_1413(): pass

    label('loc_1413')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_144D',
    )

    ChrTalk(
        0x0105,
        (
            '#0060140102V#043F#5P这、这太危险了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_144D(): pass

    label('loc_144D')

    ChrTalk(
        0x0008,
        (
            '#0610140103V#183F哼，什么也不用说了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610140104V#185F准备……开始进攻！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1499')
    def lambda_1499():
        OP_92(0x00FE, 0x0008, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_1499)

    Sleep(10)

    @scena.Lambda('lambda_14B3')
    def lambda_14B3():
        OP_92(0x00FE, 0x0008, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_14B3)

    Sleep(10)

    ClearScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_151B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1503',
    )

    Sleep(10)

    @scena.Lambda('lambda_14F1')
    def lambda_14F1():
        OP_92(0x00FE, 0x000C, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_14F1)

    Jump('loc_1518')

    def _loc_1503(): pass

    label('loc_1503')

    @scena.Lambda('lambda_1509')
    def lambda_1509():
        OP_92(0x00FE, 0x000B, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_1509)

    def _loc_1518(): pass

    label('loc_1518')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_151B(): pass

    label('loc_151B')

    If(
        (
            (Expr.PushValueByIndex, 0xB),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xB),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_156C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1554',
    )

    Sleep(10)

    @scena.Lambda('lambda_1542')
    def lambda_1542():
        OP_92(0x00FE, 0x000C, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_1542)

    Jump('loc_1569')

    def _loc_1554(): pass

    label('loc_1554')

    @scena.Lambda('lambda_155A')
    def lambda_155A():
        OP_92(0x00FE, 0x000B, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_155A)

    def _loc_1569(): pass

    label('loc_1569')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_156C(): pass

    label('loc_156C')

    If(
        (
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_15BD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_15A5',
    )

    Sleep(10)

    @scena.Lambda('lambda_1593')
    def lambda_1593():
        OP_92(0x00FE, 0x000C, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0000, lambda_1593)

    Jump('loc_15BA')

    def _loc_15A5(): pass

    label('loc_15A5')

    @scena.Lambda('lambda_15AB')
    def lambda_15AB():
        OP_92(0x00FE, 0x000B, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0000, lambda_15AB)

    def _loc_15BA(): pass

    label('loc_15BA')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_15BD(): pass

    label('loc_15BD')

    If(
        (
            (Expr.PushValueByIndex, 0xD),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xD),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_160E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_15F6',
    )

    Sleep(10)

    @scena.Lambda('lambda_15E4')
    def lambda_15E4():
        OP_92(0x00FE, 0x000C, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0000, lambda_15E4)

    Jump('loc_160B')

    def _loc_15F6(): pass

    label('loc_15F6')

    @scena.Lambda('lambda_15FC')
    def lambda_15FC():
        OP_92(0x00FE, 0x000B, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0000, lambda_15FC)

    def _loc_160B(): pass

    label('loc_160B')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_160E(): pass

    label('loc_160E')

    Sleep(50)

    ExecExpressionWithValue(
        0x000B,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x000B, 20)

    @scena.Lambda('lambda_1629')
    def lambda_1629():
        ChrWalkTo(0x00FE, 52250, 0, -11650, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1629)

    Sleep(10)

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x000C, 20)

    @scena.Lambda('lambda_1659')
    def lambda_1659():
        ChrWalkTo(0x00FE, 52250, 0, -16329, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1659)

    Sleep(10)

    @scena.Lambda('lambda_1679')
    def lambda_1679():
        OP_92(0x00FE, 0x0000, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1679)

    Sleep(200)

    TerminateThread(0x0000, 0xFF)
    TerminateThread(0x0001, 0xFF)
    TerminateThread(0x0002, 0xFF)
    TerminateThread(0x0003, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)
    Battle(0x0000039B, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_16C2'),
        (-1, 'loc_16C5'),
    )

    def _loc_16C2(): pass

    label('loc_16C2')

    OP_B4(0x00)

    Return()

    def _loc_16C5(): pass

    label('loc_16C5')

    EventBegin(0x00)
    SetChrPos(0x0101, 57050, 0, -12660, 132)
    SetChrPos(0x0102, 56160, 0, -14450, 88)
    ClearScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1730',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_171C',
    )

    SetChrPos(0x0000, 57840, 0, -15280, 27)

    Jump('loc_172D')

    def _loc_171C(): pass

    label('loc_171C')

    SetChrPos(0x0000, 56200, 0, -11470, 112)

    def _loc_172D(): pass

    label('loc_172D')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_1730(): pass

    label('loc_1730')

    If(
        (
            (Expr.PushValueByIndex, 0xB),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xB),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1774',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1760',
    )

    SetChrPos(0x0001, 57840, 0, -15280, 27)

    Jump('loc_1771')

    def _loc_1760(): pass

    label('loc_1760')

    SetChrPos(0x0001, 56200, 0, -11470, 112)

    def _loc_1771(): pass

    label('loc_1771')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_1774(): pass

    label('loc_1774')

    If(
        (
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_17B8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_17A4',
    )

    SetChrPos(0x0002, 57840, 0, -15280, 27)

    Jump('loc_17B5')

    def _loc_17A4(): pass

    label('loc_17A4')

    SetChrPos(0x0002, 56200, 0, -11470, 112)

    def _loc_17B5(): pass

    label('loc_17B5')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_17B8(): pass

    label('loc_17B8')

    If(
        (
            (Expr.PushValueByIndex, 0xD),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xD),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_17FC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_17E8',
    )

    SetChrPos(0x0003, 57840, 0, -15280, 27)

    Jump('loc_17F9')

    def _loc_17E8(): pass

    label('loc_17E8')

    SetChrPos(0x0003, 56200, 0, -11470, 112)

    def _loc_17F9(): pass

    label('loc_17F9')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_17FC(): pass

    label('loc_17FC')

    SetChrPos(0x0008, 59690, 0, -13480, 0)
    SetChrChipByIndex(0x0008, 21)
    SetChrSubChip(0x0008, 0)
    ClearChrFlags(0x0008, 0x0001)
    SetChrFlags(0x0008, 0x0800)
    SetChrFlags(0x000B, 0x0080)
    SetChrFlags(0x000C, 0x0080)
    CameraMove(57980, 0, -13040, 0)
    OP_67(0, 9150, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010140105V#007F这、这回总算是完全昏迷了吧……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140106V#010F嗯……\n',
            '短时间内应该不能行动了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140107V多亏了她的出现……\n',
            '从她守卫在这里的举动来判断，\n',
            '通过这条路线应该就能找到上校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1A1E',
    )

    ChrTalk(
        0x0101,
        (
            '#0010140108V#004F的、的确……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060140109V#040F那么，\n',
            '我就叫基库将他们带过来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0000, 65535)
    SetChrChipByIndex(0x0001, 65535)
    SetChrChipByIndex(0x0002, 65535)
    SetChrChipByIndex(0x0003, 65535)
    SetChrDirection(0x0105, 270, 400)

    @scena.Lambda('lambda_19AD')
    def lambda_19AD():
        SetChrDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_19AD)

    @scena.Lambda('lambda_19BB')
    def lambda_19BB():
        SetChrDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_19BB)

    @scena.Lambda('lambda_19C9')
    def lambda_19C9():
        SetChrDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_19C9)

    @scena.Lambda('lambda_19D7')
    def lambda_19D7():
        SetChrDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_19D7)

    Sleep(400)

    ChrTalk(
        0x0105,
        (
            '#0060140110V#040F#2P基库，过来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0440140111V#2P啾～⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B00')

    def _loc_1A1E(): pass

    label('loc_1A1E')

    ChrTalk(
        0x0101,
        (
            '#0010140112V#004F的、的确……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140113V#006F这么说来的话，\n',
            '就可以叫基库将他们带过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0000, 65535)
    SetChrChipByIndex(0x0001, 65535)
    SetChrChipByIndex(0x0002, 65535)
    SetChrChipByIndex(0x0003, 65535)
    SetChrDirection(0x0101, 270, 400)

    @scena.Lambda('lambda_1A96')
    def lambda_1A96():
        SetChrDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1A96)

    @scena.Lambda('lambda_1AA4')
    def lambda_1AA4():
        SetChrDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1AA4)

    @scena.Lambda('lambda_1AB2')
    def lambda_1AB2():
        SetChrDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1AB2)

    @scena.Lambda('lambda_1AC0')
    def lambda_1AC0():
        SetChrDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1AC0)

    Sleep(400)

    ChrTalk(
        0x0101,
        (
            '#0010140114V#508F#2P喂～基库！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0440130849V#2P啾！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B00(): pass

    label('loc_1B00')

    ClearChrFlags(0x000A, 0x0080)
    SetChrFlags(0x000A, 0x0004)
    SetChrPos(0x000A, 37300, 5000, -13990, 0)
    PlaySE(140, 0x00, 0x64)

    @scena.Lambda('lambda_1B26')
    def lambda_1B26():
        CameraMove(52800, 0, -14030, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1B26)

    @scena.Lambda('lambda_1B3E')
    def lambda_1B3E():
        ChrWalkTo(0x00FE, 55480, 1000, -13580, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1B3E)

    Sleep(500)

    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(500)

    SetChrPos(0x0101, 54150, 0, -5010, 45)
    SetChrPos(0x0102, 55010, 0, -6060, 45)
    SetChrFlags(0x000A, 0x0080)
    ClearScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1BD6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1BC2',
    )

    SetChrPos(0x0000, 53820, 0, -7240, 45)

    Jump('loc_1BD3')

    def _loc_1BC2(): pass

    label('loc_1BC2')

    SetChrPos(0x0000, 52900, 0, -6250, 45)

    def _loc_1BD3(): pass

    label('loc_1BD3')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_1BD6(): pass

    label('loc_1BD6')

    If(
        (
            (Expr.PushValueByIndex, 0xB),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xB),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C1A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1C06',
    )

    SetChrPos(0x0001, 53820, 0, -7240, 45)

    Jump('loc_1C17')

    def _loc_1C06(): pass

    label('loc_1C06')

    SetChrPos(0x0001, 52900, 0, -6250, 45)

    def _loc_1C17(): pass

    label('loc_1C17')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_1C1A(): pass

    label('loc_1C1A')

    If(
        (
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xC),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1C5E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1C4A',
    )

    SetChrPos(0x0002, 53820, 0, -7240, 45)

    Jump('loc_1C5B')

    def _loc_1C4A(): pass

    label('loc_1C4A')

    SetChrPos(0x0002, 52900, 0, -6250, 45)

    def _loc_1C5B(): pass

    label('loc_1C5B')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_1C5E(): pass

    label('loc_1C5E')

    If(
        (
            (Expr.PushValueByIndex, 0xD),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            (Expr.PushValueByIndex, 0xD),
            (Expr.PushLong, 0x1),
            Expr.Neq,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1CA2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1C8E',
    )

    SetChrPos(0x0003, 53820, 0, -7240, 45)

    Jump('loc_1C9F')

    def _loc_1C8E(): pass

    label('loc_1C8E')

    SetChrPos(0x0003, 52900, 0, -6250, 45)

    def _loc_1C9F(): pass

    label('loc_1C9F')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_1CA2(): pass

    label('loc_1CA2')

    OP_4A(0x0009, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x000E, 255)
    OP_4A(0x000F, 255)
    OP_4A(0x0010, 255)
    OP_4A(0x0011, 255)
    OP_4A(0x0012, 255)
    Call(0, 0x000E)
    SetChrFlags(0x0008, 0x0800)
    ClearChrFlags(0x0008, 0x0001)
    CameraMove(56230, 0, -3780, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(1500, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0540140116V#102F#5P从刚才检测出的导力反应的程度来看，\n',
            '基本上已经可以确定这个遗迹的规模了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540140117V这个地方应该是在遗迹的中间位置。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140118V#007F呼，只走了一半啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140119V#003F再不快一点的话恐怕上校会……\n',
            '哎呀，总觉得好着急呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140120V#012F可是，如果现在就着急，\n',
            '反而有可能会迷路的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140121V放松一些，认真地走下去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0540140122V#104F#5P唔……\n',
            '一定要坚持下去啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540140123V#102F随时可能会和上校开战，\n',
            '做好充分的准备再前进吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0009, 255)
    OP_4B(0x000D, 255)
    OP_4B(0x000E, 255)
    OP_4B(0x000F, 255)
    OP_4B(0x0010, 255)
    OP_4B(0x0011, 255)
    OP_4B(0x0012, 255)
    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x1EEE
@scena.Code('func_0D_1EEE')
def func_0D_1EEE():
    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1EFF',
    )

    FormationDelMember(0x02, 0xFF)

    def _loc_1EFF(): pass

    label('loc_1EFF')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F10',
    )

    FormationDelMember(0x03, 0xFF)

    def _loc_1F10(): pass

    label('loc_1F10')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F21',
    )

    FormationDelMember(0x05, 0xFF)

    def _loc_1F21(): pass

    label('loc_1F21')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F32',
    )

    FormationDelMember(0x04, 0xFF)

    def _loc_1F32(): pass

    label('loc_1F32')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F43',
    )

    FormationDelMember(0x06, 0xFF)

    def _loc_1F43(): pass

    label('loc_1F43')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1F54',
    )

    FormationDelMember(0x07, 0xFF)

    def _loc_1F54(): pass

    label('loc_1F54')

    Fade(1000)
    SetChrPos(0x0101, 54150, 0, -5010, 45)
    SetChrPos(0x0102, 55010, 0, -6060, 45)
    Call(0, 0x000E)
    CameraMove(56230, 0, -3780, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    FadeOut(300, 0, 100)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0x18),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '请选择除了约修亚和艾丝蒂尔以外的两名成员。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    def _loc_200C(): pass

    label('loc_200C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_25E3',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20A5',
    )

    Menu(
        0,
        10,
        106,
        1,
        (
            TXT(0x00, '★【　雪拉扎德　】\n'),
            TXT(0x01, '　【　奥利维尔　】\n'),
            TXT(0x02, '　【　 阿加特 　】\n'),
            TXT(0x03, '　【　　提妲　　】\n'),
            TXT(0x04, '　【　　 金 　　】\n'),
            TXT(0x05, '　【　 科洛丝 　】\n'),
        ),
    )

    Jump('loc_23DC')

    def _loc_20A5(): pass

    label('loc_20A5')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2131',
    )

    Menu(
        0,
        10,
        106,
        1,
        (
            TXT(0x00, '　【　雪拉扎德　】\n'),
            TXT(0x01, '★【　奥利维尔　】\n'),
            TXT(0x02, '　【　 阿加特 　】\n'),
            TXT(0x03, '　【　　提妲　　】\n'),
            TXT(0x04, '　【　　 金 　　】\n'),
            TXT(0x05, '　【　 科洛丝 　】\n'),
        ),
    )

    Jump('loc_23DC')

    def _loc_2131(): pass

    label('loc_2131')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_21BD',
    )

    Menu(
        0,
        10,
        106,
        1,
        (
            TXT(0x00, '　【　雪拉扎德　】\n'),
            TXT(0x01, '　【　奥利维尔　】\n'),
            TXT(0x02, '★【　 阿加特 　】\n'),
            TXT(0x03, '　【　　提妲　　】\n'),
            TXT(0x04, '　【　　 金 　　】\n'),
            TXT(0x05, '　【　 科洛丝 　】\n'),
        ),
    )

    Jump('loc_23DC')

    def _loc_21BD(): pass

    label('loc_21BD')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2249',
    )

    Menu(
        0,
        10,
        106,
        1,
        (
            TXT(0x00, '　【　雪拉扎德　】\n'),
            TXT(0x01, '　【　奥利维尔　】\n'),
            TXT(0x02, '　【　 阿加特 　】\n'),
            TXT(0x03, '★【　　提妲　　】\n'),
            TXT(0x04, '　【　　 金 　　】\n'),
            TXT(0x05, '　【　 科洛丝 　】\n'),
        ),
    )

    Jump('loc_23DC')

    def _loc_2249(): pass

    label('loc_2249')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_22D5',
    )

    Menu(
        0,
        10,
        106,
        1,
        (
            TXT(0x00, '　【　雪拉扎德　】\n'),
            TXT(0x01, '　【　奥利维尔　】\n'),
            TXT(0x02, '　【　 阿加特 　】\n'),
            TXT(0x03, '　【　　提妲　　】\n'),
            TXT(0x04, '★【　　 金 　　】\n'),
            TXT(0x05, '　【　 科洛丝 　】\n'),
        ),
    )

    Jump('loc_23DC')

    def _loc_22D5(): pass

    label('loc_22D5')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2361',
    )

    Menu(
        0,
        10,
        106,
        1,
        (
            TXT(0x00, '　【　雪拉扎德　】\n'),
            TXT(0x01, '　【　奥利维尔　】\n'),
            TXT(0x02, '　【　 阿加特 　】\n'),
            TXT(0x03, '　【　　提妲　　】\n'),
            TXT(0x04, '　【　　 金 　　】\n'),
            TXT(0x05, '★【　 科洛丝 　】\n'),
        ),
    )

    Jump('loc_23DC')

    def _loc_2361(): pass

    label('loc_2361')

    Menu(
        0,
        10,
        106,
        0,
        (
            TXT(0x00, '　【　雪拉扎德　】\n'),
            TXT(0x01, '　【　奥利维尔　】\n'),
            TXT(0x02, '　【　 阿加特 　】\n'),
            TXT(0x03, '　【　　提妲　　】\n'),
            TXT(0x04, '　【　　 金 　　】\n'),
            TXT(0x05, '　【　 科洛丝 　】\n'),
        ),
    )

    def _loc_23DC(): pass

    label('loc_23DC')

    MenuEnd(0x0000)
    OP_5F(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2403'),
        (0x00000001, 'loc_241D'),
        (0x00000002, 'loc_2437'),
        (0x00000003, 'loc_2451'),
        (0x00000004, 'loc_246B'),
        (0x00000005, 'loc_2485'),
        (-1, 'loc_249F'),
    )

    def _loc_2403(): pass

    label('loc_2403')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2417',
    )

    FormationAddMember(0x02, 0xFF)

    Jump('loc_241A')

    def _loc_2417(): pass

    label('loc_2417')

    FormationDelMember(0x02, 0xFF)

    def _loc_241A(): pass

    label('loc_241A')

    Jump('loc_2517')

    def _loc_241D(): pass

    label('loc_241D')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2431',
    )

    FormationAddMember(0x03, 0xFF)

    Jump('loc_2434')

    def _loc_2431(): pass

    label('loc_2431')

    FormationDelMember(0x03, 0xFF)

    def _loc_2434(): pass

    label('loc_2434')

    Jump('loc_2517')

    def _loc_2437(): pass

    label('loc_2437')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_244B',
    )

    FormationAddMember(0x05, 0xFF)

    Jump('loc_244E')

    def _loc_244B(): pass

    label('loc_244B')

    FormationDelMember(0x05, 0xFF)

    def _loc_244E(): pass

    label('loc_244E')

    Jump('loc_2517')

    def _loc_2451(): pass

    label('loc_2451')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2465',
    )

    FormationAddMember(0x06, 0xFF)

    Jump('loc_2468')

    def _loc_2465(): pass

    label('loc_2465')

    FormationDelMember(0x06, 0xFF)

    def _loc_2468(): pass

    label('loc_2468')

    Jump('loc_2517')

    def _loc_246B(): pass

    label('loc_246B')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_247F',
    )

    FormationAddMember(0x07, 0xFF)

    Jump('loc_2482')

    def _loc_247F(): pass

    label('loc_247F')

    FormationDelMember(0x07, 0xFF)

    def _loc_2482(): pass

    label('loc_2482')

    Jump('loc_2517')

    def _loc_2485(): pass

    label('loc_2485')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2499',
    )

    FormationAddMember(0x04, 0xFF)

    Jump('loc_249C')

    def _loc_2499(): pass

    label('loc_2499')

    FormationDelMember(0x04, 0xFF)

    def _loc_249C(): pass

    label('loc_249C')

    Jump('loc_2517')

    def _loc_249F(): pass

    label('loc_249F')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24B3',
    )

    FormationDelMember(0x02, 0xFF)

    Jump('loc_2514')

    def _loc_24B3(): pass

    label('loc_24B3')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24C7',
    )

    FormationDelMember(0x03, 0xFF)

    Jump('loc_2514')

    def _loc_24C7(): pass

    label('loc_24C7')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24DB',
    )

    FormationDelMember(0x05, 0xFF)

    Jump('loc_2514')

    def _loc_24DB(): pass

    label('loc_24DB')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24EF',
    )

    FormationDelMember(0x04, 0xFF)

    Jump('loc_2514')

    def _loc_24EF(): pass

    label('loc_24EF')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2503',
    )

    FormationDelMember(0x06, 0xFF)

    Jump('loc_2514')

    def _loc_2503(): pass

    label('loc_2503')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2514',
    )

    FormationDelMember(0x07, 0xFF)

    def _loc_2514(): pass

    label('loc_2514')

    Jump('loc_2517')

    def _loc_2517(): pass

    label('loc_2517')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_253A',
    )

    SetChrFlags(0x0003, 0x0080)
    SetChrFlags(0x0002, 0x0080)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_25BE')

    def _loc_253A(): pass

    label('loc_253A')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_257B',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '请选择除了约修亚和艾丝蒂尔以外的两名成员。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_25BE')

    def _loc_257B(): pass

    label('loc_257B')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_25BE',
    )

    SetChrFlags(0x0002, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '请选择除了约修亚和艾丝蒂尔以外的两名成员。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    def _loc_25BE(): pass

    label('loc_25BE')

    SetChrPos(0x0101, 54150, 0, -5010, 45)
    SetChrPos(0x0102, 55010, 0, -6060, 45)

    Jump('loc_200C')

    def _loc_25E3(): pass

    label('loc_25E3')

    OP_5F(0x0000)
    OP_56(0x00)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeIn(300, 0)
    Fade(1000)
    SetChrPos(0x0101, 54150, 0, -5010, 45)
    SetChrPos(0x0102, 55010, 0, -6060, 45)
    ClearChrFlags(0x0002, 0x0080)
    ClearChrFlags(0x0003, 0x0080)
    SetChrPos(0x0002, 54470, 0, -7820, 27)
    SetChrPos(0x0003, 56010, 0, -8590, 27)
    Call(0, 0x000E)
    CameraMove(56230, 0, -3780, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    Return()

# id: 0x000E offset: 0x268F
@scena.Code('func_0E_268F')
def func_0E_268F():
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0009, 55790, 0, -4250, 225)
    SetChrFlags(0x0008, 0x0800)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x0008, 60460, 0, 480, 90)
    SetChrChipByIndex(0x0008, 21)
    ClearChrFlags(0x0008, 0x0001)

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_26F1',
    )

    ClearChrFlags(0x0010, 0x0080)
    SetChrPos(0x0010, 55690, 0, 1000, 180)

    Jump('loc_26F6')

    def _loc_26F1(): pass

    label('loc_26F1')

    SetChrFlags(0x0010, 0x0080)

    def _loc_26F6(): pass

    label('loc_26F6')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_271D',
    )

    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0011, 54740, 0, -1560, 180)

    Jump('loc_2722')

    def _loc_271D(): pass

    label('loc_271D')

    SetChrFlags(0x0011, 0x0080)

    def _loc_2722(): pass

    label('loc_2722')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2749',
    )

    ClearChrFlags(0x000E, 0x0080)
    SetChrPos(0x000E, 57870, 0, -2040, 225)

    Jump('loc_274E')

    def _loc_2749(): pass

    label('loc_2749')

    SetChrFlags(0x000E, 0x0080)

    def _loc_274E(): pass

    label('loc_274E')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2775',
    )

    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000D, 57210, 0, -860, 225)

    Jump('loc_277A')

    def _loc_2775(): pass

    label('loc_2775')

    SetChrFlags(0x000D, 0x0080)

    def _loc_277A(): pass

    label('loc_277A')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_27A1',
    )

    ClearChrFlags(0x0012, 0x0080)
    SetChrPos(0x0012, 59350, 0, -3220, 225)

    Jump('loc_27A6')

    def _loc_27A1(): pass

    label('loc_27A1')

    SetChrFlags(0x0012, 0x0080)

    def _loc_27A6(): pass

    label('loc_27A6')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_27CD',
    )

    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x000F, 56420, 0, -2530, 225)

    Jump('loc_27D2')

    def _loc_27CD(): pass

    label('loc_27CD')

    SetChrFlags(0x000F, 0x0080)

    def _loc_27D2(): pass

    label('loc_27D2')

    Return()

# id: 0x000F offset: 0x27D3
@scena.Code('func_0F_27D3')
def func_0F_27D3():
    EventBegin(0x00)
    OP_4A(0x0009, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x000E, 255)
    OP_4A(0x000F, 255)
    OP_4A(0x0010, 255)
    OP_4A(0x0011, 255)
    OP_4A(0x0012, 255)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)

    @scena.Lambda('lambda_280B')
    def lambda_280B():
        OP_7C(0, 100, 2000, 3000)
        Yield()

        Jump('lambda_280B')

    DispatchAsync2(0x0009, 0x0003, lambda_280B)

    PlaySE(133, 0x01, 0x64)
    LoadEffect(0x01, 'map\\\\mp015_00.eff')
    CreateThread(0x0101, 0x00, 0x00, 0x0010)
    CameraMove(55710, 0, -7780, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(134000, 0)
    OP_6E(513, 0)
    FadeIn(2000, 0)
    Sleep(600)

    OP_77(0xC8, 0xC8, 0xC8, 0x00, 0x00000BB8)

    @scena.Lambda('lambda_289A')
    def lambda_289A():
        CameraMove(-130, 0, -14000, 3500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_289A)

    @scena.Lambda('lambda_28B2')
    def lambda_28B2():
        OP_6C(45000, 5500)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_28B2)

    Sleep(400)

    OP_B0(0x0003, 0x0A)
    OP_B0(0x0004, 0x0A)
    OP_B0(0x0005, 0x0A)
    OP_B0(0x0006, 0x0A)
    OP_B0(0x0007, 0x0A)
    OP_B0(0x0008, 0x0A)
    OP_B0(0x0009, 0x0A)
    OP_B0(0x000A, 0x0A)
    OP_B0(0x000B, 0x0A)
    OP_B0(0x000C, 0x0A)
    OP_B0(0x000D, 0x0A)
    OP_B0(0x000E, 0x0A)
    OP_B0(0x000F, 0x0A)
    OP_B0(0x0010, 0x0A)
    OP_B0(0x0011, 0x0A)
    OP_B0(0x0012, 0x0A)
    OP_B0(0x0013, 0x0A)
    OP_B0(0x0014, 0x0A)
    OP_B0(0x0015, 0x0A)
    OP_B0(0x0016, 0x0A)
    OP_6F(0x0003, 18)
    OP_6F(0x0004, 18)
    OP_6F(0x0005, 18)
    OP_6F(0x0006, 18)
    OP_6F(0x0007, 18)
    OP_6F(0x0008, 18)
    OP_6F(0x0009, 18)
    OP_6F(0x000A, 18)
    OP_6F(0x000B, 18)
    OP_6F(0x000C, 18)
    OP_6F(0x000D, 18)
    OP_6F(0x000E, 18)
    OP_6F(0x000F, 18)
    OP_6F(0x0010, 18)
    OP_6F(0x0011, 18)
    OP_6F(0x0012, 18)
    OP_6F(0x0013, 18)
    OP_6F(0x0014, 18)
    OP_6F(0x0015, 18)
    OP_6F(0x0016, 18)
    Sleep(250)

    OP_70(0x000F, 20)
    OP_70(0x0010, 20)
    Sleep(250)

    Sleep(250)

    OP_70(0x0004, 20)
    OP_70(0x0003, 20)
    Sleep(250)

    OP_70(0x0013, 20)
    OP_70(0x0014, 20)
    Sleep(250)

    Sleep(250)

    OP_70(0x0016, 20)
    OP_70(0x0015, 20)
    Sleep(250)

    Sleep(250)

    OP_70(0x0007, 20)
    OP_70(0x0005, 20)

    @scena.Lambda('lambda_2A11')
    def lambda_2A11():
        OP_6E(665, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_2A11)

    Sleep(250)

    Sleep(500)

    PlaySE(145, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x00FF, 67290, 1000, -13940, 0, 0, 0, 4500, 4500, 4500, 0x00FF, 0, 0, 0, 0)
    WaitForThreadExit(0x0000, 0x0001)
    OP_77(0x8C, 0x8C, 0x8C, 0x00, 0x000007D0)
    OP_72(0x0000, 0x0020)
    OP_72(0x0001, 0x0020)
    OP_72(0x0002, 0x0020)
    OP_6F(0x0000, 4000)
    OP_6F(0x0001, 4000)
    OP_6F(0x0002, 4000)
    OP_70(0x0000, 4060)
    OP_70(0x0001, 4060)
    OP_70(0x0002, 4060)

    @scena.Lambda('lambda_2AAC')
    def lambda_2AAC():
        CameraMove(280, 0, 25240, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2AAC)

    Sleep(200)

    OP_70(0x000E, 20)
    OP_70(0x0006, 20)
    Sleep(200)

    OP_70(0x0008, 20)
    OP_70(0x000D, 20)
    Sleep(200)

    OP_70(0x000C, 20)
    OP_70(0x0009, 20)
    Sleep(100)

    OP_70(0x000B, 20)
    OP_70(0x0011, 20)
    Sleep(100)

    OP_70(0x000A, 20)
    Sleep(100)

    OP_70(0x0012, 20)
    Sleep(500)

    Sleep(1000)

    Fade(1000)
    CameraMove(57500, 0, -2650, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0540140274V#105F#5P糟了！\n',
            '是『导力停止现象』！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_24(0x0085, 0x5A)
    Sleep(200)

    OP_24(0x0085, 0x50)
    Sleep(200)

    OP_24(0x0085, 0x46)
    Sleep(200)

    OP_24(0x0085, 0x3C)
    Sleep(200)

    OP_24(0x0085, 0x32)
    Sleep(200)

    OP_24(0x0085, 0x28)
    Sleep(200)

    OP_24(0x0085, 0x1E)
    Sleep(200)

    OP_24(0x0085, 0x14)
    Sleep(200)

    OP_24(0x0085, 0x0A)
    Sleep(200)

    OP_23(0x0085)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C4303._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0010 offset: 0x2C0B
@scena.Code('func_10_2C0B')
def func_10_2C0B():
    PlaySE(145, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x00FF, 67290, 1000, -13940, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    Sleep(800)

    StopEffect(0x06, 0x02)
    PlaySE(145, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x00FF, 67290, 1000, -13940, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    Sleep(1100)

    PlaySE(145, 0x00, 0x64)
    PlayEffect(0x01, 0xFF, 0x00FF, 67290, 1000, -13940, 0, 0, 0, 3000, 3000, 3000, 0x00FF, 0, 0, 0, 0)
    Sleep(1000)

    Sleep(800)

    Sleep(800)

    Sleep(800)

    Sleep(500)

    Return()

# id: 0x0011 offset: 0x2CE0
@scena.Code('func_11_2CE0')
def func_11_2CE0():
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '这是一台可供旅行者回复体力的导力器装置。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

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
        32,
        1,
        (
            TXT(0x00, '在此休息\n'),
            TXT(0x01, '离开\n'),
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

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E9C',
    )

    FadeIn(100, 0)
    Sleep(500)

    OP_26(13)
    OP_72(0x0019, 0x0020)
    OP_6F(0x0019, 300)
    OP_70(0x0019, 500)
    OP_73(0x0019)
    OP_6F(0x0019, 500)
    OP_70(0x0019, 700)
    OP_71(0x0019, 0x0020)
    OP_20(0x00000BB8)
    PlaySE(12, 0x00, 0x64)
    StopEffect(0x06, 0x02)
    LoadEffect(0x05, 'map\\\\mp027_01.eff')
    PlayEffect(0x05, 0x06, 0x00FF, 62990, 1200, -2920, 0, 0, 0, 1500, 1500, 1500, 0x00FF, 0, 0, 0, 0)
    FadeOut(1500, 0, -1)
    Sleep(1500)

    PlaySE(13, 0x00, 0x64)
    OP_0D()
    SetChrStatus(0x0000, 0xFE, 0)
    SetChrStatus(0x0001, 0xFE, 0)
    SetChrStatus(0x0002, 0xFE, 0)
    SetChrStatus(0x0003, 0xFE, 0)
    SetChrStatus(0x0004, 0xFE, 0)
    SetChrStatus(0x0005, 0xFE, 0)
    SetChrStatus(0x0006, 0xFE, 0)
    SetChrStatus(0x0007, 0xFE, 0)
    OP_69(0x0000, 0)
    OP_30(0x00)
    Sleep(3500)

    StopEffect(0x06, 0x00)
    LoadEffect(0x05, 'map\\\\mp027_00.eff')
    PlayEffect(0x05, 0x00, 0x00FF, 62990, 1200, -2920, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)
    OP_6F(0x0019, 0)
    OP_70(0x0019, 250)
    OP_1E()
    FadeIn(1000, 0)
    OP_56(0x00)
    TalkEnd(0x00FF)

    Return()

    def _loc_2E9C(): pass

    label('loc_2E9C')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2EB6',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_2EB6(): pass

    label('loc_2EB6')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
