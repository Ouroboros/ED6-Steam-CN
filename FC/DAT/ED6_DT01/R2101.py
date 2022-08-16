import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import R2101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('R2101   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'R2101.x'
    header.mapIndex       = 100
    header.bgm            = 20
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
            word_3A         = 100,
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
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT09/CH10160._CH', 'ED6_DT09/CH10160P._CP'),
        ('ED6_DT09/CH10161._CH', 'ED6_DT09/CH10161P._CP'),
        ('ED6_DT09/CH10450._CH', 'ED6_DT09/CH10450P._CP'),
        ('ED6_DT09/CH10451._CH', 'ED6_DT09/CH10451P._CP'),
        ('ED6_DT09/CH10220._CH', 'ED6_DT09/CH10220P._CP'),
        ('ED6_DT09/CH10221._CH', 'ED6_DT09/CH10221P._CP'),
    ]

# id: 0x10001 offset: 0xE2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '基库',
            x                   = 800,
            z                   = 6130,
            y                   = -13810,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '玛诺利亚村方向',
            x                   = 13030,
            z                   = -2070,
            y                   = -137400,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '巴伦诺灯塔方向',
            x                   = -72540,
            z                   = -1880,
            y                   = -134520,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '古罗尼山道方向',
            x                   = -18980,
            z                   = -2000,
            y                   = 6950,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x00FF,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10002 offset: 0x162
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
        ScenaMonsterData(
            name        = '',
            x           = -9560,
            z           = -2080,
            y           = -65670,
            word_0C     = 0x00B4,
            word_0E     = 0x0003,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x016C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = 6390,
            z           = -2020,
            y           = -101440,
            word_0C     = 0x00B4,
            word_0E     = 0x0003,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x016C,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -41930,
            z           = -1980,
            y           = -61650,
            word_0C     = 0x00B4,
            word_0E     = 0x0001,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x016E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
        ScenaMonsterData(
            name        = '',
            x           = -75520,
            z           = -1990,
            y           = -83680,
            word_0C     = 0x00B4,
            word_0E     = 0x0001,
            byte_10     = 0x01,
            byte_11     = 0x01,
            dword_12    = 0xFFFFFFFF,
            battleIndex = 0x016E,
            word_18     = 0x0000,
            word_1A     = 0x0000,
        ),
    )

# id: 0x10003 offset: 0x1D2
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -16740,
            y           = -3000,
            z           = -43910,
            range       = 3000,
            dword_10    = 0x00002710,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000003,
        ),
        ScenaEventData(
            x           = -22290,
            y           = -3000,
            z           = -15520,
            range       = -16120,
            dword_10    = 0x00000000,
            dword_14    = 0xFFFFCFEA,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000005,
        ),
        ScenaEventData(
            x           = -80580,
            y           = -3000,
            z           = -110630,
            range       = -67150,
            dword_10    = 0x000003E8,
            dword_14    = 0xFFFE4666,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000007,
        ),
    )

# id: 0x10004 offset: 0x232
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -16670,
            triggerZ            = -1970,
            triggerY            = -43720,
            triggerRange        = 1500,
            actorX              = -16670,
            actorZ              = -300,
            actorY              = -43720,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = -20680,
            triggerZ            = -2009,
            triggerY            = -44860,
            triggerRange        = 1500,
            actorX              = -20680,
            actorZ              = -350,
            actorY              = -44860,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x27A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_291',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_02_2FB)

    def _loc_291(): pass

    label('loc_291')

    Return()

