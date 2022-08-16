import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C4301_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C4301   ._SN')

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

# id: 0x10001 offset: 0x18A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '凯诺娜上尉',
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
            name                = '拉赛尔博士',
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
            name                = '基库',
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
            name                = '机器',
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
            name                = '机器',
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
            name                = '雪拉扎德',
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
            name                = '奥利维尔',
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
            name                = '科洛丝',
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
            name                = '阿加特',
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
            name                = '提妲',
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
            name                = '金',
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

# id: 0x10002 offset: 0x2EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x2EA
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

# id: 0x10004 offset: 0x30A
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
@scena.Code('Init')
def Init():
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
    Event(0, func_0F_2936)

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
@scena.Code('func_01_362')
def func_01_362():
    LoadEffect(0x05, 'map\\\\mp027_00.eff')
    PlayEffect(0x05, 0x06, 0x00FF, 62990, 1200, -2920, 0, 0, 0, 1300, 1300, 1300, 0x00FF, 0, 0, 0, 0)

    Return()

# id: 0x0002 offset: 0x3AC
@scena.Code('func_02_3AC')
def func_02_3AC():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3C1',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_3AC')

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

# id: 0x0004 offset: 0x421
@scena.Code('func_04_421')
def func_04_421():
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

# id: 0x0005 offset: 0x4E1
@scena.Code('func_05_4E1')
def func_05_4E1():
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

# id: 0x0006 offset: 0x560
@scena.Code('func_06_560')
def func_06_560():
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

# id: 0x0007 offset: 0x5D5
@scena.Code('func_07_5D5')
def func_07_5D5():
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

# id: 0x0008 offset: 0x645
@scena.Code('func_08_645')
def func_08_645():
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

# id: 0x0009 offset: 0x69A
@scena.Code('func_09_69A')
def func_09_69A():
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
        'loc_70F',
    )

    Call(0, 0x000A)
    OP_56(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_70F(): pass

    label('loc_70F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_726',
    )

    Call(0, 0x000B)
    OP_56(0x00)
    TalkEnd(0x0009)

    Return()

    def _loc_726(): pass

    label('loc_726')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_777',
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

    def _loc_777(): pass

    label('loc_777')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_788',
    )

    TalkEnd(0x0009)

    Return()

    def _loc_788(): pass

    label('loc_788')

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

# id: 0x000A offset: 0x7F7
@scena.Code('func_0A_7F7')
def func_0A_7F7():
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

# id: 0x000B offset: 0x83B
@scena.Code('func_0B_83B')
def func_0B_83B():
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

