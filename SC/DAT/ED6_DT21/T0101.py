import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0101_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0101   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'rolent'
    header.mapModel       = 'T0101.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0101_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT06/CH20038._CH', 'ED6_DT06/CH20038P._CP'),
    ]

# id: 0x10001 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '雪拉',
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
            name                = '提妲',
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
            name                = '科洛丝',
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
            name                = '奥利维尔',
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
            name                = '阿加特',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '洛连特·市长官邸',
            x                   = 90860,
            z                   = 0,
            y                   = 40240,
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
            name                = '洛连特飞船坪',
            x                   = 49150,
            z                   = 0,
            y                   = 95090,
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
            name                = '艾利兹街道方向',
            x                   = 48960,
            z                   = 0,
            y                   = 1120,
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
            name                = '米尔西街道方向',
            x                   = 5400,
            z                   = 0,
            y                   = 39830,
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
            name                = '玛鲁加山道方向',
            x                   = 28060,
            z                   = 0,
            y                   = 80870,
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

# id: 0x10002 offset: 0x21A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x21A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 43240,
            y           = -50,
            z           = 11610,
            range       = 54840,
            dword_10    = 0x0000079E,
            dword_14    = 0x0000317E,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000008,
        ),
        ScenaEventData(
            x           = 18140,
            y           = -50,
            z           = 36360,
            range       = 19090,
            dword_10    = 0x0000079E,
            dword_14    = 0x0000AF14,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000009,
        ),
        ScenaEventData(
            x           = 25210,
            y           = -50,
            z           = 70360,
            range       = 30660,
            dword_10    = 0x0000079E,
            dword_14    = 0x00011828,
            dword_18    = 0x00000000,
            dword_1C    = 0x0000000A,
        ),
        ScenaEventData(
            x           = 52800,
            y           = 0,
            z           = 18950,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000016,
        ),
        ScenaEventData(
            x           = 52800,
            y           = 0,
            z           = 29050,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000017,
        ),
        ScenaEventData(
            x           = 44700,
            y           = 0,
            z           = 33020,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000018,
        ),
        ScenaEventData(
            x           = 44700,
            y           = 0,
            z           = 21990,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000019,
        ),
        ScenaEventData(
            x           = 30900,
            y           = 0,
            z           = 47270,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001A,
        ),
        ScenaEventData(
            x           = 34300,
            y           = 0,
            z           = 52980,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001A,
        ),
        ScenaEventData(
            x           = 66000,
            y           = 0,
            z           = 52470,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001B,
        ),
        ScenaEventData(
            x           = 73000,
            y           = 0,
            z           = 34550,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001C,
        ),
        ScenaEventData(
            x           = 54800,
            y           = 0,
            z           = 49170,
            range       = 1000,
            dword_10    = 0x000007D0,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x0000001D,
        ),
    )

# id: 0x10004 offset: 0x39A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 55000,
            triggerZ            = 0,
            triggerY            = 45300,
            triggerRange        = 1700,
            actorX              = 55000,
            actorZ              = 2500,
            actorY              = 45300,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0013,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 44710,
            triggerZ            = 0,
            triggerY            = 70740,
            triggerRange        = 1500,
            actorX              = 44710,
            actorZ              = 1800,
            actorY              = 70740,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0014,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 45280,
            triggerZ            = 0,
            triggerY            = 71310,
            triggerRange        = 1500,
            actorX              = 45280,
            actorZ              = 1800,
            actorY              = 71310,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0015,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 76980,
            triggerZ            = 0,
            triggerY            = 19020,
            triggerRange        = 800,
            actorX              = 76980,
            actorZ              = 0,
            actorY              = 19020,
            flags               = 0x007C,
            talkScenaIndex      = 0x0001,
            talkFunctionIndex   = 0x0000,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x42A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_444',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x51),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    Event(0, func_02_4C9)

    Jump('loc_47C')

    def _loc_444(): pass

    label('loc_444')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 1, 0x10F1)),
            Expr.Return,
        ),
        'loc_455',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 1, 0x10F1))
    Event(0, func_03_5BE)

    Jump('loc_47C')

    def _loc_455(): pass

    label('loc_455')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 2, 0x10F2)),
            Expr.Return,
        ),
        'loc_466',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 2, 0x10F2))
    Event(0, func_0B_1378)

    Jump('loc_47C')

    def _loc_466(): pass

    label('loc_466')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 3, 0x10F3)),
            Expr.Return,
        ),
        'loc_47C',
    )

    ClearScenaFlags(ScenaFlag(0x021E, 3, 0x10F3))
    MapSetFlags(0x10000000)
    Event(1, 0x0002)

    Jump('loc_47C')

    def _loc_47C(): pass

    label('loc_47C')

    Return()

