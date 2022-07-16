import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4210_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4210   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '凯诺娜上尉'),
    TXT(0x02, '茜亚'),
    TXT(0x03, '理查德上校'),
    TXT(0x04, '特务兵'),
    TXT(0x05, '特务兵'),
    TXT(0x06, '特务兵'),
    TXT(0x07, '特务兵'),
    TXT(0x08, '特务兵'),
    TXT(0x09, '王国军士兵'),
    TXT(0x0A, '王国军士兵'),
    TXT(0x0B, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4210.x'
    header.mapIndex       = 1
    header.bgm            = 17
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x3178
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
        ('ED6_DT07/CH02100._CH', 'ED6_DT07/CH02100P._CP'),
        ('ED6_DT07/CH02540._CH', 'ED6_DT07/CH02540P._CP'),
        ('ED6_DT07/CH02030._CH', 'ED6_DT07/CH02030P._CP'),
        ('ED6_DT07/CH02460._CH', 'ED6_DT07/CH02460P._CP'),
        ('ED6_DT07/CH02230._CH', 'ED6_DT07/CH02230P._CP'),
        ('ED6_DT07/CH02240._CH', 'ED6_DT07/CH02240P._CP'),
        ('ED6_DT07/CH01330._CH', 'ED6_DT07/CH01330P._CP'),
        ('ED6_DT07/CH00177._CH', 'ED6_DT07/CH00177P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10002 offset: 0xF2
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
            dword_10            = 2,
            chipIndex           = 2,
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
            dword_10            = 6,
            chipIndex           = 6,
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
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 21430,
            z                   = 750,
            y                   = -3970,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 2750,
            z                   = 0,
            y                   = -26300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = -2980,
            z                   = 0,
            y                   = -26300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 2750,
            z                   = 0,
            y                   = -26300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000C,
        ),
        ScenaNpcData(
            x                   = -2980,
            z                   = 0,
            y                   = -26300,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000D,
        ),
    )

# id: 0x10003 offset: 0x232
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x232
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 4010,
            y           = 10000,
            z           = 16219,
            range       = -4330,
            dword_10    = 0x00001F40,
            dword_14    = 0x00002D78,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000008,
        ),
        ScenaEventData(
            x           = 21060,
            y           = -1000,
            z           = -1860,
            range       = 19780,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFE854,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000A,
        ),
        ScenaEventData(
            x           = 4290,
            y           = -1000,
            z           = -25590,
            range       = -4690,
            dword_10    = 0x000007D0,
            dword_14    = 0xFFFFA33A,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000B,
        ),
    )

# id: 0x10005 offset: 0x292
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x292
@scena.Code('PreInit')
def PreInit():
    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_2A2'),
        (0x0000006C, 'loc_2B8'),
        (-1, 'loc_2CE'),
    )

    def _loc_2A2(): pass

    label('loc_2A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 1, 0x639)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 0, 0x638)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2B5',
    )

    SetScenaFlags(ScenaFlag(0x00C7, 1, 0x639))
    Event(0, 0x0003)

    def _loc_2B5(): pass

    label('loc_2B5')

    Jump('loc_2CE')

    def _loc_2B8(): pass

    label('loc_2B8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 1, 0x641)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 0, 0x640)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2CB',
    )

    SetScenaFlags(ScenaFlag(0x00C8, 1, 0x641))
    Event(0, 0x0006)

    def _loc_2CB(): pass

    label('loc_2CB')

    Jump('loc_2CE')

    def _loc_2CE(): pass

    label('loc_2CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 2, 0x642)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2F8',
    )

    SetChrChipByIndex(0x0000, 3)
    SetChrChipByIndex(0x0001, 4)
    SetChrChipByIndex(0x0138, 5)
    SetChrFlags(0x0000, 0x1000)
    SetChrFlags(0x0001, 0x1000)
    SetChrFlags(0x0138, 0x1000)

    def _loc_2F8(): pass

    label('loc_2F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_31C',
    )

    SetChrFlags(0x000D, 0x0080)
    SetChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0010, 0x0080)

    def _loc_31C(): pass

    label('loc_31C')

    Return()