# id: 0x000C offset: 0x866
@scena.Code('func_0C_866')
def func_0C_866():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 0, 0x668)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 7, 0x667)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_873',
    )

    Return()

    def _loc_873(): pass

    label('loc_873')

    SetScenaFlags(ScenaFlag(0x00CD, 0, 0x668))
    EventBegin(0x00)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000C, 0x0004)
    ChrSetRGBAMask(0x000B, 255, 0, 0, 0, 0)
    ChrSetRGBAMask(0x000C, 255, 0, 0, 0, 0)
    ChrSetPos(0x0008, 61000, 0, -13970, 270)
    ChrSetPos(0x000B, 59250, 6000, -11650, 270)
    ChrSetPos(0x000C, 59250, 6000, -16329, 270)

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

    @scena.Lambda('lambda_098D')
    def lambda_098D():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_098D)

    @scena.Lambda('lambda_099B')
    def lambda_099B():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_099B)

    @scena.Lambda('lambda_09A9')
    def lambda_09A9():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_09A9)

    @scena.Lambda('lambda_09B7')
    def lambda_09B7():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_09B7)

    @scena.Lambda('lambda_09C5')
    def lambda_09C5():
        OP_67(0, 8170, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_09C5)

    @scena.Lambda('lambda_09DD')
    def lambda_09DD():
        OP_6C(37000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_09DD)

    CameraMove(57560, 0, -13380, 2000)
    ChrSetChipByIndex(0x0101, 4)
    ChrSetChipByIndex(0x0102, 6)

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A15',
    )

    ChrSetChipByIndex(0x0103, 8)

    def _loc_A15(): pass

    label('loc_A15')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A28',
    )

    ChrSetChipByIndex(0x0104, 10)

    def _loc_A28(): pass

    label('loc_A28')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A3B',
    )

    ChrSetChipByIndex(0x0106, 14)

    def _loc_A3B(): pass

    label('loc_A3B')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A4E',
    )

    ChrSetChipByIndex(0x0105, 12)

    def _loc_A4E(): pass

    label('loc_A4E')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A61',
    )

    ChrSetChipByIndex(0x0107, 16)

    def _loc_A61(): pass

    label('loc_A61')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A74',
    )

    ChrSetChipByIndex(0x0108, 18)

    def _loc_A74(): pass

    label('loc_A74')

    ChrSetPos(0x0000, 45670, 0, -14030, 90)
    ChrSetPos(0x0001, 45670, 0, -14030, 90)
    ChrSetPos(0x0002, 45670, 0, -14030, 90)
    ChrSetPos(0x0003, 45670, 0, -14030, 90)

    @scena.Lambda('lambda_0ABE')
    def lambda_0ABE():
        ChrWalkTo(0x00FE, 53520, 0, -13400, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0ABE)

    Sleep(500)

    @scena.Lambda('lambda_0ADE')
    def lambda_0ADE():
        ChrWalkTo(0x00FE, 53520, 0, -14710, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_0ADE)

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
        'loc_B58',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_B3A',
    )

    Sleep(500)

    @scena.Lambda('lambda_0B22')
    def lambda_0B22():
        ChrWalkTo(0x00FE, 52890, 0, -16059, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0B22)

    Jump('loc_B55')

    def _loc_B3A(): pass

    label('loc_B3A')

    @scena.Lambda('lambda_0B40')
    def lambda_0B40():
        ChrWalkTo(0x00FE, 52860, 0, -12160, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_0B40)

    def _loc_B55(): pass

    label('loc_B55')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_B58(): pass

    label('loc_B58')

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
        'loc_BB5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_B97',
    )

    Sleep(500)

    @scena.Lambda('lambda_0B7F')
    def lambda_0B7F():
        ChrWalkTo(0x00FE, 52890, 0, -16059, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_0B7F)

    Jump('loc_BB2')

    def _loc_B97(): pass

    label('loc_B97')

    @scena.Lambda('lambda_0B9D')
    def lambda_0B9D():
        ChrWalkTo(0x00FE, 52860, 0, -12160, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_0B9D)

    def _loc_BB2(): pass

    label('loc_BB2')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_BB5(): pass

    label('loc_BB5')

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
        'loc_C12',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_BF4',
    )

    Sleep(500)

    @scena.Lambda('lambda_0BDC')
    def lambda_0BDC():
        ChrWalkTo(0x00FE, 52890, 0, -16059, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0000, lambda_0BDC)

    Jump('loc_C0F')

    def _loc_BF4(): pass

    label('loc_BF4')

    @scena.Lambda('lambda_0BFA')
    def lambda_0BFA():
        ChrWalkTo(0x00FE, 52860, 0, -12160, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0000, lambda_0BFA)

    def _loc_C0F(): pass

    label('loc_C0F')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_C12(): pass

    label('loc_C12')

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
        'loc_C6F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_C51',
    )

    Sleep(500)

    @scena.Lambda('lambda_0C39')
    def lambda_0C39():
        ChrWalkTo(0x00FE, 52890, 0, -16059, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0000, lambda_0C39)

    Jump('loc_C6C')

    def _loc_C51(): pass

    label('loc_C51')

    @scena.Lambda('lambda_0C57')
    def lambda_0C57():
        ChrWalkTo(0x00FE, 52860, 0, -12160, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0000, lambda_0C57)

    def _loc_C6C(): pass

    label('loc_C6C')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_C6F(): pass

    label('loc_C6F')

    WaitForThreadExit(0x0000, 0x0000)
    ChrSetDirection(0x0000, 90, 0)
    WaitForThreadExit(0x0001, 0x0000)
    ChrSetDirection(0x0001, 90, 0)
    WaitForThreadExit(0x0002, 0x0000)
    ChrSetDirection(0x0002, 90, 0)
    WaitForThreadExit(0x0003, 0x0000)
    ChrSetDirection(0x0003, 90, 0)

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
        'loc_EA4',
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

    Jump('loc_1122')

    def _loc_EA4(): pass

    label('loc_EA4')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F22',
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

    Jump('loc_1122')

    def _loc_F22(): pass

    label('loc_F22')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_F9A',
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

    Jump('loc_1122')

    def _loc_F9A(): pass

    label('loc_F9A')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_100D',
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

    Jump('loc_1122')

    def _loc_100D(): pass

    label('loc_100D')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_108F',
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

    Jump('loc_1122')

    def _loc_108F(): pass

    label('loc_108F')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1122',
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

    def _loc_1122(): pass

    label('loc_1122')

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

    @scena.Lambda('lambda_11A5')
    def lambda_11A5():
        ChrJumpTo(0x00FE, 59250, 0, -11650, 1000, 5000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_11A5)

    ChrSetRGBAMask(0x000B, 100, 100, 255, 255, 100)
    ChrSetRGBAMask(0x000B, 255, 255, 255, 255, 100)
    WaitForThreadExit(0x000B, 0x0001)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 500, 3000, 100)

    @scena.Lambda('lambda_11F4')
    def lambda_11F4():
        OP_99(0x00FE, 0x00, 0x07, 2000)
        Yield()

        Jump('lambda_11F4')

    DispatchAsync2(0x000B, 0x0001, lambda_11F4)

    @scena.Lambda('lambda_1207')
    def lambda_1207():
        ChrJumpTo(0x00FE, 59250, 0, -16329, 1000, 5000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1207)

    ChrSetRGBAMask(0x000C, 100, 100, 255, 255, 100)
    ChrSetRGBAMask(0x000C, 255, 255, 255, 255, 100)
    WaitForThreadExit(0x000C, 0x0001)
    PlaySE(200, 0x00, 0x64)
    OP_7C(0, 500, 3000, 100)

    @scena.Lambda('lambda_1256')
    def lambda_1256():
        OP_99(0x00FE, 0x00, 0x07, 2000)
        Yield()

        Jump('lambda_1256')

    DispatchAsync2(0x000C, 0x0001, lambda_1256)

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
        'loc_13CA',
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

    Jump('loc_1547')

    def _loc_13CA(): pass

    label('loc_13CA')

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
        'loc_1417',
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

    Jump('loc_1547')

    def _loc_1417(): pass

    label('loc_1417')

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
        'loc_145B',
    )

    ChrTalk(
        0x0106,
        (
            '#0050140099V#057F#5P嘁……不要开玩笑了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1547')

    def _loc_145B(): pass

    label('loc_145B')

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
        'loc_14C2',
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

    Jump('loc_1547')

    def _loc_14C2(): pass

    label('loc_14C2')

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
        'loc_1508',
    )

    ChrTalk(
        0x0108,
        (
            '#0080140101V#075F#5P喂喂，你不要命了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1547')

    def _loc_1508(): pass

    label('loc_1508')

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
        'loc_1547',
    )

    ChrTalk(
        0x0105,
        (
            '#0060140102V#043F#5P这、这太危险了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1547(): pass

    label('loc_1547')

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

    @scena.Lambda('lambda_159D')
    def lambda_159D():
        OP_92(0x00FE, 0x0008, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_159D)

    Sleep(10)

    @scena.Lambda('lambda_15B7')
    def lambda_15B7():
        OP_92(0x00FE, 0x0008, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0000, lambda_15B7)

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
        'loc_161F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1607',
    )

    Sleep(10)

    @scena.Lambda('lambda_15F5')
    def lambda_15F5():
        OP_92(0x00FE, 0x000C, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_15F5)

    Jump('loc_161C')

    def _loc_1607(): pass

    label('loc_1607')

    @scena.Lambda('lambda_160D')
    def lambda_160D():
        OP_92(0x00FE, 0x000B, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0000, 0x0000, lambda_160D)

    def _loc_161C(): pass

    label('loc_161C')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_161F(): pass

    label('loc_161F')

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
        'loc_1670',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1658',
    )

    Sleep(10)

    @scena.Lambda('lambda_1646')
    def lambda_1646():
        OP_92(0x00FE, 0x000C, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_1646)

    Jump('loc_166D')

    def _loc_1658(): pass

    label('loc_1658')

    @scena.Lambda('lambda_165E')
    def lambda_165E():
        OP_92(0x00FE, 0x000B, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0001, 0x0000, lambda_165E)

    def _loc_166D(): pass

    label('loc_166D')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_1670(): pass

    label('loc_1670')

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
        'loc_16C1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_16A9',
    )

    Sleep(10)

    @scena.Lambda('lambda_1697')
    def lambda_1697():
        OP_92(0x00FE, 0x000C, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0000, lambda_1697)

    Jump('loc_16BE')

    def _loc_16A9(): pass

    label('loc_16A9')

    @scena.Lambda('lambda_16AF')
    def lambda_16AF():
        OP_92(0x00FE, 0x000B, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0002, 0x0000, lambda_16AF)

    def _loc_16BE(): pass

    label('loc_16BE')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_16C1(): pass

    label('loc_16C1')

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
        'loc_1712',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_16FA',
    )

    Sleep(10)

    @scena.Lambda('lambda_16E8')
    def lambda_16E8():
        OP_92(0x00FE, 0x000C, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0000, lambda_16E8)

    Jump('loc_170F')

    def _loc_16FA(): pass

    label('loc_16FA')

    @scena.Lambda('lambda_1700')
    def lambda_1700():
        OP_92(0x00FE, 0x000B, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0003, 0x0000, lambda_1700)

    def _loc_170F(): pass

    label('loc_170F')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_1712(): pass

    label('loc_1712')

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

    ChrSetChipByIndex(0x000B, 20)

    @scena.Lambda('lambda_172D')
    def lambda_172D():
        ChrWalkTo(0x00FE, 52250, 0, -11650, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_172D)

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

    ChrSetChipByIndex(0x000C, 20)

    @scena.Lambda('lambda_175D')
    def lambda_175D():
        ChrWalkTo(0x00FE, 52250, 0, -16329, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_175D)

    Sleep(10)

    @scena.Lambda('lambda_177D')
    def lambda_177D():
        OP_92(0x00FE, 0x0000, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_177D)

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
        (0x00000001, 'loc_17C6'),
        (-1, 'loc_17C9'),
    )

    def _loc_17C6(): pass

    label('loc_17C6')

    OP_B4(0x00)

    Return()

    def _loc_17C9(): pass

    label('loc_17C9')

    EventBegin(0x00)
    ChrSetPos(0x0101, 57050, 0, -12660, 132)
    ChrSetPos(0x0102, 56160, 0, -14450, 88)
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
        'loc_1834',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1820',
    )

    ChrSetPos(0x0000, 57840, 0, -15280, 27)

    Jump('loc_1831')

    def _loc_1820(): pass

    label('loc_1820')

    ChrSetPos(0x0000, 56200, 0, -11470, 112)

    def _loc_1831(): pass

    label('loc_1831')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_1834(): pass

    label('loc_1834')

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
        'loc_1878',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1864',
    )

    ChrSetPos(0x0001, 57840, 0, -15280, 27)

    Jump('loc_1875')

    def _loc_1864(): pass

    label('loc_1864')

    ChrSetPos(0x0001, 56200, 0, -11470, 112)

    def _loc_1875(): pass

    label('loc_1875')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_1878(): pass

    label('loc_1878')

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
        'loc_18BC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_18A8',
    )

    ChrSetPos(0x0002, 57840, 0, -15280, 27)

    Jump('loc_18B9')

    def _loc_18A8(): pass

    label('loc_18A8')

    ChrSetPos(0x0002, 56200, 0, -11470, 112)

    def _loc_18B9(): pass

    label('loc_18B9')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_18BC(): pass

    label('loc_18BC')

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
        'loc_1900',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_18EC',
    )

    ChrSetPos(0x0003, 57840, 0, -15280, 27)

    Jump('loc_18FD')

    def _loc_18EC(): pass

    label('loc_18EC')

    ChrSetPos(0x0003, 56200, 0, -11470, 112)

    def _loc_18FD(): pass

    label('loc_18FD')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_1900(): pass

    label('loc_1900')

    ChrSetPos(0x0008, 59690, 0, -13480, 0)
    ChrSetChipByIndex(0x0008, 21)
    ChrSetSubChip(0x0008, 0)
    ChrClearFlags(0x0008, 0x0001)
    ChrSetFlags(0x0008, 0x0800)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x000C, 0x0080)
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
        'loc_1B45',
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
    ChrSetChipByIndex(0x0000, 65535)
    ChrSetChipByIndex(0x0001, 65535)
    ChrSetChipByIndex(0x0002, 65535)
    ChrSetChipByIndex(0x0003, 65535)
    ChrSetDirection(0x0105, 270, 400)

    @scena.Lambda('lambda_1ACA')
    def lambda_1ACA():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1ACA)

    @scena.Lambda('lambda_1AD8')
    def lambda_1AD8():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1AD8)

    @scena.Lambda('lambda_1AE6')
    def lambda_1AE6():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1AE6)

    @scena.Lambda('lambda_1AF4')
    def lambda_1AF4():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1AF4)

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

    Jump('loc_1C3B')

    def _loc_1B45(): pass

    label('loc_1B45')

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
    ChrSetChipByIndex(0x0000, 65535)
    ChrSetChipByIndex(0x0001, 65535)
    ChrSetChipByIndex(0x0002, 65535)
    ChrSetChipByIndex(0x0003, 65535)
    ChrSetDirection(0x0101, 270, 400)

    @scena.Lambda('lambda_1BC7')
    def lambda_1BC7():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_1BC7)

    @scena.Lambda('lambda_1BD5')
    def lambda_1BD5():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_1BD5)

    @scena.Lambda('lambda_1BE3')
    def lambda_1BE3():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_1BE3)

    @scena.Lambda('lambda_1BF1')
    def lambda_1BF1():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_1BF1)

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

    def _loc_1C3B(): pass

    label('loc_1C3B')

    ChrClearFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0004)
    ChrSetPos(0x000A, 37300, 5000, -13990, 0)
    PlaySE(140, 0x00, 0x64)

    @scena.Lambda('lambda_1C61')
    def lambda_1C61():
        CameraMove(52800, 0, -14030, 2000)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1C61)

    @scena.Lambda('lambda_1C79')
    def lambda_1C79():
        ChrWalkTo(0x00FE, 55480, 1000, -13580, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1C79)

    Sleep(500)

    FadeOut(2000, 0, -1)
    OP_0D()
    Sleep(500)

    ChrSetPos(0x0101, 54150, 0, -5010, 45)
    ChrSetPos(0x0102, 55010, 0, -6060, 45)
    ChrSetFlags(0x000A, 0x0080)
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
        'loc_1D11',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1CFD',
    )

    ChrSetPos(0x0000, 53820, 0, -7240, 45)

    Jump('loc_1D0E')

    def _loc_1CFD(): pass

    label('loc_1CFD')

    ChrSetPos(0x0000, 52900, 0, -6250, 45)

    def _loc_1D0E(): pass

    label('loc_1D0E')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_1D11(): pass

    label('loc_1D11')

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
        'loc_1D55',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1D41',
    )

    ChrSetPos(0x0001, 53820, 0, -7240, 45)

    Jump('loc_1D52')

    def _loc_1D41(): pass

    label('loc_1D41')

    ChrSetPos(0x0001, 52900, 0, -6250, 45)

    def _loc_1D52(): pass

    label('loc_1D52')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_1D55(): pass

    label('loc_1D55')

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
        'loc_1D99',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1D85',
    )

    ChrSetPos(0x0002, 53820, 0, -7240, 45)

    Jump('loc_1D96')

    def _loc_1D85(): pass

    label('loc_1D85')

    ChrSetPos(0x0002, 52900, 0, -6250, 45)

    def _loc_1D96(): pass

    label('loc_1D96')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_1D99(): pass

    label('loc_1D99')

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
        'loc_1DDD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Return,
        ),
        'loc_1DC9',
    )

    ChrSetPos(0x0003, 53820, 0, -7240, 45)

    Jump('loc_1DDA')

    def _loc_1DC9(): pass

    label('loc_1DC9')

    ChrSetPos(0x0003, 52900, 0, -6250, 45)

    def _loc_1DDA(): pass

    label('loc_1DDA')

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    def _loc_1DDD(): pass

    label('loc_1DDD')

    OP_4A(0x0009, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x000E, 255)
    OP_4A(0x000F, 255)
    OP_4A(0x0010, 255)
    OP_4A(0x0011, 255)
    OP_4A(0x0012, 255)
    Call(0, 0x000E)
    ChrSetFlags(0x0008, 0x0800)
    ChrClearFlags(0x0008, 0x0001)
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