# id: 0x0001 offset: 0x47D
@scena.Code('func_01_47D')
def func_01_47D():
    OP_B1('T0100_n')
    OP_16(0x02, 4000, -80000, -88000, 2293761)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4B9',
    )

    MapSetFlags(0x00000010)
    OP_11(0x4B, 0x4B, 0x96, 0, 60000, 0)

    def _loc_4B9(): pass

    label('loc_4B9')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_4C5'),
        (-1, 'loc_4C8'),
    )

    def _loc_4C5(): pass

    label('loc_4C5')

    Jump('loc_4C8')

    def _loc_4C8(): pass

    label('loc_4C8')

    Return()

# id: 0x0002 offset: 0x4C9
@scena.Code('func_02_4C9')
def func_02_4C9():
    EventBegin(0x00)
    OP_11(0x4B, 0x4B, 0x96, 0, 90000, 0)
    OP_DB()
    ChrSetFlags(0x0000, 0x0080)
    ChrSetFlags(0x0001, 0x0080)
    ChrSetFlags(0x0002, 0x0080)
    ChrSetFlags(0x0003, 0x0080)
    CameraMove(50400, 0, 23350, 0)
    OP_67(0, 7720, -10000, 0)
    CameraSetDistance(5070, 0)
    OP_6C(134000, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_0533')
    def lambda_0533():
        CameraMove(63060, 0, 57110, 9500)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0533)

    @scena.Lambda('lambda_054B')
    def lambda_054B():
        OP_6C(38000, 9500)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_054B)

    @scena.Lambda('lambda_055B')
    def lambda_055B():
        OP_67(0, 5420, -10000, 9500)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_055B)

    FadeIn(1000, 0)
    Sleep(4500)

    Sleep(2000)

    Sleep(2000)

    FadeOut(2000, 0, -1)
    OP_0D()
    TerminateThread(0x0000, 0x01)
    TerminateThread(0x0000, 0x02)
    TerminateThread(0x0000, 0x03)
    ChrClearFlags(0x0000, 0x0080)
    ChrClearFlags(0x0001, 0x0080)
    ChrClearFlags(0x0002, 0x0080)
    ChrClearFlags(0x0003, 0x0080)
    OP_DC()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T0211._SN', 106, 0, 0)
    IdleLoop()

    Return()