# id: 0x0001 offset: 0x292
@scena.Code('func_01_292')
def func_01_292():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 7, 0x437)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 6, 0x436)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2B4',
    )

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -16940, -1000, -44310, 135)

    def _loc_2B4(): pass

    label('loc_2B4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 6, 0x436)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2D2',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_77(0x41, 0x64, 0x82, 0x00, 0x00000000)

    def _loc_2D2(): pass

    label('loc_2D2')

    OP_16(0x02, 4000, -151000, -195000, 196652)
    PlaySE(452, 0x01, 0x64)

    ExecExpressionWithValue(
        0x0008,
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

# id: 0x0002 offset: 0x2FB
@scena.Code('func_02_2FB')
def func_02_2FB():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    CameraMove(10562, -2000, -118830, 0)
    OP_6C(270000, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, 14150, 1000, -123720, 0)
    ChrSetPos(0x0101, 13220, -2000, -128560, 0)
    ChrSetPos(0x0102, 13220, -2000, -128560, 0)
    ChrSetPos(0x0105, 13220, -2000, -128560, 0)
    ChrSetPos(0x0106, 13220, -2000, -128560, 0)

    @scena.Lambda('lambda_037C')
    def lambda_037C():
        OP_6C(315000, 3000)

        ExitThread()

    DispatchAsync(0x0105, 0x0003, lambda_037C)

    @scena.Lambda('lambda_038C')
    def lambda_038C():
        ChrWalkTo(0x00FE, 11270, 3000, -101560, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_038C)

    Sleep(1000)

    @scena.Lambda('lambda_03AC')
    def lambda_03AC():
        ChrWalkTo(0x00FE, 13130, -2009, -118750, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_03AC)

    Sleep(500)

    @scena.Lambda('lambda_03CC')
    def lambda_03CC():
        ChrWalkTo(0x00FE, 12380, -1930, -119890, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_03CC)

    Sleep(500)

    @scena.Lambda('lambda_03EC')
    def lambda_03EC():
        ChrWalkTo(0x00FE, 13890, -2040, -119820, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_03EC)

    Sleep(500)

    @scena.Lambda('lambda_040C')
    def lambda_040C():
        ChrWalkTo(0x00FE, 12950, -2009, -120790, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_040C)

    WaitForThreadExit(0x0106, 0x0001)

    ChrTalk(
        0x0106,
        (
            '#0050061126V#052F好像真的是在给我们引路啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061127V喂，小姑娘。\n',
            '开玩笑的话还是就此打住吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0494')
    def lambda_0494():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0494)

    @scena.Lambda('lambda_04A2')
    def lambda_04A2():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_04A2)

    ChrTurnDirection(0x0105, 0x0106, 400)

    ChrTalk(
        0x0105,
        (
            '#0060061128V#049F#2P我不是在开玩笑。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061129V因为老师和孩子们\n',
            '就像我的家人一样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050061130V#050F嘁……算了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061131V大不了\n',
            '就让你骗一次吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061132V#007F#1P你也真是的。\n',
            '一点都不老实。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020061133V#012F#4P先别说了，\n',
            '我们快点跟着基库走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x0008, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x5D5
@scena.Code('func_03_5D5')
def func_03_5D5():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 7, 0x437)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 6, 0x436)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_775',
    )

    MapClearFlags(0x00000001)
    EventBegin(0x00)
    SetScenaFlags(ScenaFlag(0x0086, 7, 0x437))
    OP_28(0x003E, 0x01, 0x0010)

    @scena.Lambda('lambda_05F7')
    def lambda_05F7():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_05F7)

    @scena.Lambda('lambda_0605')
    def lambda_0605():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0605)

    @scena.Lambda('lambda_0613')
    def lambda_0613():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_0613)

    @scena.Lambda('lambda_0621')
    def lambda_0621():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_0621)

    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0008, -17250, 2000, -38520, 315)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '此时能听到基库的声音。＃',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    @scena.Lambda('lambda_068C')
    def lambda_068C():
        CameraMove(-16010, 2000, -39760, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_068C)

    @scena.Lambda('lambda_06A4')
    def lambda_06A4():
        OP_6C(225000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_06A4)

    OP_97(0x0008, -16030, -39740, -360000, 8000, 0x0001)
    OP_97(0x0008, -16030, -39740, -360000, 8000, 0x0001)
    OP_97(0x0008, -16030, -39740, -360000, 8000, 0x0001)

    @scena.Lambda('lambda_06F3')
    def lambda_06F3():
        ChrWalkTo(0x0008, -33520, 5000, -56870, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_06F3)

    Sleep(2000)

    OP_69(0x0001, 2000)

    ChrTalk(
        0x0101,
        (
            '#0010061134V#004F那边不就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020061135V#012F嗯……\n',
            '总之先过去看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x01)
    ChrSetFlags(0x0008, 0x0080)
    MapClearFlags(0x02000000)

    def _loc_775(): pass

    label('loc_775')

    Return()

# id: 0x0004 offset: 0x776
@scena.Code('func_04_776')
def func_04_776():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_798',
    )

    OP_97(0x0008, -16940, -44310, -60000, 9000, 0x0001)
    Yield()

    Jump('func_04_776')

    def _loc_798(): pass

    label('loc_798')

    Return()

# id: 0x0005 offset: 0x799
@scena.Code('func_05_799')
def func_05_799():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0086, 6, 0x436)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 0, 0x438)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_90F',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_83C',
    )

    ChrTalk(
        0x0106,
        (
            '#0050061136V#050F没有绕远路的时间了……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061137V嘁，没办法了。\n',
            '虽然觉得像被捉弄了一样，\n',
            '不过现在也只有赌在那个基库上了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_908')

    def _loc_83C(): pass

    label('loc_83C')

    ChrTurnDirection(0x0106, 0x0000, 400)

    ChrTalk(
        0x0106,
        (
            '#0050061138V#050F喂，你们去哪儿。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061139V现在可没有绕远路的时间啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_089B')
    def lambda_089B():
        ChrTurnDirection(0x0105, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0105, 0x0001, lambda_089B)

    @scena.Lambda('lambda_08A9')
    def lambda_08A9():
        ChrTurnDirection(0x0101, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_08A9)

    ChrTurnDirection(0x0102, 0x0106, 400)

    ChrTalk(
        0x0102,
        (
            '#0020061140V#012F是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061141V现在只能相信基库，\n',
            '跟在它后面追踪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_908(): pass

    label('loc_908')

    Call(0, 0x0006)

    Jump('loc_9EB')

    def _loc_90F(): pass

    label('loc_90F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 0, 0x438)),
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 4, 0x43C)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_9EB',
    )

    EventBegin(0x02)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_990',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    ChrTalk(
        0x0106,
        (
            '#0050061142V#050F没有绕远路的时间了……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061143V赶快回灯塔去把这件事搞定吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9E7')

    def _loc_990(): pass

    label('loc_990')

    ChrTurnDirection(0x0106, 0x0000, 400)

    ChrTalk(
        0x0106,
        (
            '#0050061144V#050F喂喂，\n',
            '你们打算去散步吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050061145V……赶快回灯塔吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9E7(): pass

    label('loc_9E7')

    Call(0, 0x0006)

    def _loc_9EB(): pass

    label('loc_9EB')

    Return()

# id: 0x0006 offset: 0x9EC
@scena.Code('func_06_9EC')
def func_06_9EC():
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0007 offset: 0xA08
@scena.Code('func_07_A08')
def func_07_A08():
    If(
        (
            (Expr.Eval, "OP_42(0x0036)"),
            (Expr.PushLong, 0x0),
            Expr.Geq,
            (Expr.Eval, "OP_29(0x001F, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_AAB',
    )

    EventBegin(0x01)
    ChrTurnDirection(0x0137, 0x0000, 400)

    ChrTalk(
        0x0137,
        (
            '#1070160718V不好意思，\n',
            '能直接去玛诺利亚村吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0137,
        (
            '#1070160719V我在格兰赛尔\n',
            '还有重要的商谈要进行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    def _loc_AAB(): pass

    label('loc_AAB')

    Return()

# id: 0x0008 offset: 0xAAC
@scena.Code('func_08_AAC')
def func_08_AAC():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '东　卢安市　　　３７４塞尔矩\n',
            '　　玛诺利亚村　　６３塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0009 offset: 0xB18
@scena.Code('func_09_B18')
def func_09_B18():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '南　巴伦诺灯塔　　７０塞尔矩',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