# id: 0x000D offset: 0x2051
@scena.Code('func_0D_2051')
def func_0D_2051():
    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2062',
    )

    FormationDelMember(0x02, 0xFF)

    def _loc_2062(): pass

    label('loc_2062')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2073',
    )

    FormationDelMember(0x03, 0xFF)

    def _loc_2073(): pass

    label('loc_2073')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2084',
    )

    FormationDelMember(0x05, 0xFF)

    def _loc_2084(): pass

    label('loc_2084')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2095',
    )

    FormationDelMember(0x04, 0xFF)

    def _loc_2095(): pass

    label('loc_2095')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20A6',
    )

    FormationDelMember(0x06, 0xFF)

    def _loc_20A6(): pass

    label('loc_20A6')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_20B7',
    )

    FormationDelMember(0x07, 0xFF)

    def _loc_20B7(): pass

    label('loc_20B7')

    Fade(1000)
    ChrSetPos(0x0101, 54150, 0, -5010, 45)
    ChrSetPos(0x0102, 55010, 0, -6060, 45)
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

    def _loc_216F(): pass

    label('loc_216F')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0xFF),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2746',
    )

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2208',
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

    Jump('loc_253F')

    def _loc_2208(): pass

    label('loc_2208')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2294',
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

    Jump('loc_253F')

    def _loc_2294(): pass

    label('loc_2294')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2320',
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

    Jump('loc_253F')

    def _loc_2320(): pass

    label('loc_2320')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_23AC',
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

    Jump('loc_253F')

    def _loc_23AC(): pass

    label('loc_23AC')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2438',
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

    Jump('loc_253F')

    def _loc_2438(): pass

    label('loc_2438')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_24C4',
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

    Jump('loc_253F')

    def _loc_24C4(): pass

    label('loc_24C4')

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

    def _loc_253F(): pass

    label('loc_253F')

    MenuEnd(0x0000)
    OP_5F(0x0000)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_2566'),
        (0x00000001, 'loc_2580'),
        (0x00000002, 'loc_259A'),
        (0x00000003, 'loc_25B4'),
        (0x00000004, 'loc_25CE'),
        (0x00000005, 'loc_25E8'),
        (-1, 'loc_2602'),
    )

    def _loc_2566(): pass

    label('loc_2566')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_257A',
    )

    FormationAddMember(0x02, 0xFF)

    Jump('loc_257D')

    def _loc_257A(): pass

    label('loc_257A')

    FormationDelMember(0x02, 0xFF)

    def _loc_257D(): pass

    label('loc_257D')

    Jump('loc_267A')

    def _loc_2580(): pass

    label('loc_2580')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2594',
    )

    FormationAddMember(0x03, 0xFF)

    Jump('loc_2597')

    def _loc_2594(): pass

    label('loc_2594')

    FormationDelMember(0x03, 0xFF)

    def _loc_2597(): pass

    label('loc_2597')

    Jump('loc_267A')

    def _loc_259A(): pass

    label('loc_259A')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_25AE',
    )

    FormationAddMember(0x05, 0xFF)

    Jump('loc_25B1')

    def _loc_25AE(): pass

    label('loc_25AE')

    FormationDelMember(0x05, 0xFF)

    def _loc_25B1(): pass

    label('loc_25B1')

    Jump('loc_267A')

    def _loc_25B4(): pass

    label('loc_25B4')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_25C8',
    )

    FormationAddMember(0x06, 0xFF)

    Jump('loc_25CB')

    def _loc_25C8(): pass

    label('loc_25C8')

    FormationDelMember(0x06, 0xFF)

    def _loc_25CB(): pass

    label('loc_25CB')

    Jump('loc_267A')

    def _loc_25CE(): pass

    label('loc_25CE')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_25E2',
    )

    FormationAddMember(0x07, 0xFF)

    Jump('loc_25E5')

    def _loc_25E2(): pass

    label('loc_25E2')

    FormationDelMember(0x07, 0xFF)

    def _loc_25E5(): pass

    label('loc_25E5')

    Jump('loc_267A')

    def _loc_25E8(): pass

    label('loc_25E8')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_25FC',
    )

    FormationAddMember(0x04, 0xFF)

    Jump('loc_25FF')

    def _loc_25FC(): pass

    label('loc_25FC')

    FormationDelMember(0x04, 0xFF)

    def _loc_25FF(): pass

    label('loc_25FF')

    Jump('loc_267A')

    def _loc_2602(): pass

    label('loc_2602')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2616',
    )

    FormationDelMember(0x02, 0xFF)

    Jump('loc_2677')

    def _loc_2616(): pass

    label('loc_2616')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_262A',
    )

    FormationDelMember(0x03, 0xFF)

    Jump('loc_2677')

    def _loc_262A(): pass

    label('loc_262A')

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_263E',
    )

    FormationDelMember(0x05, 0xFF)

    Jump('loc_2677')

    def _loc_263E(): pass

    label('loc_263E')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2652',
    )

    FormationDelMember(0x04, 0xFF)

    Jump('loc_2677')

    def _loc_2652(): pass

    label('loc_2652')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2666',
    )

    FormationDelMember(0x06, 0xFF)

    Jump('loc_2677')

    def _loc_2666(): pass

    label('loc_2666')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2677',
    )

    FormationDelMember(0x07, 0xFF)

    def _loc_2677(): pass

    label('loc_2677')

    Jump('loc_267A')

    def _loc_267A(): pass

    label('loc_267A')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_269D',
    )

    ChrSetFlags(0x0003, 0x0080)
    ChrSetFlags(0x0002, 0x0080)

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Jump('loc_2721')

    def _loc_269D(): pass

    label('loc_269D')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_26DE',
    )

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '请选择除了约修亚和艾丝蒂尔以外的两名成员。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    Jump('loc_2721')

    def _loc_26DE(): pass

    label('loc_26DE')

    If(
        (
            (Expr.PushValueByIndex, 0x5),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2721',
    )

    ChrSetFlags(0x0002, 0x0080)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '请选择除了约修亚和艾丝蒂尔以外的两名成员。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    def _loc_2721(): pass

    label('loc_2721')

    ChrSetPos(0x0101, 54150, 0, -5010, 45)
    ChrSetPos(0x0102, 55010, 0, -6060, 45)

    Jump('loc_216F')

    def _loc_2746(): pass

    label('loc_2746')

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
    ChrSetPos(0x0101, 54150, 0, -5010, 45)
    ChrSetPos(0x0102, 55010, 0, -6060, 45)
    ChrClearFlags(0x0002, 0x0080)
    ChrClearFlags(0x0003, 0x0080)
    ChrSetPos(0x0002, 54470, 0, -7820, 27)
    ChrSetPos(0x0003, 56010, 0, -8590, 27)
    Call(0, 0x000E)
    CameraMove(56230, 0, -3780, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    Return()

# id: 0x000E offset: 0x27F2
@scena.Code('func_0E_27F2')
def func_0E_27F2():
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 55790, 0, -4250, 225)
    ChrSetFlags(0x0008, 0x0800)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 60460, 0, 480, 90)
    ChrSetChipByIndex(0x0008, 21)
    ChrClearFlags(0x0008, 0x0001)

    If(
        (
            (Expr.Eval, "OP_42(0x0005)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2854',
    )

    ChrClearFlags(0x0010, 0x0080)
    ChrSetPos(0x0010, 55690, 0, 1000, 180)

    Jump('loc_2859')

    def _loc_2854(): pass

    label('loc_2854')

    ChrSetFlags(0x0010, 0x0080)

    def _loc_2859(): pass

    label('loc_2859')

    If(
        (
            (Expr.Eval, "OP_42(0x0006)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2880',
    )

    ChrClearFlags(0x0011, 0x0080)
    ChrSetPos(0x0011, 54740, 0, -1560, 180)

    Jump('loc_2885')

    def _loc_2880(): pass

    label('loc_2880')

    ChrSetFlags(0x0011, 0x0080)

    def _loc_2885(): pass

    label('loc_2885')

    If(
        (
            (Expr.Eval, "OP_42(0x0003)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_28AC',
    )

    ChrClearFlags(0x000E, 0x0080)
    ChrSetPos(0x000E, 57870, 0, -2040, 225)

    Jump('loc_28B1')

    def _loc_28AC(): pass

    label('loc_28AC')

    ChrSetFlags(0x000E, 0x0080)

    def _loc_28B1(): pass

    label('loc_28B1')

    If(
        (
            (Expr.Eval, "OP_42(0x0002)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_28D8',
    )

    ChrClearFlags(0x000D, 0x0080)
    ChrSetPos(0x000D, 57210, 0, -860, 225)

    Jump('loc_28DD')

    def _loc_28D8(): pass

    label('loc_28D8')

    ChrSetFlags(0x000D, 0x0080)

    def _loc_28DD(): pass

    label('loc_28DD')

    If(
        (
            (Expr.Eval, "OP_42(0x0007)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2904',
    )

    ChrClearFlags(0x0012, 0x0080)
    ChrSetPos(0x0012, 59350, 0, -3220, 225)

    Jump('loc_2909')

    def _loc_2904(): pass

    label('loc_2904')

    ChrSetFlags(0x0012, 0x0080)

    def _loc_2909(): pass

    label('loc_2909')

    If(
        (
            (Expr.Eval, "OP_42(0x0004)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2930',
    )

    ChrClearFlags(0x000F, 0x0080)
    ChrSetPos(0x000F, 56420, 0, -2530, 225)

    Jump('loc_2935')

    def _loc_2930(): pass

    label('loc_2930')

    ChrSetFlags(0x000F, 0x0080)

    def _loc_2935(): pass

    label('loc_2935')

    Return()

# id: 0x000F offset: 0x2936
@scena.Code('func_0F_2936')
def func_0F_2936():
    EventBegin(0x00)
    OP_4A(0x0009, 255)
    OP_4A(0x000D, 255)
    OP_4A(0x000E, 255)
    OP_4A(0x000F, 255)
    OP_4A(0x0010, 255)
    OP_4A(0x0011, 255)
    OP_4A(0x0012, 255)
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)

    @scena.Lambda('lambda_296E')
    def lambda_296E():
        OP_7C(0, 100, 2000, 3000)
        Yield()

        Jump('lambda_296E')

    DispatchAsync2(0x0009, 0x0003, lambda_296E)

    PlaySE(133, 0x01, 0x64)
    LoadEffect(0x01, 'map\\\\mp015_00.eff')
    CreateThread(0x0101, 0x00, 0x00, func_10_2D73)
    CameraMove(55710, 0, -7780, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3200, 0)
    OP_6C(134000, 0)
    OP_6E(513, 0)
    FadeIn(2000, 0)
    Sleep(600)

    OP_77(0xC8, 0xC8, 0xC8, 0x00, 0x00000BB8)

    @scena.Lambda('lambda_29FD')
    def lambda_29FD():
        CameraMove(-130, 0, -14000, 3500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_29FD)

    @scena.Lambda('lambda_2A15')
    def lambda_2A15():
        OP_6C(45000, 5500)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_2A15)

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

    @scena.Lambda('lambda_2B74')
    def lambda_2B74():
        OP_6E(665, 1500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_2B74)

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

    @scena.Lambda('lambda_2C0F')
    def lambda_2C0F():
        CameraMove(280, 0, 25240, 2000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_2C0F)

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

# id: 0x0010 offset: 0x2D73
@scena.Code('func_10_2D73')
def func_10_2D73():
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

# id: 0x0011 offset: 0x2E48
@scena.Code('func_11_2E48')
def func_11_2E48():
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
        'loc_3004',
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
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
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

    def _loc_3004(): pass

    label('loc_3004')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_301E',
    )

    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

    def _loc_301E(): pass

    label('loc_301E')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