# id: 0x0003 offset: 0x5BE
@scena.Code('func_03_5BE')
def func_03_5BE():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_5DE',
    )

    Call(0, 0x0011)
    FadeIn(0, 0)
    Call(0, 0x0012)

    def _loc_5DE(): pass

    label('loc_5DE')

    ChrSetPos(0x0101, 73060, 500, 32259, 0)
    ChrSetPos(0x0103, 73060, 500, 31260, 0)
    ChrSetPos(0x00F8, 73060, 500, 30260, 0)
    ChrSetPos(0x00F9, 73060, 500, 29260, 0)
    CameraMove(73090, 0, 34420, 0)
    OP_67(0, 8780, -10000, 0)
    CameraSetDistance(2810, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    FadeIn(1000, 0)
    OP_0D()
    OP_6F(0x000E, 0)
    OP_70(0x000E, 59)
    OP_73(0x000E)
    Sleep(200)

    CreateThread(0x0101, 0x01, 0x00, func_04_C00)
    CreateThread(0x0103, 0x01, 0x00, func_05_C30)
    CreateThread(0x00F8, 0x01, 0x00, func_06_C60)
    CreateThread(0x00F9, 0x01, 0x00, func_07_C90)

    @scena.Lambda('lambda_06A1')
    def lambda_06A1():
        CameraMove(73020, 0, 37990, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_06A1)

    Sleep(2000)

    WaitForThreadExit(0x00F9, 0x0001)
    Sleep(200)

    ChrTalk(
        0x0101,
        (
            '#0010281420V#1010F#6P我说，各位……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281421V#1002F我觉得……\n',
            '这会不会是『结社』干的好事？',
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
        'loc_761',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281422V#074F啊啊……\n',
            '很有可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_809')

    def _loc_761(): pass

    label('loc_761')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_79A',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281423V#032F嗯……\n',
            '很有可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_809')

    def _loc_79A(): pass

    label('loc_79A')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7D3',
    )

    ChrTalk(
        0x0106,
        (
            '#0050281424V#057F嗯……\n',
            '很有可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_809')

    def _loc_7D3(): pass

    label('loc_7D3')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_809',
    )

    ChrTalk(
        0x0105,
        (
            '#0060281425V#043F嗯……\n',
            '很有可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_809(): pass

    label('loc_809')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_894',
    )

    ChrTalk(
        0x0107,
        (
            '#0070281426V#561F连教区长都查不出原由、\n',
            '原因不明的昏睡状态……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070281427V#062F可以称为是\n',
            '『不可能的现象』了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A34')

    def _loc_894(): pass

    label('loc_894')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['科洛丝'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_921',
    )

    ChrTalk(
        0x0105,
        (
            '#0060281428V#047F连教会都查不出原由、\n',
            '原因不明的昏睡状态……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060281429V#042F可能可以称为是\n',
            '『不可能的现象』了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A34')

    def _loc_921(): pass

    label('loc_921')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_9AC',
    )

    ChrTalk(
        0x0106,
        (
            '#0050281430V#053F连教会的人都查不出原由、\n',
            '原因不明的昏睡状态……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050281431V#057F可以称为是\n',
            '『不可能的现象』了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A34')

    def _loc_9AC(): pass

    label('loc_9AC')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['奥利维尔'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_A34',
    )

    ChrTalk(
        0x0104,
        (
            '#0040281432V#035F连教会的人都查不出原由、\n',
            '原因不明的昏睡状态……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040281433V#032F可以称为是\n',
            '『不可能的现象』了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A34(): pass

    label('loc_A34')

    ChrTalk(
        0x0101,
        (
            '#0010281434V#1007F#6P果然是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010281435V#1002F那么，莫非\n',
            '也有『暗示』吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030281436V#026F#5P嗯……\n',
            '有必要确认一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281437V#022F昏睡的人的名单\n',
            '都记在笔记上了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010281438V#1004F#6P啊，等一等……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_AD('ED6_DT24/C_VIS226._CH', 0x0000, 0x0000, 0x000001F4)
    Sleep(2000)

    OP_56(0x03)
    OP_AE(0x000001F4)
    Sleep(1000)

    ChrTalk(
        0x0103,
        (
            '#0030281439V#022F以那四个人身边的人为中心\n',
            '走访一下整个城镇。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281440V转一圈后再返回协会\n',
            '向爱娜报告就行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010260345V#1002F#6P嗯……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0302, 2, 0x1812))
    OP_28(0x0090, 0x04, 0x02)
    OP_28(0x0090, 0x04, 0x08)
    OP_28(0x0090, 0x01, 0x0001)
    OP_28(0x0090, 0x01, 0x0002)
    OP_28(0x0090, 0x01, 0x0008)
    OP_28(0x0090, 0x01, 0x0020)
    OP_28(0x0090, 0x01, 0x0080)
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0xC00
@scena.Code('func_04_C00')
def func_04_C00():
    ChrMoveToRelative(0x00FE, 0, 0, 5000, 2000, 0x00)
    ChrWalkTo(0x00FE, 72930, 0, 39220, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x0005 offset: 0xC30
@scena.Code('func_05_C30')
def func_05_C30():
    ChrMoveToRelative(0x00FE, 0, 0, 5000, 2000, 0x00)
    ChrWalkTo(0x00FE, 74000, 0, 38170, 2000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)

    Return()

# id: 0x0006 offset: 0xC60
@scena.Code('func_06_C60')
def func_06_C60():
    ChrMoveToRelative(0x00FE, 0, 0, 5000, 2000, 0x00)
    ChrWalkTo(0x00FE, 71870, 0, 38090, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x0007 offset: 0xC90
@scena.Code('func_07_C90')
def func_07_C90():
    ChrMoveToRelative(0x00FE, 0, 0, 5000, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(200)

    OP_72(0x000E, 0x0800)
    OP_6F(0x000E, 59)
    OP_70(0x000E, 0)
    OP_23(0x0006)
    PlaySE(7, 0x00, 0x64)
    OP_73(0x000E)
    OP_71(0x000E, 0x0800)
    ChrSetDirection(0x00FE, 0, 400)
    ChrWalkTo(0x00FE, 73210, 0, 37050, 2000, 0x00)

    Return()

# id: 0x0008 offset: 0xCEF
@scena.Code('func_08_CEF')
def func_08_CEF():
    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 3, 0x1813)),
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 4, 0x1814)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 5, 0x1815)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 6, 0x1816)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_E6A',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DDD',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_D47',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281732V#070F好，差不多该回协会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DDA')

    def _loc_D47(): pass

    label('loc_D47')

    ChrTalk(
        0x0108,
        (
            '#0080281733V#070F呼，浓雾弥漫的夜路……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080281734V对修行正合适，\n',
            '不过现在时机\n',
            '并不对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080281735V该问的都已经问过了，\n',
            '我们回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_DDA(): pass

    label('loc_DDA')

    Jump('loc_E67')

    def _loc_DDD(): pass

    label('loc_DDD')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_DF3',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_DFA')

    def _loc_DF3(): pass

    label('loc_DF3')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_DFA(): pass

    label('loc_DFA')

    ChrTalk(
        0x0103,
        (
            '#0030281736V#020F在雾这么浓的深夜\n',
            '出去太危险了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281737V该问的都已经问过了，\n',
            '差不多该回协会了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_E67(): pass

    label('loc_E67')

    Jump('loc_EFE')

    def _loc_E6A(): pass

    label('loc_E6A')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EAD',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281738V#070F夜已经深了，\n',
            '赶快完成走访吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EFE')

    def _loc_EAD(): pass

    label('loc_EAD')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EC3',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_ECA')

    def _loc_EC3(): pass

    label('loc_EC3')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_ECA(): pass

    label('loc_ECA')

    ChrTalk(
        0x0103,
        (
            '#0030281739V#020F夜已经深了，尽快\n',
            '完成走访吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EFE(): pass

    label('loc_EFE')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0009 offset: 0xF1A
@scena.Code('func_09_F1A')
def func_09_F1A():
    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 3, 0x1813)),
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 4, 0x1814)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 5, 0x1815)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 6, 0x1816)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1095',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1008',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_F72',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281732V#070F好，差不多该回协会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1005')

    def _loc_F72(): pass

    label('loc_F72')

    ChrTalk(
        0x0108,
        (
            '#0080281733V#070F呼，浓雾弥漫的夜路……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080281734V对修行正合适，\n',
            '不过现在时机\n',
            '并不对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080281735V该问的都已经问过了，\n',
            '我们回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_1005(): pass

    label('loc_1005')

    Jump('loc_1092')

    def _loc_1008(): pass

    label('loc_1008')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_101E',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_1025')

    def _loc_101E(): pass

    label('loc_101E')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_1025(): pass

    label('loc_1025')

    ChrTalk(
        0x0103,
        (
            '#0030281736V#020F在雾这么浓的深夜\n',
            '出去太危险了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281737V该问的都已经问过了，\n',
            '差不多该回协会了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_1092(): pass

    label('loc_1092')

    Jump('loc_112F')

    def _loc_1095(): pass

    label('loc_1095')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10DE',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281738V#070F夜已经深了，\n',
            '得赶快把事情做完才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_112F')

    def _loc_10DE(): pass

    label('loc_10DE')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10F4',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_10FB')

    def _loc_10F4(): pass

    label('loc_10F4')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_10FB(): pass

    label('loc_10FB')

    ChrTalk(
        0x0103,
        (
            '#0030281739V#020F夜已经深了，尽快\n',
            '完成走访吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_112F(): pass

    label('loc_112F')

    ChrMoveToRelative(0x0000, 1500, 0, 0, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x000A offset: 0x114B
@scena.Code('func_0A_114B')
def func_0A_114B():
    EventBegin(0x01)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 3, 0x1813)),
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 4, 0x1814)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 5, 0x1815)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x0302, 6, 0x1816)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_12C2',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1235',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_11A3',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281732V#070F好，差不多该回协会了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1232')

    def _loc_11A3(): pass

    label('loc_11A3')

    ChrTalk(
        0x0108,
        (
            '#0080281733V#070F呼，浓雾弥漫的夜路……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080281734V对修行正合适，\n',
            '不过现在时机\n',
            '并不对。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080281735V该问的都问过了，\n',
            '我们回协会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_1232(): pass

    label('loc_1232')

    Jump('loc_12BF')

    def _loc_1235(): pass

    label('loc_1235')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_124B',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_1252')

    def _loc_124B(): pass

    label('loc_124B')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_1252(): pass

    label('loc_1252')

    ChrTalk(
        0x0103,
        (
            '#0030281736V#020F在雾这么浓的深夜\n',
            '出去太危险了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030281737V该问的都已经问过了，\n',
            '差不多该回协会了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    def _loc_12BF(): pass

    label('loc_12BF')

    Jump('loc_135C')

    def _loc_12C2(): pass

    label('loc_12C2')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_130B',
    )

    ChrTalk(
        0x0108,
        (
            '#0080281738V#070F夜已经深了，\n',
            '得赶快把事情做完才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_135C')

    def _loc_130B(): pass

    label('loc_130B')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1321',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_1328')

    def _loc_1321(): pass

    label('loc_1321')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_1328(): pass

    label('loc_1328')

    ChrTalk(
        0x0103,
        (
            '#0030281739V#020F夜已经深了，尽快\n',
            '完成走访吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_135C(): pass

    label('loc_135C')

    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x000B offset: 0x1378
@scena.Code('func_0B_1378')
def func_0B_1378():
    EventBegin(0x00)
    CameraMove(52910, 250, 28860, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetPos(0x0101, 55680, 250, 28860, 270)
    ChrSetPos(0x0008, 56680, 250, 28860, 270)
    ChrSetPos(0x0009, 57680, 250, 28860, 270)
    ChrSetPos(0x000A, 58680, 250, 28860, 270)
    ChrSetPos(0x000B, 60680, 250, 28860, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)
    ChrClearFlags(0x000B, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    OP_6F(0x000A, 0)
    OP_70(0x000A, 59)
    OP_73(0x000A)
    Sleep(500)

    CreateThread(0x0101, 0x01, 0x00, func_0C_1D6B)
    CreateThread(0x0008, 0x01, 0x00, func_0D_1D9B)
    CreateThread(0x0009, 0x01, 0x00, func_0E_1DCB)
    CreateThread(0x000A, 0x01, 0x00, func_0F_1DFB)
    CreateThread(0x000B, 0x01, 0x00, func_10_1E24)
    Sleep(2000)

    @scena.Lambda('lambda_146E')
    def lambda_146E():
        CameraMove(50370, 0, 29350, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_146E)

    @scena.Lambda('lambda_1486')
    def lambda_1486():
        OP_67(0, 8830, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1486)

    @scena.Lambda('lambda_149E')
    def lambda_149E():
        OP_6C(32000, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_149E)

    @scena.Lambda('lambda_14AE')
    def lambda_14AE():
        OP_6E(272, 3000)

        ExitThread()

    DispatchAsync(0x0008, 0x0003, lambda_14AE)

    WaitForThreadExit(0x000B, 0x0001)
    Sleep(500)

    ChrTalk(
        0x000B,
        (
            '#0040290098V#030F呼，已经这么晚了，\n',
            '还是快点回去休息的好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290099V#031F那么，艾丝蒂尔，\n',
            '能不能带我去拜访你家？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1542')
    def lambda_1542():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1542)

    Sleep(50)

    @scena.Lambda('lambda_1555')
    def lambda_1555():
        ChrTurnDirection(0x00FE, 0x000B, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1555)

    Sleep(50)

    ChrTurnDirection(0x000A, 0x000B, 400)

    ChrTalk(
        0x0101,
        (
            '#0010290100V#1019F#6P等等……\n',
            '你为什么要来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040290101V#031F哈哈哈。\n',
            '不用这么警惕。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290102V我奥利维尔，\n',
            '就算在后宫环境中\n',
            '也能保持绅士风度。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290103V#037F呼呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070290104V#065F啊、啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0060290105V#045F#6P奥利维尔先生……\n',
            '你的眼睛已经把你出卖了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290106V#1007F#6P真是的，该不该\n',
            '直接用草席把你包着吊在外面呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_6F(0x000A, 0)
    OP_70(0x000A, 59)
    OP_73(0x000A)
    Sleep(200)

    ChrSetPos(0x000C, 55680, 250, 28860, 270)
    ChrClearFlags(0x000C, 0x0080)

    @scena.Lambda('lambda_1704')
    def lambda_1704():
        ChrWalkTo(0x000C, 52910, 250, 28860, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0000, lambda_1704)

    Sleep(500)

    @scena.Lambda('lambda_1724')
    def lambda_1724():
        CameraMove(51570, 0, 29500, 1500)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_1724)

    WaitForThreadExit(0x0106, 0x0001)
    WaitForThreadExit(0x0106, 0x0000)

    ChrTalk(
        0x000C,
        (
            '#0050290107V#555F你这个没出息的演奏家，\n',
            '在这里干吗呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050290108V赶快决定巡逻的\n',
            '队伍吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000C, 400)

    ChrTalk(
        0x000B,
        (
            '#0040290109V#033F#6P咦……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290110V#031F……哈哈哈。\n',
            '阿加特兄你真坏，',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290111V巡逻不是说好由\n',
            '你和金先生来嘛？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0050290112V#050F没这回事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050290113V我只记得是说\n',
            '由我们这些男的负责巡逻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0040290114V#033F#6P啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x000C, 52300, 130, 28860, 2000, 0x00)

    ChrTalk(
        0x000C,
        (
            '#0050290115V#054F好了，赶紧来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x00)

    ChrTalk(
        0x000B,
        (
            '#0040290116V#036F#6P阿、阿加特兄。\n',
            '能不能稍微等等？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290117V这样的后宫环境\n',
            '可是很难得的啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040290118V我会代替你一起享受的，\n',
            '求你放过我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0050290119V#053F少废话，赶紧开工。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000B, 0x0020)
    ChrSetDirection(0x000B, 270, 800)

    @scena.Lambda('lambda_19B8')
    def lambda_19B8():
        ChrMoveToRelative(0x00FE, 6000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_19B8)

    ChrSetFlags(0x000B, 0x0002)
    ChrSetChipByIndex(0x000B, 5)
    ChrSetSubChip(0x000B, 7)
    OP_63(0x000B)

    @scena.Lambda('lambda_19E5')
    def lambda_19E5():
        ChrMoveToRelativeAsync(0x00FE, 4000, 0, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_19E5)

    WaitForThreadExit(0x000B, 0x0001)
    OP_72(0x000A, 0x0800)
    OP_6F(0x000A, 59)
    OP_70(0x000A, 0)
    OP_23(0x0006)
    PlaySE(7, 0x00, 0x64)
    OP_73(0x000A)
    OP_71(0x000A, 0x0800)
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0008, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 1700, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x000A, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_1A89')
    def lambda_1A89():
        CameraMove(50370, 0, 29350, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1A89)

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010290120V#1007F#6P嗯，对付奥利维尔\n',
            '那样是最好的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290121V#1019F不过真是个不知道啥叫紧张的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1B16')
    def lambda_1B16():
        ChrSetDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_1B16)

    Sleep(50)

    @scena.Lambda('lambda_1B29')
    def lambda_1B29():
        ChrSetDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1B29)

    Sleep(50)

    @scena.Lambda('lambda_1B3C')
    def lambda_1B3C():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1B3C)

    WaitForThreadExit(0x000A, 0x0001)
    Sleep(400)

    ChrTalk(
        0x000A,
        (
            '#0060290122V#045F#2P呵呵，我到现在都不知道\n',
            '他到底是说笑的还是认真的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290123V#1015F#6P我看１００％是认真的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290124V#1006F总之他肯定是个\n',
            '会教坏提妲的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070290125V#067F#4P姐、姐姐这么说的话\n',
            '奥利维尔先生就太可怜了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030290126V#524F#5P呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#0010290127V#1015F#6P雪拉姐？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0030290128V#027F#5P嗯，没什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030290129V不过奥利维尔他说的也对，\n',
            '今夜就早点休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010290130V#1006F#6P嗯，是啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010290131V提妲，科洛丝。\n',
            '我来给你们带路。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x021E, 0, 0x10F0))
    NewScene('ED6_DT21/T0301._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x1D6B
@scena.Code('func_0C_1D6B')
def func_0C_1D6B():
    ChrMoveToRelative(0x00FE, -6000, 0, 0, 2000, 0x00)
    ChrMoveToRelative(0x00FE, -1000, 0, 0, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)

    Return()

# id: 0x000D offset: 0x1D9B
@scena.Code('func_0D_1D9B')
def func_0D_1D9B():
    ChrMoveToRelative(0x00FE, -6000, 0, 0, 2000, 0x00)
    ChrMoveToRelative(0x00FE, -1000, 0, 1000, 2000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)

    Return()

# id: 0x000E offset: 0x1DCB
@scena.Code('func_0E_1DCB')
def func_0E_1DCB():
    ChrMoveToRelative(0x00FE, -6000, 0, 0, 2000, 0x00)
    ChrMoveToRelative(0x00FE, -2000, 0, -1000, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)

    Return()

# id: 0x000F offset: 0x1DFB
@scena.Code('func_0F_1DFB')
def func_0F_1DFB():
    ChrMoveToRelative(0x00FE, -6000, 0, 0, 2000, 0x00)
    ChrMoveToRelative(0x00FE, -2200, 0, 0, 2000, 0x00)

    Return()

# id: 0x0010 offset: 0x1E24
@scena.Code('func_10_1E24')
def func_10_1E24():
    ChrWalkTo(0x00FE, 52910, 250, 28860, 2000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)
    Sleep(200)

    OP_72(0x000A, 0x0800)
    OP_6F(0x000A, 59)
    OP_70(0x000A, 0)
    OP_23(0x0006)
    PlaySE(7, 0x00, 0x64)
    OP_73(0x000A)
    ChrSetDirection(0x00FE, 270, 400)
    OP_71(0x000A, 0x0800)
    ChrMoveToRelative(0x00FE, -1230, 0, 0, 2000, 0x00)

    Return()

# id: 0x0011 offset: 0x1E83
@scena.Code('func_11_1E83')
def func_11_1E83():
    FadeOut(0, 0, -1)
    ClearScenaFlags(ScenaFlag(0x0240, 0, 0x1200))
    ClearScenaFlags(ScenaFlag(0x0240, 1, 0x1201))
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)
    FormationDelMember(0x09, 0xFF)

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
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_1F00'),
        (0x00000001, 'loc_1F06'),
        (-1, 'loc_1F0C'),
    )

    def _loc_1F00(): pass

    label('loc_1F00')

    SetScenaFlags(ScenaFlag(0x0240, 0, 0x1200))

    Jump('loc_1F0C')

    def _loc_1F06(): pass

    label('loc_1F06')

    SetScenaFlags(ScenaFlag(0x0240, 1, 0x1201))

    Jump('loc_1F0C')

    def _loc_1F0C(): pass

    label('loc_1F0C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_1F1A',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_1F1E')

    def _loc_1F1A(): pass

    label('loc_1F1A')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_1F1E(): pass

    label('loc_1F1E')

    Return()

# id: 0x0012 offset: 0x1F1F
@scena.Code('func_12_1F1F')
def func_12_1F1F():
    MapClearFlags(0x00000001)
    CameraMove(106730, -1920, 53920, 0)
    Sleep(100)

    OP_C9(
        0x00,
        (
            ChrTable['艾丝蒂尔'],
            ChrTable['雪拉扎德'],
            0x00FF,
            0x00FF,
        ),
        (
            ChrTable['阿加特'],
            ChrTable['奥利维尔'],
            ChrTable['科洛丝'],
            ChrTable['提妲'],
            ChrTable['金'],
            0xFFFF,
        ),
    )

    ExecExpressionWithVar(
        0x28,
        (
            (Expr.PushLong, 0xFFFF),
            Expr.Nop,
            Expr.Return,
        ),
    )

    FadeOut(0, 0, -1)
    OP_69(0x0000, 0)
    Sleep(1000)

    Return()

# id: 0x0013 offset: 0x1F71
@scena.Code('func_13_1F71')
def func_13_1F71():
    MapSetFlags(0x00000080)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '『七耀历１０７５年』\n',
            '　由利贝尔王室、七耀教会\n',
            '　以及洛连特市共同建造。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '『七耀历１１９２年』\n',
            '　百日战役中，被围攻洛连特的\n',
            '　埃雷波尼亚帝国军队炮击而倒塌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '『七耀历１１９７年』\n',
            '　在市民的协力下得以重建。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    MapClearFlags(0x00000080)

    Return()

# id: 0x0014 offset: 0x2075
@scena.Code('func_14_2075')
def func_14_2075():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '西　玛鲁加山道一侧出口',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0015 offset: 0x20BE
@scena.Code('func_15_20BE')
def func_15_20BE():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '北　洛连特飞船坪',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0016 offset: 0x2101
@scena.Code('func_16_2101')
def func_16_2101():
    OP_13(0x0004)

    Return()

# id: 0x0017 offset: 0x2105
@scena.Code('func_17_2105')
def func_17_2105():
    OP_13(0x0002)

    Return()

# id: 0x0018 offset: 0x2109
@scena.Code('func_18_2109')
def func_18_2109():
    OP_13(0x0006)

    Return()

# id: 0x0019 offset: 0x210D
@scena.Code('func_19_210D')
def func_19_210D():
    OP_13(0x0005)

    Return()

# id: 0x001A offset: 0x2111
@scena.Code('func_1A_2111')
def func_1A_2111():
    OP_13(0x0007)

    Return()

# id: 0x001B offset: 0x2115
@scena.Code('func_1B_2115')
def func_1B_2115():
    OP_13(0x0008)

    Return()

# id: 0x001C offset: 0x2119
@scena.Code('func_1C_2119')
def func_1C_2119():
    OP_13(0x0003)

    Return()

# id: 0x001D offset: 0x211D
@scena.Code('func_1D_211D')
def func_1D_211D():
    OP_13(0x000A)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
