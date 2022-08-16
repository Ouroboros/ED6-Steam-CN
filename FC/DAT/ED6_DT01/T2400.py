import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2400_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2400   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2400.x'
    header.mapIndex       = 1
    header.bgm            = 15
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
        ('ED6_DT07/CH02590._CH', 'ED6_DT07/CH02590P._CP'),
        ('ED6_DT07/CH02640._CH', 'ED6_DT07/CH02640P._CP'),
        ('ED6_DT07/CH02630._CH', 'ED6_DT07/CH02630P._CP'),
        ('ED6_DT07/CH02570._CH', 'ED6_DT07/CH02570P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT06/CH20051._CH', 'ED6_DT06/CH20051P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00041._CH', 'ED6_DT07/CH00041P._CP'),
        ('ED6_DT07/CH01720._CH', 'ED6_DT07/CH01720P._CP'),
    ]

# id: 0x10001 offset: 0xF2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '特蕾莎院长',
            x                   = 0,
            z                   = 0,
            y                   = 33500,
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
            name                = '达尼艾尔',
            x                   = 6000,
            z                   = 200,
            y                   = 22200,
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
            name                = '玛丽',
            x                   = 5800,
            z                   = 0,
            y                   = 23600,
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
            name                = '克拉姆',
            x                   = 4300,
            z                   = 200,
            y                   = 22900,
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
            name                = '基库',
            x                   = 800,
            z                   = 6000,
            y                   = -13810,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x01C5,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '目标用摄像机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0080,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '鸡',
            x                   = 44200,
            z                   = 240,
            y                   = 18540,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '鸡',
            x                   = 44200,
            z                   = 240,
            y                   = 18540,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '鸡',
            x                   = 44200,
            z                   = 240,
            y                   = 18540,
            direction           = 45,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '梅威海道方向',
            x                   = 1060,
            z                   = 0,
            y                   = -23220,
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

# id: 0x10002 offset: 0x232
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x232
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -1880,
            y           = 2000,
            z           = 4450,
            range       = 2800,
            dword_10    = 0xFFFFFC18,
            dword_14    = 0x000014B4,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000006,
        ),
    )

# id: 0x10004 offset: 0x252
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x252
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_25C',
    )

    Jump('loc_28B')

    def _loc_25C(): pass

    label('loc_25C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_266',
    )

    Jump('loc_28B')

    def _loc_266(): pass

    label('loc_266')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0084, 0, 0x420)),
            Expr.Return,
        ),
        'loc_270',
    )

    Jump('loc_28B')

    def _loc_270(): pass

    label('loc_270')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 6, 0x41E)),
            Expr.Return,
        ),
        'loc_27A',
    )

    Jump('loc_28B')

    def _loc_27A(): pass

    label('loc_27A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 1, 0x411)),
            Expr.Return,
        ),
        'loc_284',
    )

    Jump('loc_28B')

    def _loc_284(): pass

    label('loc_284')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0081, 5, 0x40D)),
            Expr.Return,
        ),
        'loc_28B',
    )

    def _loc_28B(): pass

    label('loc_28B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_299',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_0A_21D8)

    def _loc_299(): pass

    label('loc_299')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_2B0',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_0E_2CD7)

    def _loc_2B0(): pass

    label('loc_2B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_2C7',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x56),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, func_0F_2D4C)

    def _loc_2C7(): pass

    label('loc_2C7')

    ExecExpressionWithValue(
        0x000C,
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

# id: 0x0001 offset: 0x2D9
@scena.Code('func_01_2D9')
def func_01_2D9():
    OP_16(0x02, 4000, -128000, -108000, 196711)

    Return()

# id: 0x0002 offset: 0x2EC
@scena.Code('func_02_2EC')
def func_02_2EC():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_301',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_2EC')

    def _loc_301(): pass

    label('loc_301')

    Return()