# id: 0x0001 offset: 0x31D
@scena.Code('Init')
def Init():
    OP_71(0x0000, 0x0002)

    ExecExpressionWithVar(
        0x2B,
        (
            (Expr.PushLong, 0xFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0002 offset: 0x32C
@scena.Code('ReInit')
def ReInit():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0x8),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_351',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_3E4')

    def _loc_351(): pass

    label('loc_351')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_36A',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_3E4')

    def _loc_36A(): pass

    label('loc_36A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_383',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_3E4')

    def _loc_383(): pass

    label('loc_383')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_39C',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_3E4')

    def _loc_39C(): pass

    label('loc_39C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3B5',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_3E4')

    def _loc_3B5(): pass

    label('loc_3B5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3CE',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_3E4')

    def _loc_3CE(): pass

    label('loc_3CE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3E4',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    def _loc_3E4(): pass

    label('loc_3E4')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3F9',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_3E4')

    def _loc_3F9(): pass

    label('loc_3F9')

    Return()

# id: 0x0003 offset: 0x3FA
@scena.Code('func_03_3FA')
def func_03_3FA():
    EventBegin(0x00)
    SetChrPos(0x0101, 520, 0, -22530, 0)
    SetChrPos(0x0102, -1610, 0, -22470, 0)
    SetChrPos(0x0108, -290, 0, -21870, 0)
    CameraMove(-210, 0, -19730, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(10000, 0)
    OP_6E(280, 0)

    @scena.Lambda('lambda_0472')
    def lambda_0472():
        CameraMove(180, 9000, 14710, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0472)

    @scena.Lambda('lambda_048A')
    def lambda_048A():
        OP_67(0, 4950, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_048A)

    @scena.Lambda('lambda_04A2')
    def lambda_04A2():
        CameraSetDistance(2190, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_04A2)

    @scena.Lambda('lambda_04B2')
    def lambda_04B2():
        OP_6C(45000, 12000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_04B2)

    @scena.Lambda('lambda_04C2')
    def lambda_04C2():
        OP_6E(899, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_04C2)

    FadeIn(2000, 0)
    Sleep(12000)

    Fade(1000)
    CameraMove(30, 0, -22200, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#000F哇～～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120052V#010F虽然是理所当然的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120053V这比至今为止见过的房间\n',
            '要豪华不知道多少倍呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F不只是豪华，\n',
            '还有蕴含历史和传统的壮丽。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '到处都有浓厚的\n',
            '古代王国的传统风格呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0008, 770, 0, -9870, 180)
    SetChrPos(0x0009, -280, 0, -9260, 180)

    ChrTalk(
        0x0008,
        (
            '欢迎来到格兰赛尔城。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0611100002V请问你们就是\n',
            '金先生一行人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0659')
    def lambda_0659():
        ChrWalkTo(0x00FE, -80, 0, -19430, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0659)

    @scena.Lambda('lambda_0674')
    def lambda_0674():
        ChrWalkTo(0x00FE, -850, 0, -18600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0674)

    CameraMove(130, 0, -20310, 3000)

    ChrTalk(
        0x0101,
        (
            '#000F（哎哎……是凯诺娜上尉……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（虽然也不是没有预料到……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120060V#070F啊，没错。\n',
            '我们受了公爵阁下的邀请。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120061V请问……你是？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#180F呵呵，忘了自我介绍。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120063V我是担任格兰赛尔城警卫工作的\n',
            '情报部的凯诺娜上尉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0611100003V恭喜金先生你们\n',
            '获得武术大会的优胜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120065V我看了你们的比赛，\n',
            '真是威风凛凛，令人叹为观止啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F哎呀～真是过奖了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120067V我倒觉得，您这样年轻和漂亮，\n',
            '担当军队的上尉真是让我吃惊呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120068V一定是非常优秀才能做到这样吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#180F哎呀……\n',
            '您真会说话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '哦，这两位不是\n',
            '年轻的游击士嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0610120073V#180F艾丝蒂尔·布莱特，\n',
            '以及约修亚·布莱特。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120074V蔡斯事件之后我们就没见过面吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F……嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120076V#010F确实很久不见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#180F虽然很遗憾，\n',
            '不过拉赛尔博士的事件\n',
            '还没有完全解决。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120078V博士和她的孙女\n',
            '好像被一伙暴徒绑架了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '所以就让\n',
            '有没有这方面的线索呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F那、那个。\n',
            '一点也不知道呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F那个事情交给了正游击士去处理，\n',
            '然后我们就来王都了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120082V之后的事情就没再听说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#180F是吗……呵呵。\n',
            '那真是遗憾呢',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120084V不过，只要借助情报部的力量，\n',
            '逮捕绑架犯也只是时间上的问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120085V就请你们瞧着吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F（这、这个狐狸精～……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我明白了，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120088V博士是我们的恩人，\n',
            '所以一定请你们救出他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#180F那是自然……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，就招待各位\n',
            '到你们的房间去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '#180F茜亚……\n',
            '接下来就交给你了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '好……\n',
            '我会好好照顾客人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#180F还有，请你注意……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120094V不要对客人没有礼貌，\n',
            '说些不该说的话。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120095V记住了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '好、好的……\n',
            '我明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#180F哼哼，这样就好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0102, 400)
    ChrTurnDirection(0x0008, 0x0108, 400)

    ChrTalk(
        0x0008,
        (
            '#180F那么各位，\n',
            '希望你们今晚过得愉快。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120099V我就此告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0D10')
    def lambda_0D10():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0D10')

    DispatchAsync2(0x0108, 0x0001, lambda_0D10)

    @scena.Lambda('lambda_0D21')
    def lambda_0D21():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0D21')

    DispatchAsync2(0x0101, 0x0001, lambda_0D21)

    @scena.Lambda('lambda_0D32')
    def lambda_0D32():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_0D32')

    DispatchAsync2(0x0102, 0x0001, lambda_0D32)

    ChrWalkTo(0x0008, 1840, 0, -15630, 2000, 0x00)

    @scena.Lambda('lambda_0D57')
    def lambda_0D57():
        ChrWalkTo(0x00FE, 7360, 0, -10100, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_0D57)

    Sleep(1500)

    ChrTalk(
        0x0108,
        (
            '#0081040015V#070F唔～这个女人真是不错啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F金先生，你的兴趣真是奇怪啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120102V那个狐狸精，\n',
            '有什么地方好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    ChrTurnDirection(0x0102, 0x0108, 400)

    ChrTalk(
        0x0102,
        (
            '#010F那样的人，\n',
            '是金先生喜欢的类型吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F哈哈，只有这样\n',
            '本质上才会纯情啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120105V就是这一点最吸引人了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0108, 400)

    ChrTalk(
        0x0101,
        (
            '#000F不行了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不管怎么样都好啦。\n',
            '金先生，你好像大叔一样呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0EC5')
    def lambda_0EC5():
        ChrTurnDirection(0x00FE, 0x0101, 800)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0EC5)

    ChrTalk(
        0x0108,
        (
            '#070F（受到打击）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0EEA')
    def lambda_0EEA():
        CameraMove(-240, 0, -20830, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0EEA)

    ChrWalkTo(0x0009, -260, 0, -20090, 1500, 0x00)
    ChrTurnDirection(0x0009, 0x0108, 400)

    ChrTalk(
        0x0009,
        (
            '那、那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0F2F')
    def lambda_0F2F():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0F2F)

    @scena.Lambda('lambda_0F3D')
    def lambda_0F3D():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0F3D)

    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#000F啊，抱歉抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120111V现在可以带我们\n',
            '去看看房间吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '好……\n',
            '我来带路吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '请允许我先自我介绍一下。\n',
            '我是这里的侍女，名叫茜亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '从晚宴开始到明天，\n',
            '由我来照顾你们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '如果有什么不便，\n',
            '随时可以告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120116V#070F啊，请多关照啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120117V#010F那么，\n',
            '现在带我们去房间吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '啊，好的。\n',
            '各位的房间在２楼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0009, 0x01, 0x00, 0x0004)
    Sleep(50)

    ChrWalkTo(0x0108, -240, 0, -20830, 3000, 0x00)
    OP_6A(0x0108)
    CreateThread(0x0108, 0x01, 0x00, 0x0004)
    Sleep(150)

    CreateThread(0x0102, 0x01, 0x00, 0x0004)
    Sleep(400)

    CreateThread(0x0101, 0x01, 0x00, 0x0004)
    Sleep(12000)

    OP_66(0x0000)
    WaitForThreadExit(0x0009, 0x0001)

    @scena.Lambda('lambda_10F4')
    def lambda_10F4():
        OP_6E(196, 3000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_10F4)

    @scena.Lambda('lambda_1104')
    def lambda_1104():
        ChrWalkTo(0x00FE, 50, 9000, 23150, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1104)

    WaitForThreadExit(0x0108, 0x0001)

    @scena.Lambda('lambda_1124')
    def lambda_1124():
        ChrWalkTo(0x00FE, 1040, 9000, 22000, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1124)

    WaitForThreadExit(0x0102, 0x0001)

    @scena.Lambda('lambda_1144')
    def lambda_1144():
        ChrWalkTo(0x00FE, -1130, 9000, 21070, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1144)

    WaitForThreadExit(0x0101, 0x0001)

    @scena.Lambda('lambda_1164')
    def lambda_1164():
        ChrWalkTo(0x00FE, -110, 9000, 20410, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1164)

    ChrTalk(
        0x0101,
        (
            '#000F哇～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那个巨大的吊灯，\n',
            '真是豪华绚丽呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_11B1')
    def lambda_11B1():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_11B1)

    ChrTalk(
        0x0102,
        (
            '#010F艾丝蒂尔，不要大声喧哗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对了，那边是……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_11F6')
    def lambda_11F6():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_11F6)

    @scena.Lambda('lambda_1204')
    def lambda_1204():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1204)

    @scena.Lambda('lambda_1212')
    def lambda_1212():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_1212)

    SetChrDirection(0x0009, 0, 400)

    ChrTalk(
        0x0009,
        (
            '是『谒见室』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '艾莉茜雅女王陛下\n',
            '就是在这里会见客人的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过最近一直没有用过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1286')
    def lambda_1286():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1286)

    @scena.Lambda('lambda_1294')
    def lambda_1294():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1294)

    ChrTurnDirection(0x0102, 0x0009, 400)

    ChrTalk(
        0x0102,
        (
            '#010F……是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F说起来，女王陛下的病情\n',
            '有那么严重吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120128V不是就要举行生日庆典了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearMapFlags(0x00000001)
    OP_69(0x0102, 1000)
    OP_6A(0x0102)
    ChrTurnDirection(0x0009, 0x0108, 400)

    ChrTalk(
        0x0009,
        (
            '不、不是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '最近照顾陛下的，\n',
            '是这里的女官长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '所以，我不太清楚\n',
            '具体的情况……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 0)

    ChrTalk(
        0x0009,
        (
            '真、真是不好意思……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_66(0x0001)
    CreateThread(0x0009, 0x01, 0x00, 0x0005)
    Sleep(420)

    CreateThread(0x0102, 0x01, 0x00, 0x0005)
    Sleep(150)

    CreateThread(0x0101, 0x01, 0x00, 0x0005)
    Sleep(400)

    CreateThread(0x0108, 0x01, 0x00, 0x0005)
    Sleep(3000)

    OP_28(0x0049, 0x01, 0x0080)
    OP_28(0x0049, 0x01, 0x0100)
    OP_28(0x0049, 0x01, 0x0200)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4222._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0004 offset: 0x13F6
@scena.Code('func_04_13F6')
def func_04_13F6():
    ChrWalkTo(0x00FE, -1210, 0, -15560, 3000, 0x01)
    ChrWalkTo(0x00FE, -1860, 0, -14700, 3000, 0x01)
    ChrWalkTo(0x00FE, -3820, 0, -12520, 3000, 0x01)
    ChrWalkTo(0x00FE, -8080, 0, -10300, 3000, 0x01)
    ChrWalkTo(0x00FE, -8080, 0, -10300, 3000, 0x01)
    ChrWalkTo(0x00FE, -12960, 0, -9190, 3000, 0x01)
    ChrWalkTo(0x00FE, -15420, 0, -7110, 3000, 0x01)
    ChrWalkTo(0x00FE, -17480, 0, -520, 3000, 0x01)
    ChrWalkTo(0x00FE, -17190, 1250, 3150, 3000, 0x01)
    ChrWalkTo(0x00FE, -16219, 2500, 5730, 3000, 0x01)
    ChrWalkTo(0x00FE, -15090, 3500, 7960, 3000, 0x01)
    ChrWalkTo(0x00FE, -13020, 5000, 10640, 3000, 0x01)
    ChrWalkTo(0x00FE, -10430, 6250, 12400, 3000, 0x01)
    ChrWalkTo(0x00FE, -8180, 7250, 13350, 3000, 0x01)
    ChrWalkTo(0x00FE, -5780, 8250, 13950, 3000, 0x01)
    ChrWalkTo(0x00FE, -2210, 9000, 14440, 3000, 0x01)
    ChrWalkTo(0x00FE, -1160, 9000, 14880, 3000, 0x01)
    ChrWalkTo(0x00FE, -430, 9000, 15810, 3000, 0x01)
    ChrWalkTo(0x00FE, 20, 9000, 17590, 3000, 0x01)

    Return()

# id: 0x0005 offset: 0x1573
@scena.Code('func_05_1573')
def func_05_1573():
    SetChrFlags(0x00FE, 0x0040)
    ChrWalkTo(0x00FE, -3610, 9000, 24020, 3000, 0x01)
    ChrWalkTo(0x00FE, -7960, 9000, 25860, 3000, 0x01)
    ChrWalkTo(0x00FE, -9570, 9000, 26050, 3000, 0x01)

    @scena.Lambda('lambda_15BA')
    def lambda_15BA():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_15BA)

    ChrWalkTo(0x00FE, -12900, 9000, 26050, 3000, 0x01)

    Return()

# id: 0x0006 offset: 0x15DB
@scena.Code('func_06_15DB')
def func_06_15DB():
    EventBegin(0x00)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x000A, -6640, 8000, 13770, 80)
    SetChrPos(0x0008, -7900, 7500, 13100, 62)
    SetChrPos(0x0101, -7920, 9000, 24630, 118)
    SetChrPos(0x0102, -7520, 9000, 25920, 118)

    ChrTalk(
        0x000A,
        (
            '#110F哦，是你们俩啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1661')
    def lambda_1661():
        CameraMove(-3860, 9000, 20630, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1661)

    Sleep(1000)

    @scena.Lambda('lambda_167E')
    def lambda_167E():
        ChrWalkTo(0x00FE, -2029, 9000, 14880, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_167E)

    @scena.Lambda('lambda_1699')
    def lambda_1699():
        ChrWalkTo(0x00FE, -2260, 9000, 13770, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1699)

    WaitForThreadExit(0x000A, 0x0001)

    @scena.Lambda('lambda_16B9')
    def lambda_16B9():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_16B9)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_16CC')
    def lambda_16CC():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_16CC)

    @scena.Lambda('lambda_16DA')
    def lambda_16DA():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_16DA')

    DispatchAsync2(0x0101, 0x0001, lambda_16DA)

    @scena.Lambda('lambda_16EB')
    def lambda_16EB():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_16EB')

    DispatchAsync2(0x0102, 0x0001, lambda_16EB)

    ChrTalk(
        0x0102,
        (
            '#010F理查德上校……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1715')
    def lambda_1715():
        CameraMove(-7040, 9000, 25530, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1715)

    CreateThread(0x000A, 0x01, 0x00, 0x0007)
    Sleep(300)

    CreateThread(0x0008, 0x01, 0x00, 0x0007)
    WaitForThreadExit(0x000A, 0x0001)

    @scena.Lambda('lambda_1745')
    def lambda_1745():
        SetChrDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_1745')

    DispatchAsync2(0x000A, 0x0001, lambda_1745)

    @scena.Lambda('lambda_1756')
    def lambda_1756():
        ChrWalkTo(0x00FE, -6280, 9000, 25380, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0002, lambda_1756)

    WaitForThreadExit(0x0008, 0x0001)

    @scena.Lambda('lambda_1776')
    def lambda_1776():
        SetChrDirection(0x00FE, 270, 0)
        Yield()

        Jump('lambda_1776')

    DispatchAsync2(0x0008, 0x0001, lambda_1776)

    WaitForThreadExit(0x000A, 0x0002)

    ChrTalk(
        0x000A,
        (
            '#110F呵呵……\n',
            '是艾丝蒂尔和约修亚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0131090001V我们像这样面对面\n',
            '的对话已经不是第一次了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120816V#010F我们最后一次对话是在\n',
            '戴尔蒙市长被捕之后。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020120817V不过没有想到上校您\n',
            '还能记起我们来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#110F虽然对话的机会很少，\n',
            '不过你们给我留下了很深的印象。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120819V因此我调查了一下，结果让我大吃一惊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0131090002V没有想到你们竟然是\n',
            '卡西乌斯上校的孩子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#000F这、这件事也知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#110F哈哈，情报部\n',
            '可不是浪得虚名的哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……卡西乌斯上校当年\n',
            '在军中时曾给予我许多照料。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120824V正因如此……\n',
            '言语实在难表我的谢意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#110F怎么样，我们去稍微\n',
            '谈谈如何呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120827V我之前就一直想\n',
            '和你们私下谈谈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x000A, 400)

    ChrTalk(
        0x0008,
        (
            '#180F对、对不起，上校……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610120831V不是要去和公爵大人\n',
            '商量相关事宜的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#110F稍微迟一点也没关系的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对了，要谈谈的话，\n',
            '就借里面的谈话室一用吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120834V我只是请你们喝一些\n',
            '不带酒精的鸡尾酒而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#180F只、只是这样的话，\n',
            '就让我来吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000A, 0x0008, 400)

    ChrTalk(
        0x000A,
        (
            '#110F不，这与你无关。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120837V你到公爵那里去，\n',
            '把我要迟到一会儿的消息告诉他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#180F明、明白了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1BEF')
    def lambda_1BEF():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1BEF')

    DispatchAsync2(0x000A, 0x0001, lambda_1BEF)

    @scena.Lambda('lambda_1C00')
    def lambda_1C00():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1C00')

    DispatchAsync2(0x0101, 0x0001, lambda_1C00)

    @scena.Lambda('lambda_1C11')
    def lambda_1C11():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_1C11')

    DispatchAsync2(0x0102, 0x0001, lambda_1C11)

    OP_62(0x0008, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    ChrTurnDirection(0x0008, 0x0101, 800)

    ChrTalk(
        0x0008,
        (
            '#180F…………………（怒视）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F（我好怕怕……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#180F……那么我就先告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, -150, 9000, 28360, 3000, 0x00)

    @scena.Lambda('lambda_1CB1')
    def lambda_1CB1():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 1000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1CB1)

    ChrWalkTo(0x0008, -70, 9000, 33280, 3000, 0x00)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    SetChrDirection(0x000A, 270, 400)

    @scena.Lambda('lambda_1CEA')
    def lambda_1CEA():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_1CEA')

    DispatchAsync2(0x0101, 0x0001, lambda_1CEA)

    @scena.Lambda('lambda_1CFB')
    def lambda_1CFB():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_1CFB')

    DispatchAsync2(0x0102, 0x0001, lambda_1CFB)

    ChrTalk(
        0x000A,
        (
            '#110F我们这就到\n',
            '谈话室去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0130120843V请跟我来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1D41')
    def lambda_1D41():
        ChrWalkTo(0x00FE, 9130, 9000, 25780, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1D41)

    Sleep(300)

    CameraMove(-5680, 9000, 25260, 2000)

    ChrTalk(
        0x0101,
        (
            '#000F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我说约修亚啊，怎么办好呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F只有先奉陪一下了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽说会有些迟，\n',
            '但只有稍后才去夫人那里了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x004A, 0x01, 0x0008)
    OP_28(0x004A, 0x01, 0x0010)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4221._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x1DFC
@scena.Code('func_07_1DFC')
def func_07_1DFC():
    ChrWalkTo(0x00FE, -1800, 9000, 20840, 3000, 0x00)
    ChrWalkTo(0x00FE, -4740, 9000, 23780, 3000, 0x00)

    Return()

# id: 0x0008 offset: 0x1E25
@scena.Code('func_08_1E25')
def func_08_1E25():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 7, 0x647)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C8, 6, 0x646)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_1E32',
    )

    Return()

    def _loc_1E32(): pass

    label('loc_1E32')

    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x00C8, 7, 0x647))
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    SetChrPos(0x0008, -70, 9000, 27870, 180)
    SetChrPos(0x000B, -800, 9000, 28970, 180)
    SetChrPos(0x000C, 530, 9000, 28970, 180)

    ChrTalk(
        0x0008,
        (
            '……这种时候\n',
            '还在那儿做什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_1ED2')
    def lambda_1ED2():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1ED2)

    @scena.Lambda('lambda_1EE0')
    def lambda_1EE0():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1EE0)

    CameraMove(10, 9000, 27580, 3000)
    FormationAddMember(0x07, 0xFF)
    SetChrPos(0x0101, -550, 9000, 16309, 0)
    SetChrPos(0x0102, 670, 9000, 16190, 0)
    SetChrPos(0x0108, 6350, 9000, 24020, 225)
    SetChrFlags(0x0108, 0x0080)

    @scena.Lambda('lambda_1F3A')
    def lambda_1F3A():
        ChrWalkTo(0x00FE, 140, 9000, 19940, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1F3A)

    @scena.Lambda('lambda_1F55')
    def lambda_1F55():
        ChrWalkTo(0x00FE, -580, 9000, 21140, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1F55)

    @scena.Lambda('lambda_1F70')
    def lambda_1F70():
        ChrWalkTo(0x00FE, 830, 9000, 21150, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_1F70)

    CameraMove(100, 9000, 18910, 3000)

    ChrTalk(
        0x0101,
        (
            '#000F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F凯诺娜上尉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0008, 0x0001)

    ChrTalk(
        0x0008,
        (
            '#180F哼哼哼，晚上好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121483V怎么说你们也是贵宾，\n',
            '我还是对你们比较客气的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121484V可要说是孩子晚上出去散步\n',
            '不觉得也太迟了一些吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F很抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121486V因为看见城里有许多新奇的东西，\n',
            '所以稍微迟了一些……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#180F哎呀，倒是个不错的选择呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121488V那么你们３０分钟之前\n',
            '在哪里参观呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121489V能不能告诉我，　\n',
            '让我做个参考呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
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

    Menu(
        0,
        10,
        10,
        0,
        (
            TXT(0x00, '厨房\n'),
            TXT(0x01, '侍女休息室\n'),
            TXT(0x02, '行政区域\n'),
            TXT(0x03, '亲卫队值勤室\n'),
            TXT(0x04, '地下仓库\n'),
        ),
    )

    MenuEnd(0x0000)
    OP_5F(0x0000)

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_56(0x00)
    FadeIn(300, 0)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_21B7'),
        (0x00000001, 'loc_2227'),
        (0x00000002, 'loc_2250'),
        (0x00000003, 'loc_22CB'),
        (0x00000004, 'loc_2364'),
        (-1, 'loc_23C3'),
    )

    def _loc_21B7(): pass

    label('loc_21B7')

    ChrTalk(
        0x0008,
        (
            '#0610121491V#180F哎呀，很可疑呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121492V刚才我去巡视的时候\n',
            '怎么没有看见你们呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F这、这个嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23C3')

    def _loc_2227(): pass

    label('loc_2227')

    ChrTalk(
        0x0008,
        (
            '#180F呵呵……\n',
            '真是老实的孩子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23C3')

    def _loc_2250(): pass

    label('loc_2250')

    ChrTalk(
        0x0008,
        (
            '#0610121501V#180F行政区域的值班人\n',
            '早就已经回去了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0611100004V你们在那种地方，\n',
            '到底干了些什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F这、这个嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23C3')

    def _loc_22CB(): pass

    label('loc_22CB')

    ChrTalk(
        0x0008,
        (
            '#0610121507V那真是奇怪了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121508V那里现在正作为我们\n',
            '情报部的办公室使用……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121509V自从看到你们在\n',
            '不可能让你们进去参观的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F这、这个嘛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23C3')

    def _loc_2364(): pass

    label('loc_2364')

    ChrTalk(
        0x0008,
        (
            '什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121515V你们去那种地方\n',
            '到底干了些什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F没、没有\n',
            '干什么事情啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_23C3')

    def _loc_23C3(): pass

    label('loc_23C3')

    ChrTalk(
        0x0008,
        (
            '#0611100005V#180F算了，我不准备\n',
            '再和你们兜圈子了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0611100006V事实上我已经收到了报告，\n',
            '发现你们俩曾屡次在\n',
            '侍女休息室进进出出。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121496V在那样的地方去参观，\n',
            '难道一点都不可疑吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F什么……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F你明知故问，\n',
            '人品也太差了一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#180F哼哼哼，我收下\n',
            '你的赞美之词。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121523V说吧，到侍女休息室\n',
            '做什么去了啊？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121524V老老实实回答对你们有好处哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '喂～！\n',
            '艾丝蒂尔、约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '原来你们还呆在那里啊～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0108, 0x0080)

    @scena.Lambda('lambda_2584')
    def lambda_2584():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2584)

    @scena.Lambda('lambda_2592')
    def lambda_2592():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2592)

    @scena.Lambda('lambda_25A0')
    def lambda_25A0():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_25A0)

    @scena.Lambda('lambda_25AE')
    def lambda_25AE():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_25AE)

    @scena.Lambda('lambda_25BC')
    def lambda_25BC():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_25BC)

    CameraMove(3230, 9000, 20920, 2000)

    @scena.Lambda('lambda_25DB')
    def lambda_25DB():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_25DB')

    DispatchAsync2(0x0101, 0x0001, lambda_25DB)

    @scena.Lambda('lambda_25EC')
    def lambda_25EC():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_25EC')

    DispatchAsync2(0x0102, 0x0001, lambda_25EC)

    @scena.Lambda('lambda_25FD')
    def lambda_25FD():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_25FD')

    DispatchAsync2(0x0008, 0x0001, lambda_25FD)

    @scena.Lambda('lambda_260E')
    def lambda_260E():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_260E')

    DispatchAsync2(0x000B, 0x0001, lambda_260E)

    @scena.Lambda('lambda_261F')
    def lambda_261F():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_261F')

    DispatchAsync2(0x000C, 0x0001, lambda_261F)

    ChrTalk(
        0x0102,
        (
            '#0020140698V#010F金大哥……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_264C')
    def lambda_264C():
        CameraMove(900, 9000, 19490, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_264C)

    @scena.Lambda('lambda_2664')
    def lambda_2664():
        OP_6E(256, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2664)

    @scena.Lambda('lambda_2674')
    def lambda_2674():
        OP_9E(0x00FE, 60, 0, 5000, 700)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_2674)

    ChrWalkTo(0x0108, 1880, 9000, 19250, 2000, 0x00)
    SetChrChipByIndex(0x0108, 7)
    OP_99(0x0108, 0x00, 0x07, 2000)

    ChrTalk(
        0x0101,
        (
            '#000F哇，酩酊大醉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0108,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0108, 65535)
    ChrTurnDirection(0x0108, 0x0008, 400)

    ChrTalk(
        0x0108,
        (
            '#070F哦哟，抱歉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121532V我说是和谁在那儿呢，\n',
            '原来是和美女军官在一起啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0081040016V哎呀啊～怎么说都\n',
            '是美妙的偶然相遇啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#180F是、是啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F你看怎么样？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121536V我那不成熟的徒弟给您\n',
            '添了不少麻烦吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F徒、徒弟……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#180F没有，不过刚才他们竟然\n',
            '呆在侍女休息室里面……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121539V出于保卫这里安全的理由，\n',
            '我问问他们在里面做什么。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0108, 0x0102, 400)

    ChrTalk(
        0x0108,
        (
            '#070F哦，那个是这么回事的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '下酒的菜都没有了，\n',
            '所以我叫他们去取一些来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '喂，约修亚，\n',
            '还有什么可以吃的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121543V#010F没有了，厨师他们好像\n',
            '已经回去休息了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020121544V我又问了侍女她们，\n',
            '虽然她们去找了一下，\n',
            '但下酒菜是的确没有了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F呼，没办法啦。\n',
            '没有下酒菜就只有忍了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0108, 0x00000000, 2300, 0x22, 0x24, 0x000000FA, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x0108, 0x0008, 400)
    Sleep(1000)

    ChrTalk(
        0x0108,
        (
            '#070F呀……\n',
            '我想到了一个好办法！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_29B7')
    def lambda_29B7():
        OP_9E(0x00FE, 100, 0, 3000, 300)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_29B7)

    OP_92(0x0108, 0x0008, 600, 1000, 0x00)

    ChrTalk(
        0x0108,
        (
            '#070F你不介意的话\n',
            '陪我喝喝酒如何呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080121548V哇哈哈，美人的笑脸\n',
            '是最好的下酒佳肴啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_94(0x01, 0x0008, 0x00B4, 0x00000258, 0x00000BB8, 0x00)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#180F我、我还有任务在身，\n',
            '恕不奉陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0xFF)
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '#180F刚才的那件事\n',
            '先姑且不问……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121551V你们现在就回房间去，\n',
            '今晚不准再出来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0610121552V如果再发现你们的可疑行动，\n',
            '我会保留调查权利的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0008, 0xFF)
    TerminateThread(0x000B, 0xFF)
    TerminateThread(0x000C, 0xFF)

    @scena.Lambda('lambda_2B36')
    def lambda_2B36():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2B36')

    DispatchAsync2(0x0101, 0x0001, lambda_2B36)

    @scena.Lambda('lambda_2B47')
    def lambda_2B47():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2B47')

    DispatchAsync2(0x0102, 0x0001, lambda_2B47)

    @scena.Lambda('lambda_2B58')
    def lambda_2B58():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2B58')

    DispatchAsync2(0x0108, 0x0001, lambda_2B58)

    ChrTalk(
        0x0101,
        (
            '#000F知、知道了还不行吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F已经很晚了，\n',
            '也应该休息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#180F哼哼，老实点好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么……\n',
            '我们这就告辞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CreateThread(0x0008, 0x01, 0x00, 0x0009)
    Sleep(500)

    CreateThread(0x000B, 0x01, 0x00, 0x0009)
    Sleep(500)

    CreateThread(0x000C, 0x01, 0x00, 0x0009)
    CameraMove(710, 9000, 17230, 3000)
    Sleep(500)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)

    ChrTalk(
        0x0108,
        (
            '#070F哎呀，这就走掉了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '没办法了……\n',
            '我回房间去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯、嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020121560V#010F我们也一起回去了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4222._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x2CA3
@scena.Code('func_09_2CA3')
def func_09_2CA3():
    ChrWalkTo(0x00FE, -1600, 9000, 19000, 3000, 0x00)
    ChrWalkTo(0x00FE, -1600, 9000, 15470, 3000, 0x00)
    ChrWalkTo(0x00FE, 100, 9000, 14170, 3000, 0x00)
    ChrWalkTo(0x00FE, 4320, 9000, 14170, 3000, 0x00)
    ChrWalkTo(0x00FE, 8280, 7250, 13480, 3000, 0x00)
    ChrWalkTo(0x00FE, 13650, 4500, 9700, 3000, 0x00)

    Return()

# id: 0x000A offset: 0x2D1C
@scena.Code('func_0A_2D1C')
def func_0A_2D1C():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CC, 0, 0x660)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2E62',
    )

    EventBegin(0x01)
    OP_4A(0x000D, 255)

    If(
        (
            (Expr.Eval, "OP_42(0x0037)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2DD9',
    )

    ChrTurnDirection(0x000D, 0x0000, 400)

    ChrTalk(
        0x000D,
        (
            '#4340120509V哎呀呀，这不是希尔丹夫人吗……\n',
            '到我们这儿来有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#4340120510V这里是情报部的值勤室。\n',
            '请不要随随便便靠近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    SetChrDirection(0x000D, 270, 0)

    Jump('loc_2E57')

    def _loc_2DD9(): pass

    label('loc_2DD9')

    ChrTurnDirection(0x000D, 0x0000, 400)

    ChrTalk(
        0x000D,
        (
            '#4340120511V这里是情报部的值勤室。\n',
            '平民禁止入内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#4340120512V不想被逮捕的话，\n',
            '就不要靠近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, -1500, 0, 0, 3000, 0x00)
    SetChrDirection(0x000D, 270, 0)

    def _loc_2E57(): pass

    label('loc_2E57')

    OP_4B(0x000D, 255)
    Sleep(50)

    EventEnd(0x04)

    def _loc_2E62(): pass

    label('loc_2E62')

    Return()

# id: 0x000B offset: 0x2E63
@scena.Code('func_0B_2E63')
def func_0B_2E63():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2E70',
    )

    Return()

    def _loc_2E70(): pass

    label('loc_2E70')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 7, 0x66F)),
            Expr.Return,
        ),
        'loc_2F0C',
    )

    EventBegin(0x01)
    OP_4A(0x0010, 255)
    OP_4A(0x0011, 255)

    ChrTalk(
        0x0011,
        (
            '#4200120190V哦？有什么事吗？\n',
            '现在不能打开城门。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#4200120191V很抱歉，\n',
            '你们请在城内好好放松吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    SetChrDirection(0x0010, 0, 0)
    SetChrDirection(0x0011, 0, 0)
    OP_4B(0x0010, 255)
    OP_4B(0x0011, 255)

    Jump('loc_3096')

    def _loc_2F0C(): pass

    label('loc_2F0C')

    EventBegin(0x01)
    OP_4A(0x000E, 255)
    OP_4A(0x000F, 255)

    If(
        (
            (Expr.Eval, "OP_42(0x0037)"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_2FD8',
    )

    ChrTurnDirection(0x000E, 0x0000, 400)
    ChrTurnDirection(0x000F, 0x0000, 400)

    ChrTalk(
        0x000E,
        (
            '#4320120192V哦，希尔丹夫人。都这么晚了还要外出吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#4330120193V您也是知道的，出于安全考虑，\n',
            '现在城门的开闭受到限制。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#4330120194V没有得到许可\n',
            '是不能从这里通行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_306C')

    def _loc_2FD8(): pass

    label('loc_2FD8')

    ChrTurnDirection(0x000E, 0x0000, 400)
    ChrTurnDirection(0x000F, 0x0000, 400)

    ChrTalk(
        0x000F,
        (
            '#4330120195V出于安全考虑，\n',
            '现在城门的开闭受到限制。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#4320120196V请在王城内\n',
            '随便活动吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '#4320120197V你们应该不会觉得\n',
            '有什么不自由吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_306C(): pass

    label('loc_306C')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    SetChrDirection(0x000E, 0, 0)
    SetChrDirection(0x000F, 0, 0)
    OP_4B(0x000E, 255)
    OP_4B(0x000F, 255)

    def _loc_3096(): pass

    label('loc_3096')

    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x000C offset: 0x309E
@scena.Code('func_0C_309E')
def func_0C_309E():
    TalkBegin(0x00FE)

    ChrTalk(
        0x0010,
        (
            '哎呀～\n',
            '感觉就像回到自己的家里一样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '王城的警备\n',
            '还是应该由我们正规军来担当。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x000D offset: 0x30FB
@scena.Code('func_0D_30FB')
def func_0D_30FB():
    TalkBegin(0x00FE)

    ChrTalk(
        0x0011,
        (
            '那位理查德上校\n',
            '竟然是政变的主谋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '作为王国军一员的我，\n',
            '委实感觉心情难以言表。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