# id: 0x0003 offset: 0x302
@scena.Code('func_03_302')
def func_03_302():
    ChrSetFlags(0x00FE, 0x0040)
    ChrSetFlags(0x00FE, 0x0004)
    OP_8D(0x00FE, -8760, 13210, 8700, 24630, 0)

    ExecExpressionWithValue(
        0x00FE,
        0x04,
        (
            Expr.Rand,
            (Expr.PushLong, 0x168),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_330(): pass

    label('loc_330')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_454',
    )

    If(
        (
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Gtr,
            (Expr.GetChrWork, 0xFE, 0x1),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x1),
            Expr.Lss,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Add,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.GetChrWork, 0xFE, 0x3),
            (Expr.PushLong, 0xBB8),
            Expr.Sub,
            (Expr.GetChrWork, 0x0, 0x3),
            Expr.Lss,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_419',
    )

    If(
        (
            (Expr.PushLong, 0x2238),
            Expr.Neg,
            (Expr.PushLong, 0x3E8),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x1),
            Expr.Lss,
            (Expr.PushLong, 0x339A),
            (Expr.PushLong, 0x3E8),
            Expr.Add,
            (Expr.GetChrWork, 0xFE, 0x3),
            Expr.Lss,
            Expr.Nez64,
            (Expr.PushLong, 0x21FC),
            (Expr.PushLong, 0x3E8),
            Expr.Sub,
            (Expr.GetChrWork, 0xFE, 0x1),
            Expr.Gtr,
            Expr.Nez64,
            (Expr.PushLong, 0x6036),
            (Expr.PushLong, 0x3E8),
            Expr.Sub,
            (Expr.GetChrWork, 0xFE, 0x3),
            Expr.Gtr,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3EE',
    )

    ChrSetFlags(0x00FE, 0x0020)
    ChrTurnDirection(0x00FE, 0x0000, 0)
    ChrClearFlags(0x00FE, 0x0020)

    @scena.Lambda('lambda_03DB')
    def lambda_03DB():
        OP_94(0x00, 0x00FE, 0x00B4, 0x0000012C, 0x00001770, 0x00)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_03DB)

    Jump('loc_411')

    def _loc_3EE(): pass

    label('loc_3EE')

    @scena.Lambda('lambda_03F4')
    def lambda_03F4():
        OP_8D(0x00FE, -8760, 13210, 8700, 24630, 6000)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_03F4)

    Sleep(200)

    def _loc_411(): pass

    label('loc_411')

    Sleep(30)

    Jump('loc_451')

    def _loc_419(): pass

    label('loc_419')

    Sleep(50)

    If(
        (
            Expr.Rand,
            (Expr.PushLong, 0x28),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_451',
    )

    TerminateThread(0x00FE, 0x02)

    @scena.Lambda('lambda_0439')
    def lambda_0439():
        OP_8D(0x00FE, -8760, 13210, 8700, 24630, 1500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0001, lambda_0439)

    def _loc_451(): pass

    label('loc_451')

    Jump('loc_330')

    def _loc_454(): pass

    label('loc_454')

    Return()

# id: 0x0004 offset: 0x455
@scena.Code('func_04_455')
def func_04_455():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_4DF',
    )

    CreateThread(0x00FE, 0x02, 0x00, func_05_4E0)
    PlaySE(401, 0x00, 0x64)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Rand,
            (Expr.PushLong, 0xA),
            Expr.Mod,
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4DF',
    )

    If(
        (
            (Expr.Eval, "AddItem(0x038B, 1)"),
            Expr.Return,
        ),
        'loc_4DF',
    )

    TalkBegin(0x00FE)
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    PlaySE(17, 0x00, 0x64)

    Talk(
        (
            (TxtCtl.SetColor, 0x0),
            '得到了',
            (TxtCtl.SetColor, 0x2),
            '新鲜鸡蛋',
            (TxtCtl.SetColor, 0x0),
            '。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FE)

    def _loc_4DF(): pass

    label('loc_4DF')

    Return()

# id: 0x0005 offset: 0x4E0
@scena.Code('func_05_4E0')
def func_05_4E0():
    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x7),
            Expr.Lss,
            Expr.Return,
        ),
        'loc_4FB',
    )

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x1),
            Expr.Add2,
            Expr.Return,
        ),
    )

    Yield()

    Jump('func_05_4E0')

    def _loc_4FB(): pass

    label('loc_4FB')

    ExecExpressionWithReg(
        0x0000,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    Return()

# id: 0x0006 offset: 0x506
@scena.Code('func_06_506')
def func_06_506():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 0, 0x410)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_202A',
    )

    SetScenaFlags(ScenaFlag(0x0082, 0, 0x410))
    EventBegin(0x00)
    ChrTurnDirection(0x000B, 0x0009, 0)
    ChrTurnDirection(0x0009, 0x000B, 0)
    ChrTurnDirection(0x000A, 0x000B, 0)
    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000A, 0x0080)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_562',
    )

    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    Jump('loc_579')

    def _loc_562(): pass

    label('loc_562')

    OP_62(0x0000, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    def _loc_579(): pass

    label('loc_579')

    @scena.Lambda('lambda_057F')
    def lambda_057F():
        OP_6C(45000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_057F)

    CameraMove(5200, 0, 22840, 2000)
    FormationAddMember(0x35, 0xFF)
    ChrSetFlags(0x0101, 0x0001)
    ChrSetFlags(0x0102, 0x0001)
    ChrSetFlags(0x0136, 0x0001)
    ChrSetPos(0x0101, -690, 0, 17260, 45)
    ChrSetPos(0x0102, -130, 0, 16010, 45)
    ChrSetPos(0x0136, 0, 0, 31800, 90)
    ChrSetFlags(0x0136, 0x0080)

    ChrTalk(
        0x000A,
        (
            '#0410040677V克拉姆，\n',
            '你刚才到哪儿去了嘛！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0410040678V科洛丝姐姐担心死了，\n',
            '到处去找你呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0400040679V#770F嘿嘿，用不着担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400040680V今天我可是有大收获哦～\n',
            '弄到了一个超～棒的东西呢～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0420040681V是什么啊？给我们看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0400040682V#771F嘿嘿嘿，看了可别吃惊哦～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400040683V这东西是我从一个没头脑的\n',
            '大姐头身上弄过来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040684V……你说谁没头脑啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0400040685V#774F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_078F')
    def lambda_078F():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_078F')

    DispatchAsync2(0x0101, 0x0002, lambda_078F)

    @scena.Lambda('lambda_07A0')
    def lambda_07A0():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_07A0')

    DispatchAsync2(0x0102, 0x0002, lambda_07A0)

    @scena.Lambda('lambda_07B1')
    def lambda_07B1():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_07B1')

    DispatchAsync2(0x000B, 0x0001, lambda_07B1)

    @scena.Lambda('lambda_07C2')
    def lambda_07C2():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_07C2')

    DispatchAsync2(0x0009, 0x0001, lambda_07C2)

    @scena.Lambda('lambda_07D3')
    def lambda_07D3():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_07D3')

    DispatchAsync2(0x000A, 0x0001, lambda_07D3)

    @scena.Lambda('lambda_07E4')
    def lambda_07E4():
        ChrWalkTo(0x00FE, 1620, 0, 22240, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_07E4)

    @scena.Lambda('lambda_07FF')
    def lambda_07FF():
        ChrWalkTo(0x00FE, 1560, 0, 21110, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_07FF)

    ChrTurnDirection(0x000B, 0x0101, 400)
    CameraMove(3750, 0, 22850, 1000)
    WaitForThreadExit(0x0101, 0x0001)
    ChrJumpToRelative(0x000B, 0, 0, 0, 1000, 10000)
    OP_62(0x000B, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    OP_94(0x01, 0x000B, 0x00B4, 0x000001F4, 0x00000BB8, 0x00)

    ChrTalk(
        0x000B,
        (
            '#0400040686V#774F你、你们怎么会来这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040687V#006F哼哼哼。\n',
            '你也太小看我们游击士了吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040688V像你这种淘气的调皮蛋一翘起尾巴，\n',
            '姐姐我就知道你有什么坏主意！\n',
            '更何况是找到你住在哪里！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0400040689V#772F可、可恶……\n',
            '乖乖等你捉的是小狗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x000B, 5620, 100, 21240, 7000, 0x00)
    ChrWalkTo(0x000B, 9320, 200, 21150, 7000, 0x00)
    ChrWalkTo(0x000B, 8650, -200, 19110, 7000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010040690V#005F喂！给我站住！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_09E7')
    def lambda_09E7():
        CameraMove(5748, -175, 18851, 1000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_09E7)

    @scena.Lambda('lambda_09FF')
    def lambda_09FF():
        ChrWalkTo(0x00FE, 5740, 0, 20660, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_09FF)

    @scena.Lambda('lambda_0A1A')
    def lambda_0A1A():
        ChrJumpTo(0x00FE, 6380, -200, 17060, 1500, 7000)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0A1A)

    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x000B, 0x0001)
    ChrWalkTo(0x0102, 4300, 200, 22900, 3000, 0x00)

    ExecExpressionWithValue(
        0x000D,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0xB, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0xB, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0xB, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_69(0x000D, 1000)
    OP_6A(0x000D)
    CreateThread(0x0101, 0x01, 0x00, func_09_212C)
    CreateThread(0x000B, 0x01, 0x00, func_08_2078)
    CreateThread(0x0102, 0x01, 0x00, func_07_202B)
    WaitForThreadExit(0x0102, 0x0001)
    Sleep(1800)

    Fade(1000)
    TerminateThread(0x000A, 0xFF)
    TerminateThread(0x0009, 0xFF)
    ChrTurnDirection(0x0009, 0x0102, 0)
    ChrTurnDirection(0x000A, 0x0102, 0)
    OP_6A(0x0000)
    MapClearFlags(0x00000001)
    CameraMove(4800, 185, 22555, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '#0410040691V那个，大哥哥……\n',
            '这是怎么回事呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000B, 0x0040)
    ChrSetPos(0x0101, -4998, 0, 29194, 0)
    ChrSetPos(0x000B, -1998, 0, 29194, 0)

    @scena.Lambda('lambda_0B4D')
    def lambda_0B4D():
        ChrWalkTo(0x00FE, 10264, 0, 32000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_0B4D)

    @scena.Lambda('lambda_0B68')
    def lambda_0B68():
        ChrWalkTo(0x00FE, 9580, 0, 31750, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B68)

    ChrTalk(
        0x0009,
        (
            '#0420040692V难道克拉姆\n',
            '又恶作剧了吗～？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0102, 90, 400)

    ChrTalk(
        0x0102,
        (
            '#0020040693V#019F啊，那个……\n',
            '来打扰你们真是不好意思了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000B, 0x0001)
    WaitForThreadExit(0x0101, 0x0001)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x000B, 0xFF)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetPos(0x000B, 8300, 200, 31590, 90)
    ChrSetPos(0x0101, 7700, 0, 31590, 90)

    @scena.Lambda('lambda_0C2E')
    def lambda_0C2E():
        OP_99(0x00FE, 0x00, 0x07, 3000)
        Yield()

        Jump('lambda_0C2E')

    DispatchAsync2(0x000B, 0x0001, lambda_0C2E)

    ChrTalk(
        0x000B,
        (
            '#0400040694V#776F#4P我不要～！\n',
            '放开我！快点放开我～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)

    @scena.Lambda('lambda_0C86')
    def lambda_0C86():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0C86)

    @scena.Lambda('lambda_0C94')
    def lambda_0C94():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0C94)

    @scena.Lambda('lambda_0CA2')
    def lambda_0CA2():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0CA2)

    CameraMove(8880, 0, 32490, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2640, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()
    OP_62(0x000B, 0x00000000, 1700, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x000B,
        (
            '#0400040695V#776F#2P我要去告发你虐待儿童！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040696V#009F#3P什～什么虐待儿童啊？\n',
            '小小年纪竟然说出这种话来！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040697V我的徽章呢？\n',
            '马上还给我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0400040698V#776F#2P说我拿了你的东西，\n',
            '你有证据吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040699V#006F#3P证据倒是没有……\n',
            '不过，让我调查一下就知道了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0E22')
    def lambda_0E22():
        ChrSetDirection(0x00FE, 270, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0E22)

    OP_97(0x000B, 7770, 31590, 180000, 4000, 0x0003)
    TerminateThread(0x000B, 0xFF)
    ChrSetSubChip(0x000B, 0)
    OP_9E(0x000B, 30, 0, 400, 5000)

    ChrTalk(
        0x000B,
        (
            '#0400040700V#778F#3P哎呀呀……！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400040701V你、你在摸哪里啊！？\n',
            '好～痒～痒～啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400040702V大变态！粗暴女！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_9E(0x000B, 30, 0, 600, 5000)

    ChrTalk(
        0x0101,
        (
            '#0010040703V#006F#2P行啦行啦，反抗是没有用的，\n',
            '还是乖乖地交出来吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 20)
    ChrSetPos(0x0136, 10, 0, 30720, 90)
    ChrClearFlags(0x0136, 0x0080)

    NpcTalk(
        0x0136,
        '女孩的声音',
        (
            '#0060040704V#2P基库！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    CameraMove(9390, 0, 34800, 800)
    Sleep(500)

    ChrClearFlags(0x000C, 0x0080)
    ChrSetFlags(0x000C, 0x0040)
    ChrSetPos(0x000C, 0, 6000, 31900, 0)
    PlaySE(140, 0x00, 0x64)
    ChrWalkTo(0x000C, 7700, 700, 31590, 20000, 0x00)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    @scena.Lambda('lambda_0FF1')
    def lambda_0FF1():
        ChrJumpToRelative(0x00FE, 300, 0, 0, 500, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0FF1)

    @scena.Lambda('lambda_100F')
    def lambda_100F():
        ChrJumpToRelative(0x00FE, 300, 0, 0, 500, 5000)

        ExitThread()

    DispatchAsync(0x000B, 0x0002, lambda_100F)

    ChrWalkTo(0x000C, 13990, 6000, 33400, 20000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010040705V#004F#2P哇哇～！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040706V刚、刚才那个东西是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1089')
    def lambda_1089():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1089)

    @scena.Lambda('lambda_1097')
    def lambda_1097():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_1097)

    @scena.Lambda('lambda_10A5')
    def lambda_10A5():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_10A5)

    @scena.Lambda('lambda_10B3')
    def lambda_10B3():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_10B3)

    @scena.Lambda('lambda_10C1')
    def lambda_10C1():
        ChrTurnDirection(0x00FE, 0x0136, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_10C1)

    @scena.Lambda('lambda_10CF')
    def lambda_10CF():
        CameraMove(3420, 0, 32210, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_10CF)

    @scena.Lambda('lambda_10E7')
    def lambda_10E7():
        OP_6C(315000, 3000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_10E7)

    @scena.Lambda('lambda_10F7')
    def lambda_10F7():
        CameraSetDistance(2800, 3000)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_10F7)

    WaitForThreadExit(0x0000, 0x0002)
    OP_92(0x000C, 0x0136, 5000, 10000, 0x00)
    OP_92(0x000C, 0x0136, 4000, 8000, 0x00)
    OP_92(0x000C, 0x0136, 3000, 6000, 0x00)
    OP_92(0x000C, 0x0136, 2000, 3000, 0x00)
    ChrWalkTo(0x000C, 10, 1000, 31500, 1500, 0x00)

    @scena.Lambda('lambda_1158')
    def lambda_1158():
        ChrSetDirection(0x00FE, 135, 200)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_1158)

    ChrSetChipByIndex(0x0136, 5)
    ChrSetSubChip(0x0136, 3)
    ChrMoveTo(0x000C, -50, 200, 31450, 1000, 0x00)
    WaitForThreadExit(0x000C, 0x0003)
    Sleep(100)

    Fade(250)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetSubChip(0x0136, 1)
    ChrSetFlags(0x0136, 0x0020)
    OP_0D()
    Sleep(500)

    NpcTalk(
        0x0136,
        '穿制服的少女',
        (
            '#0060040707V#046F请放了那个孩子！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040708V如果再对他动粗的话，\n',
            '就别怪我不客……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040709V#044F………………哎呀？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040710V#004F啊，你不就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0136,
        '穿制服的少女',
        (
            '#0060040711V#044F在玛诺利亚村见过的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '白隼',
        (
            '#0440040712V#310F#1P啾？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrJumpTo(0x000B, 6720, 0, 31500, 500, 5000)
    ChrClearFlags(0x000B, 0x0004)
    ChrWalkTo(0x000B, 5610, 0, 31700, 7000, 0x00)

    ChrTalk(
        0x000B,
        (
            '#0400040713V#775F救救我……科洛丝姐姐！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400040714V我、我什么事情也没干，\n',
            '这姐姐就无缘无故地把我抓住了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040715V#005F什、什么事情也没干？\n',
            '明明就是你把我的徽章给偷走的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#0400040716V#770F#1P嘿嘿，证据呢？\n',
            '有本事就拿出证据来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_13E6')
    def lambda_13E6():
        ChrWalkTo(0x00FE, 6070, 0, 31900, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_13E6)

    Sleep(200)

    ChrMoveTo(0x000B, 4500, 0, 30930, 5000, 0x00)
    ChrTurnDirection(0x0101, 0x000B, 400)

    ChrTalk(
        0x000B,
        (
            '#0400040717V#774F#1P啊，可不要再挠我痒痒了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040718V#009F你这个调皮蛋……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_147C')
    def lambda_147C():
        CameraMove(2050, 0, 30810, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_147C)

    @scena.Lambda('lambda_1494')
    def lambda_1494():
        ChrWalkTo(0x00FE, 2780, 0, 28360, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1494)

    Sleep(300)

    @scena.Lambda('lambda_14B4')
    def lambda_14B4():
        ChrWalkTo(0x00FE, 4160, 0, 28540, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_14B4)

    Sleep(400)

    @scena.Lambda('lambda_14D4')
    def lambda_14D4():
        ChrWalkTo(0x00FE, 900, 0, 29140, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_14D4)

    Sleep(300)

    WaitForThreadExit(0x0102, 0x0001)
    ChrTurnDirection(0x0102, 0x0136, 0)

    ChrTalk(
        0x0102,
        (
            '#0020040719V#010F你好，我们又见面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0136, 135, 400)

    ChrTalk(
        0x0136,
        (
            '#0060040720V#045F啊，上次给你们添麻烦了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040721V刚才真不好意思，\n',
            '我还以为是强盗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040722V#043F啊，对了……\n',
            '究竟发生了什么事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x000A, 0x0001)

    ChrTalk(
        0x000A,
        (
            '#0410040723V科洛丝姐姐，\n',
            '不用问也能猜到啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0410040724V肯定是克拉姆\n',
            '又惹出什么祸来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0009, 0x0001)

    ChrTalk(
        0x0009,
        (
            '#0420040725V嗯……姐姐～\n',
            '苹果派做好了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040726V#041F啊，再等一下好吗，\n',
            '苹果派要烤一下才能吃的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040727V#005F这个臭小鬼！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0400040728V#776F#1P粗暴女！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0410040729V克拉姆你也真是的。\n',
            '什么时候才能不这么孩子气啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0420040730V苹果派，好了没有啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0136, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0102,
        (
            '#0020040731V#019F……总觉得\n',
            '情况好像变得越来越复杂了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040732V#045F啊，呵呵……\n',
            '我也觉得是呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '白隼',
        (
            '#0440040733V#311F#2P啾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '女性的声音',
        (
            '#0390040734V#3P哎呀哎呀～\n',
            '怎么外面这么吵呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0008, 0x0080)
    ChrClearFlags(0x0008, 0x0004)
    ChrWalkTo(0x0008, 0, 0, 31800, 1500, 0x00)
    ChrSetDirection(0x0008, 90, 400)

    @scena.Lambda('lambda_187D')
    def lambda_187D():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_187D')

    DispatchAsync2(0x000B, 0x0001, lambda_187D)

    @scena.Lambda('lambda_188E')
    def lambda_188E():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_188E')

    DispatchAsync2(0x0009, 0x0001, lambda_188E)

    @scena.Lambda('lambda_189F')
    def lambda_189F():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_189F')

    DispatchAsync2(0x000A, 0x0001, lambda_189F)

    @scena.Lambda('lambda_18B0')
    def lambda_18B0():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_18B0')

    DispatchAsync2(0x0101, 0x0001, lambda_18B0)

    @scena.Lambda('lambda_18C1')
    def lambda_18C1():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_18C1')

    DispatchAsync2(0x0102, 0x0001, lambda_18C1)

    @scena.Lambda('lambda_18D2')
    def lambda_18D2():
        ChrTurnDirection(0x00FE, 0x0008, 400)
        Yield()

        Jump('lambda_18D2')

    DispatchAsync2(0x0136, 0x0001, lambda_18D2)

    ChrTalk(
        0x0136,
        (
            '#0060040735V#044F特蕾莎老师！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390040736V#750F#1P虽然详细情况我不太清楚……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390040737V不过看起来，\n',
            '又是克拉姆做了什么恶作剧吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0400040738V#772F才、才不会呢。\n',
            '我可是什么都没干哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0400040739V老师你可不要听\n',
            '这个粗暴的姐姐乱说话哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040740V#009F谁、谁是粗暴的姐姐啊！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390040741V#750F#1P哎呀哎呀～真是伤脑筋。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0008, 2580, 0, 30490, 2000, 0x00)
    ChrSetDirection(0x0008, 90, 400)

    ChrTalk(
        0x0008,
        (
            '#0390040742V#750F#1P克拉姆……\n',
            '你真的什么都没有做吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0400040743V#771F嗯，那当然啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390040744V#750F#1P你敢向空之女神发誓吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0400040745V#775F当、当然敢啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390040746V#754F#1P是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390040747V#750F刚才我在你们的房间里\n',
            '捡到了一枚徽章之类的东西……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390040748V那不是你的东西吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#0400040749V#772F咦，不可能……\n',
            '我明明塞进自己裤袋里面的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 1700, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#0400040750V#774F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040751V#005F果然是你～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040752V#044F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040753V#010F老师套话还真是有一手……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390040754V#752F#1P克拉姆……\n',
            '这下你无话可说了吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390040755V马上把你拿走的东西\n',
            '还给这位姐姐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 1700, 0x0E, 0x0F, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x000B,
        (
            '#0400040756V#773F呜呜呜呜呜呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x000B, 0x01)
    ChrTurnDirection(0x000B, 0x0101, 400)

    ChrTalk(
        0x000B,
        (
            '#0400040757V#776F#1P算我倒霉！\n',
            '还你就还你！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0x01)
    TerminateThread(0x0102, 0x01)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x0009, 0x01)
    TerminateThread(0x0136, 0x01)

    @scena.Lambda('lambda_1D80')
    def lambda_1D80():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_1D80')

    DispatchAsync2(0x0101, 0x0001, lambda_1D80)

    @scena.Lambda('lambda_1D91')
    def lambda_1D91():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_1D91')

    DispatchAsync2(0x0008, 0x0001, lambda_1D91)

    @scena.Lambda('lambda_1DA2')
    def lambda_1DA2():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_1DA2')

    DispatchAsync2(0x0102, 0x0001, lambda_1DA2)

    @scena.Lambda('lambda_1DB3')
    def lambda_1DB3():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_1DB3')

    DispatchAsync2(0x000A, 0x0001, lambda_1DB3)

    @scena.Lambda('lambda_1DC4')
    def lambda_1DC4():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_1DC4')

    DispatchAsync2(0x0009, 0x0001, lambda_1DC4)

    @scena.Lambda('lambda_1DD5')
    def lambda_1DD5():
        ChrTurnDirection(0x00FE, 0x000B, 0)
        Yield()

        Jump('lambda_1DD5')

    DispatchAsync2(0x0136, 0x0001, lambda_1DD5)

    OP_92(0x000B, 0x0101, 1200, 4000, 0x00)
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '克拉姆将徽章扔在地上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    AddItem(0x035C, 1)
    ChrMoveTo(0x000B, 4500, 0, 30930, 4000, 0x00)

    ChrTalk(
        0x0101,
        (
            '#0010040758V#004F啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrJumpToRelative(0x000B, 0, 0, 0, 800, 6000)

    ChrTalk(
        0x000B,
        (
            '#0400040759V#772F#1P哼，你好样的！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x000B, 180, 400)
    ChrWalkTo(0x000B, 5125, 0, 28830, 6000, 0x00)
    ChrWalkTo(0x000B, 4359, 0, 20640, 7000, 0x00)

    ChrTalk(
        0x0136,
        (
            '#0060040760V#043F啊，克拉姆！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0390040761V#750F#1P不要紧，让他自己清醒一下也好。\n',
            '一会儿就会回来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0390040762V#750F啊，对了……\n',
            '大家都不要站在这里说话了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0008, 0xFF)
    ChrTurnDirection(0x0008, 0x0101, 400)
    Sleep(400)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0136, 0xFF)
    TerminateThread(0x000A, 0x01)
    TerminateThread(0x0009, 0x01)

    @scena.Lambda('lambda_1FA9')
    def lambda_1FA9():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1FA9)

    @scena.Lambda('lambda_1FB7')
    def lambda_1FB7():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1FB7)

    @scena.Lambda('lambda_1FC5')
    def lambda_1FC5():
        ChrTurnDirection(0x00FE, 0x0008, 400)

        ExitThread()

    DispatchAsync(0x0136, 0x0001, lambda_1FC5)

    Sleep(400)

    ChrTalk(
        0x0008,
        (
            '#0390040763V#750F#1P详细的情况，\n',
            '我们到屋子里边喝茶边谈吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1500, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T2410._SN', 100, 0, 0)
    IdleLoop()

    def _loc_202A(): pass

    label('loc_202A')

    Return()

# id: 0x0007 offset: 0x202B
@scena.Code('func_07_202B')
def func_07_202B():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2077',
    )

    ExecExpressionWithValue(
        0x000D,
        0x01,
        (
            (Expr.GetChrWork, 0x101, 0x1),
            (Expr.GetChrWork, 0xB, 0x1),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x02,
        (
            (Expr.GetChrWork, 0x101, 0x2),
            (Expr.GetChrWork, 0xB, 0x2),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    ExecExpressionWithValue(
        0x000D,
        0x03,
        (
            (Expr.GetChrWork, 0x101, 0x3),
            (Expr.GetChrWork, 0xB, 0x3),
            Expr.Add,
            (Expr.PushLong, 0x2),
            Expr.Div,
            Expr.Nop,
            Expr.Return,
        ),
    )

    Yield()

    Jump('func_07_202B')

    def _loc_2077(): pass

    label('loc_2077')

    Return()

# id: 0x0008 offset: 0x2078
@scena.Code('func_08_2078')
def func_08_2078():
    ChrWalkTo(0x00FE, 3740, -200, 16990, 7000, 0x00)
    ChrJumpTo(0x00FE, 1010, 200, 16990, 2000, 7000)
    ChrWalkTo(0x00FE, -2060, 100, 14180, 7000, 0x00)
    ChrWalkTo(0x00FE, -4500, -200, 14610, 7000, 0x00)

    @scena.Lambda('lambda_20D1')
    def lambda_20D1():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_20D1')

    DispatchAsync2(0x00FE, 0x0002, lambda_20D1)

    Sleep(1600)

    ChrMoveTo(0x00FE, -4670, -100, 18560, 7000, 0x00)
    Sleep(1200)

    ChrMoveTo(0x00FE, -4780, -200, 20270, 7000, 0x00)
    Sleep(500)

    TerminateThread(0x00FE, 0x02)
    ChrWalkTo(0x00FE, -5010, 0, 31750, 11000, 0x00)

    Return()

# id: 0x0009 offset: 0x212C
@scena.Code('func_09_212C')
def func_09_212C():
    Sleep(500)

    ChrWalkTo(0x00FE, 1240, 0, 21290, 7000, 0x00)
    ChrWalkTo(0x00FE, -1660, 200, 19240, 7000, 0x00)
    ChrJumpTo(0x00FE, -3190, -200, 18690, 2000, 7000)
    Sleep(1000)

    ChrMoveTo(0x00FE, -3120, -100, 14230, 7000, 0x00)
    Sleep(1000)

    ChrMoveTo(0x00FE, -3120, -100, 14230, 7000, 0x00)
    ChrMoveTo(0x00FE, -4500, -200, 14610, 7000, 0x00)
    Sleep(500)

    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x00FE, 0x02)
    ChrWalkTo(0x00FE, -5010, 0, 31750, 11000, 0x00)

    Return()

# id: 0x000A offset: 0x21D8
@scena.Code('func_0A_21D8')
def func_0A_21D8():
    EventBegin(0x00)
    CameraMove(-1130, 80, 31130, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0136, 0x0080)
    ChrSetPos(0x0101, 0, 0, 32900, 0)
    ChrSetPos(0x0102, 0, 0, 32900, 0)
    ChrSetPos(0x0136, 0, 0, 32900, 0)
    ChrSetFlags(0x0008, 0x0080)
    FadeIn(1000, 0)
    OP_0D()
    OP_70(0x0000, 20)
    OP_73(0x0000)
    CreateThread(0x0101, 0x01, 0x00, func_0B_2BF1)
    CreateThread(0x0102, 0x01, 0x00, func_0C_2C1C)
    CreateThread(0x0136, 0x01, 0x00, func_0D_2C60)
    WaitForThreadExit(0x0136, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010040819V#000F嗯……特蕾莎院长\n',
            '真是一位非常和蔼可亲的人呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040820V#010F是啊……\n',
            '感觉就像是母亲那样的亲切。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040821V#041F#2P呵呵，那些孩子一直都\n',
            '把老师看成是自己的母亲呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(407, 0x00, 0x64)
    OP_62(0x0101, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0102, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    OP_62(0x0136, 0x00000000, 2000, 0x26, 0x26, 0x000000FA, 0x01)
    Sleep(1000)

    ChrClearFlags(0x000C, 0x0080)
    ChrSetPos(0x000C, -5000, 8000, 13000, 0)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    @scena.Lambda('lambda_23B7')
    def lambda_23B7():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_23B7')

    DispatchAsync2(0x0101, 0x0001, lambda_23B7)

    @scena.Lambda('lambda_23C8')
    def lambda_23C8():
        ChrTurnDirection(0x00FE, 0x000C, 400)
        Yield()

        Jump('lambda_23C8')

    DispatchAsync2(0x0102, 0x0001, lambda_23C8)

    ChrSetDirection(0x0136, 180, 0)
    OP_92(0x000C, 0x0136, 5000, 10000, 0x00)
    PlaySE(140, 0x00, 0x64)
    OP_92(0x000C, 0x0136, 4000, 8000, 0x00)
    OP_92(0x000C, 0x0136, 3000, 6000, 0x00)
    OP_92(0x000C, 0x0136, 2000, 3000, 0x00)
    ChrWalkTo(0x000C, -630, 1000, 30300, 1500, 0x00)

    @scena.Lambda('lambda_2431')
    def lambda_2431():
        ChrSetDirection(0x00FE, 90, 200)

        ExitThread()

    DispatchAsync(0x000C, 0x0003, lambda_2431)

    ChrSetChipByIndex(0x0136, 5)
    ChrSetSubChip(0x0136, 2)
    ChrSetDirection(0x0136, 135, 0)
    ChrMoveTo(0x000C, -330, 200, 30600, 1000, 0x00)
    Fade(250)
    ChrSetSubChip(0x0136, 0)
    ChrSetFlags(0x000C, 0x0080)
    ChrSetFlags(0x0136, 0x0020)
    OP_0D()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    ChrTalk(
        0x0136,
        (
            '#0060040822V#040F#2P基库。\n',
            '让你久等了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0440040823V#310F#1P啾。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040824V#040F#2P嗯，是的。\n',
            '他们并不是坏人哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040825V他们是我的新朋友，\n',
            '艾丝蒂尔和约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040826V你记住他们的名字了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0440040827V#311F#1P啾！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040828V#041F#2P呵呵，乖孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040829V#004F厉、厉害啊。\n',
            '你在和它说话吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040830V#040F#2P也不能算是说话，\n',
            '不过我能知道它想表达什么。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040831V也许是因为\n',
            '大家能够感受到彼此的心情……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040832V#501F哇～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040833V#019F这就是所谓的心灵相通吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040834V#041F#2P是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0101, 0x000C, 800, 1500, 0x00)
    Sleep(500)

    ChrTalk(
        0x0101,
        (
            '#0010040835V#501F你好啊，基库。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040836V#001F我叫艾丝蒂尔，多多指教哦㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#0440040837V#310F#1P啾？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(1200)

    OP_63(0x000C)

    ChrTalk(
        0x000C,
        (
            '#0440040838V#310F#1P啾——',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_277B')
    def lambda_277B():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_277B')

    DispatchAsync2(0x0101, 0x0001, lambda_277B)

    @scena.Lambda('lambda_278C')
    def lambda_278C():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_278C')

    DispatchAsync2(0x0102, 0x0001, lambda_278C)

    @scena.Lambda('lambda_279D')
    def lambda_279D():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_279D')

    DispatchAsync2(0x0136, 0x0001, lambda_279D)

    PlaySE(140, 0x00, 0x64)
    Fade(250)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x0136, 0x0020)
    ChrSetSubChip(0x0136, 2)
    OP_0D()

    @scena.Lambda('lambda_27C8')
    def lambda_27C8():
        ChrWalkTo(0x00FE, -11680, 7000, 28410, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_27C8)

    Sleep(400)

    @scena.Lambda('lambda_27E8')
    def lambda_27E8():
        ChrWalkTo(0x00FE, -11680, 7000, 28410, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_27E8)

    Sleep(400)

    @scena.Lambda('lambda_2808')
    def lambda_2808():
        ChrWalkTo(0x00FE, -11680, 7000, 28410, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2808)

    Sleep(400)

    @scena.Lambda('lambda_2828')
    def lambda_2828():
        ChrWalkTo(0x00FE, -11680, 7000, 28410, 20000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2828)

    ChrTalk(
        0x0101,
        (
            '#0010040839V#004F啊啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040840V#007F呜呜……看来我被甩了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040841V#019F哈哈，真是可惜呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040842V#045F#2P呵呵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0136, 0xFF)
    ChrSetChipByIndex(0x0136, 6)
    ChrSetSubChip(0x0136, 0)
    ChrSetDirection(0x0136, 135, 400)

    ChrTalk(
        0x0136,
        (
            '#0060040843V#040F#2P话说回来，\n',
            '艾丝蒂尔你们等一下要去卢安市吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0102, 0x0136, 200)
    TerminateThread(0x0101, 0xFF)
    ChrTurnDirection(0x0101, 0x0136, 400)

    ChrTalk(
        0x0101,
        (
            '#0010040844V#006F嗯，我们要到那里的\n',
            '协会支部办理转属手续。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040845V要不然就不能接受工作了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040846V#040F#2P卢安的协会支部啊，\n',
            '我去过很那里多次呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040847V不介意的话，可以让我带你们去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040848V#501F哇～这真是太好了。\n',
            '我们可是求之不得呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020040849V#010F那样没关系吗？\n',
            '你不赶快回学院的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0136,
        (
            '#0060040850V#040F#2P没关系的。\n',
            '今天我向学院请了一天的假。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060040851V在天黑之前回去就没事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010040852V#001F那就这样决定啦⊙',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010040853V目的地卢安，出发～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetFlags(0x000C, 0x0080)
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    FadeOut(500, 0, -1)
    OP_0D()
    ChrSetPos(0x0101, -120, 10, 29740, 180)
    ChrSetPos(0x0102, -120, 10, 29740, 180)
    ChrSetPos(0x0136, -120, 10, 29740, 180)
    CameraMove(-120, 10, 29740, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeIn(500, 0)
    EventEnd(0x00)

    Return()

# id: 0x000B offset: 0x2BF1
@scena.Code('func_0B_2BF1')
def func_0B_2BF1():
    ChrClearFlags(0x0101, 0x0080)
    ChrWalkTo(0x0101, 0, 0, 29260, 2000, 0x00)

    @scena.Lambda('lambda_2C10')
    def lambda_2C10():
        ChrTurnDirection(0x00FE, 0x0136, 400)
        Yield()

        Jump('lambda_2C10')

    DispatchAsync2(0x00FE, 0x0002, lambda_2C10)

    Return()

# id: 0x000C offset: 0x2C1C
@scena.Code('func_0C_2C1C')
def func_0C_2C1C():
    Sleep(800)

    ChrClearFlags(0x0102, 0x0080)
    ChrWalkTo(0x00FE, 0, 0, 31670, 2000, 0x00)
    ChrWalkTo(0x00FE, 1500, 0, 30360, 2000, 0x00)

    @scena.Lambda('lambda_2C54')
    def lambda_2C54():
        ChrTurnDirection(0x00FE, 0x0136, 400)
        Yield()

        Jump('lambda_2C54')

    DispatchAsync2(0x00FE, 0x0002, lambda_2C54)

    Return()

# id: 0x000D offset: 0x2C60
@scena.Code('func_0D_2C60')
def func_0D_2C60():
    Sleep(800)

    Sleep(800)

    ChrClearFlags(0x0136, 0x0080)
    ChrWalkTo(0x00FE, 0, 0, 31670, 2000, 0x00)
    ChrSetDirection(0x00FE, 0, 400)
    Sleep(500)

    OP_72(0x0000, 0x0800)
    PlaySE(7, 0x00, 0x64)
    OP_6F(0x0000, 20)
    OP_70(0x0000, 0)
    OP_73(0x0000)
    OP_71(0x0000, 0x0800)
    Sleep(500)

    ChrSetDirection(0x00FE, 180, 400)
    ChrWalkTo(0x0136, -130, 10, 30800, 2000, 0x00)
    ChrSetDirection(0x00FE, 135, 400)

    Return()

# id: 0x000E offset: 0x2CD7
@scena.Code('func_0E_2CD7')
def func_0E_2CD7():
    EventBegin(0x00)
    CameraMove(310, 0, -160, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(3840, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    FadeIn(2000, 0)
    CameraMove(1900, 0, 36890, 10000)
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T2411._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000F offset: 0x2D4C
@scena.Code('func_0F_2D4C')
def func_0F_2D4C():
    EventBegin(0x00)
    CameraMove(3610, 0, 34400, 0)
    OP_6C(57000, 0)
    LoadEffect(0x00, 'map\\\\mpfire0.eff')
    PlayEffect(0x00, 0xFF, 0x00FF, 3450, 2000, 34330, 0, 0, 0, 4000, 4000, 4000, 0x00FF, 0, 0, 0, 0)
    PlayEffect(0x00, 0xFF, 0x00FF, 3650, 1000, 33330, 0, 0, 0, 4000, 4000, 4000, 0x00FF, 0, 0, 0, 0)
    FadeIn(2000, 0)
    OP_6C(351000, 4000)
    MapSetFlags(0x02000000)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T2411._SN', 100, 0, 0)
    IdleLoop()

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
