import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T2200_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2200   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2200.x'
    header.mapIndex       = 1
    header.bgm            = 12
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = ['ED6_DT01/T2200._SN', 'ED6_DT01/T2200_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x64
@scena.EntryPoint('EntryPoint')
def EntryPoint():
    return (
        ScenaEntryPoint(
            dword_00        = 0x000157C0,
            dword_04        = 0x00000000,
            dword_08        = 0x000055F0,
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
        ('ED6_DT07/CH02410._CH', 'ED6_DT07/CH02410P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH00005._CH', 'ED6_DT07/CH00005P._CP'),
        ('ED6_DT07/CH00015._CH', 'ED6_DT07/CH00015P._CP'),
        ('ED6_DT07/CH00045._CH', 'ED6_DT07/CH00045P._CP'),
    ]

# id: 0x10001 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '戴尔蒙市长',
            x                   = 1200,
            z                   = 4000,
            y                   = 16700,
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
            name                = '奈尔',
            x                   = 24500,
            z                   = 0,
            y                   = 6100,
            direction           = 270,
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
            name                = '照相机',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x01C0,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '谜之男人\u3000※仮',
            x                   = 111500,
            z                   = 11000,
            y                   = 15700,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '盖尔多那',
            x                   = 98500,
            z                   = 0,
            y                   = 17600,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = ' ',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = ' ',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0180,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '卢安市·南街区',
            x                   = 68010,
            z                   = 0,
            y                   = 21970,
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

# id: 0x10002 offset: 0x1DA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x1DA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x1DA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x1DA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_1F5',
    )

    ChrSetPos(0x000C, 96920, 0, 18630, 90)

    Jump('loc_243')

    def _loc_1F5(): pass

    label('loc_1F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_210',
    )

    ChrSetPos(0x000C, 96920, 0, 18630, 90)

    Jump('loc_243')

    def _loc_210(): pass

    label('loc_210')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_22B',
    )

    ChrSetPos(0x000C, 96920, 0, 18630, 90)

    Jump('loc_243')

    def _loc_22B(): pass

    label('loc_22B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_243',
    )

    ChrSetPos(0x000C, 96920, 0, 18630, 90)

    def _loc_243(): pass

    label('loc_243')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_25A',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x52),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_07_818)

    def _loc_25A(): pass

    label('loc_25A')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_26A'),
        (0x00000065, 'loc_280'),
        (-1, 'loc_2A0'),
    )

    def _loc_26A(): pass

    label('loc_26A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 7, 0x43F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 6, 0x43E)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_27D',
    )

    SetScenaFlags(ScenaFlag(0x0087, 7, 0x43F))
    Event(0, func_06_594)

    def _loc_27D(): pass

    label('loc_27D')

    Jump('loc_2A0')

    def _loc_280(): pass

    label('loc_280')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x10)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x0020, 0x00, 0x40)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_29D',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(1, 0x0000)

    def _loc_29D(): pass

    label('loc_29D')

    Jump('loc_2A0')

    def _loc_2A0(): pass

    label('loc_2A0')

    Return()

# id: 0x0001 offset: 0x2A1
@scena.Code('func_01_2A1')
def func_01_2A1():
    OP_16(0x02, 4000, -16000, -108000, 196682)
    PlaySE(453, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x2B9
@scena.Code('func_02_2B9')
def func_02_2B9():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_2CE',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_2B9')

    def _loc_2CE(): pass

    label('loc_2CE')

    Return()

# id: 0x0003 offset: 0x2CF
@scena.Code('func_03_2CF')
def func_03_2CF():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_370',
    )

    ChrWalkTo(0x00FE, 98790, 0, 19040, 3000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)
    Sleep(1000)

    ChrWalkTo(0x00FE, 98500, 0, 17600, 3000, 0x00)
    ChrSetDirection(0x00FE, 90, 400)
    Sleep(1000)

    ChrWalkTo(0x00FE, 97040, 0, 17100, 3000, 0x00)
    ChrSetDirection(0x00FE, 180, 400)
    Sleep(1000)

    ChrWalkTo(0x00FE, 96920, 0, 18630, 3000, 0x00)
    ChrSetDirection(0x00FE, 120, 400)
    OP_62(0x000C, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(3000)

    OP_63(0x000C)

    Jump('func_03_2CF')

    def _loc_370(): pass

    label('loc_370')

    Return()

# id: 0x0004 offset: 0x371
@scena.Code('func_04_371')
def func_04_371():
    TalkBegin(0x000C)
    OP_63(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A0, 0, 0x500)),
            Expr.Return,
        ),
        'loc_3C4',
    )

    ChrTalk(
        0x00FE,
        (
            '我可是一直在这里\n',
            '勤勤恳恳地工作……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这下薪水该怎么办呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_576')

    def _loc_3C4(): pass

    label('loc_3C4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0087, 5, 0x43D)),
            Expr.Return,
        ),
        'loc_42A',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才，\n',
            '有一个看起来很了不起的大叔来过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然看起来很了不起，\n',
            '但是他的发型很奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_576')

    def _loc_42A(): pass

    label('loc_42A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 5, 0x42D)),
            Expr.Return,
        ),
        'loc_48A',
    )

    ChrTalk(
        0x00FE,
        (
            '我总觉得最近这里\n',
            '有许多显赫人物进进出出啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '经常有打扮高雅的人\n',
            '从这里经过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_576')

    def _loc_48A(): pass

    label('loc_48A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0085, 0, 0x428)),
            Expr.Return,
        ),
        'loc_4C6',
    )

    ChrTalk(
        0x00FE,
        (
            '已经到这个时候啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我觉得肚子有点饿了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_576')

    def _loc_4C6(): pass

    label('loc_4C6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0083, 3, 0x41B)),
            Expr.Return,
        ),
        'loc_50D',
    )

    ChrTalk(
        0x00FE,
        (
            '听说那座铜像是\n',
            '戴尔蒙家族第一代的主人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好威猛啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_576')

    def _loc_50D(): pass

    label('loc_50D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0082, 4, 0x414)),
            Expr.Return,
        ),
        'loc_576',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_555',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '哦，有事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我呀，是个园丁。\n',
            '有问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_576')

    def _loc_555(): pass

    label('loc_555')

    ChrTalk(
        0x00FE,
        (
            '我呀，是个园丁。\n',
            '有问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_576(): pass

    label('loc_576')

    TalkEnd(0x000C)

    Return()

# id: 0x0005 offset: 0x57A
@scena.Code('func_05_57A')
def func_05_57A():
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))

    ChrTalk(
        0x0102,
        (
            '#010F设立标志',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FF)

    Return()

# id: 0x0006 offset: 0x594
@scena.Code('func_06_594')
def func_06_594():
    EventBegin(0x00)
    ChrSetPos(0x0101, 82220, 0, 22710, 90)
    ChrSetPos(0x0102, 82680, 0, 21320, 90)
    ChrSetPos(0x0105, 81500, 0, 21870, 90)
    CameraMove(120230, 1900, 24150, 0)
    OP_67(0, 6040, -10000, 0)
    CameraSetDistance(5200, 0)
    OP_6C(79000, 0)
    OP_6E(261, 0)
    OP_12(0x00009470, 0x00030D40, 0x00000000)
    FadeIn(1000, 0)

    @scena.Lambda('lambda_0622')
    def lambda_0622():
        CameraMove(82030, 0, 22110, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_0622)

    @scena.Lambda('lambda_063A')
    def lambda_063A():
        OP_6C(315000, 10000)

        ExitThread()

    DispatchAsync(0x0000, 0x0003, lambda_063A)

    Sleep(2000)

    @scena.Lambda('lambda_064F')
    def lambda_064F():
        OP_67(0, 9500, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0001, 0x0002, lambda_064F)

    @scena.Lambda('lambda_0667')
    def lambda_0667():
        CameraSetDistance(2800, 8000)

        ExitThread()

    DispatchAsync(0x0001, 0x0003, lambda_0667)

    OP_12(0x00009470, 0x000186A0, 0x00001F40)
    Sleep(8000)

    ChrTalk(
        0x0101,
        (
            '#0010061436V#007F话说回来，还真是好大的房子啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061437V#009F果然要坏事做尽，\n',
            '才能住得起这样的房子吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020061438V#010F我想和这应该没什么关系……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061439V#047F毕竟戴尔蒙家族\n',
            '曾经是王国的豪门贵族。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060061440V这座官邸也应该是\n',
            '历代主人所继承的产业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010061441V#003F是吗……\n',
            '的确，屋子本身并没有罪。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010061442V#006F算了，不管这些了。\n',
            '总之要先好好盘问那个市长。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x818
@scena.Code('func_07_818')
def func_07_818():
    MapClearFlags(0x00000001)
    EventBegin(0x00)
    LoadEffect(0x04, 'map\\\\mp013_00.eff')
    LoadEffect(0x05, 'map\\\\mp013_01.eff')
    ChrSetFlags(0x0008, 0x0080)
    ChrSetFlags(0x0101, 0x0080)
    ChrSetFlags(0x0102, 0x0080)
    ChrSetFlags(0x0105, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    CameraMove(116010, 2150, 30790, 0)
    OP_6C(225000, 0)
    CameraSetDistance(3510, 0)
    ChrSetPos(0x000E, 110390, -3000, 39780, 90)
    ChrSetFlags(0x000E, 0x0040)
    OP_A1(0x000E, 0x0002)
    OP_72(0x0002, 0x0004)
    OP_72(0x0002, 0x0002)
    OP_71(0x0002, 0x0040)
    ChrSetPos(0x000D, 111540, -3000, 42790, 90)
    ChrSetFlags(0x000D, 0x0040)
    OP_A1(0x000D, 0x0003)
    OP_72(0x0003, 0x0004)
    OP_72(0x0003, 0x0002)
    OP_71(0x0003, 0x0040)
    CreateThread(0x0008, 0x01, 0x00, func_08_D3B)
    OP_72(0x0004, 0x0010)
    OP_70(0x0004, 30)
    OP_73(0x0004)
    CameraMove(114850, 0, 36610, 4000)

    @scena.Lambda('lambda_0904')
    def lambda_0904():
        CameraMove(114500, -1800, 40890, 4500)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0904)

    CreateThread(0x0101, 0x01, 0x00, func_09_1006)
    Sleep(600)

    CreateThread(0x0102, 0x01, 0x00, func_0A_110A)
    Sleep(600)

    CreateThread(0x0105, 0x01, 0x00, func_0B_11EB)
    Sleep(2300)

    OP_4A(0x0101, 1)

    ExecExpressionWithValue(
        0x0101,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetDirection(0x0101, 270, 0)
    OP_4A(0x0102, 1)

    ExecExpressionWithValue(
        0x0102,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetDirection(0x0102, 270, 0)
    Sleep(300)

    OP_4A(0x0105, 1)

    ExecExpressionWithValue(
        0x0105,
        0x0B,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetDirection(0x0105, 270, 0)

    ChrTalk(
        0x0101,
        (
            '#0010061736V#580F#5P那、那是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0105,
        (
            '#0060061737V#046F是戴尔蒙市长的帆船！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0008, 1)

    ChrTalk(
        0x0101,
        (
            '#0010061738V#005F#5P给、给我等一下！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_4B(0x0102, 1)
    WaitForThreadExit(0x0102, 0x0001)
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020061739V#016F开这条小船去追吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020061740V快，你们两个也上来！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0A61')
    def lambda_0A61():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0A61)

    ChrTurnDirection(0x0105, 0x0102, 400)

    ChrTalk(
        0x0105,
        (
            '#006F#5P#1KＯＫ！',
            TxtCtl.Enter,
        ),
    )

    ChrTalk(
        0x0101,
        (
            '#0010061741V#042F#6P#1K好的！',
            TxtCtl.Enter,
        ),
    )

    Sleep(500)

    OP_56(0x01)
    OP_59()

    @scena.Lambda('lambda_0AB6')
    def lambda_0AB6():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_0AB6')

    DispatchAsync2(0x0102, 0x0001, lambda_0AB6)

    @scena.Lambda('lambda_0AC7')
    def lambda_0AC7():
        CameraMove(111020, -1800, 41170, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0AC7)

    OP_4B(0x0101, 1)
    Sleep(600)

    OP_4B(0x0105, 1)
    CreateThread(0x0009, 0x01, 0x00, func_0C_12E6)
    WaitForThreadExit(0x0101, 0x0001)
    WaitForThreadExit(0x0105, 0x0001)
    TerminateThread(0x0102, 0xFF)
    ChrSetDirection(0x0102, 90, 400)
    ChrSetFlags(0x0102, 0x0020)
    ChrSetChipByIndex(0x0102, 4)
    Sleep(300)

    @scena.Lambda('lambda_0B17')
    def lambda_0B17():
        CameraMove(107720, -2420, 42540, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_0B17)

    PlaySE(146, 0x00, 0x64)
    PlayEffect(0x05, 0xFF, 0x000D, 0, -300, -1800, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_72(0x0003, 0x0020)
    OP_6F(0x0003, 240)
    OP_70(0x0003, 300)

    @scena.Lambda('lambda_0B7C')
    def lambda_0B7C():
        ChrMoveTo(0x000D, 77150, -3000, 39840, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_0B7C)

    Sleep(300)

    @scena.Lambda('lambda_0B9C')
    def lambda_0B9C():
        ChrMoveTo(0x000D, 77150, -3000, 39840, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_0B9C)

    OP_73(0x0003)
    OP_71(0x0003, 0x0020)
    OP_6F(0x0003, 301)
    OP_70(0x0003, 360)
    PlayEffect(0x04, 0xFF, 0x000D, 0, 50, 2700, 180, 0, 0, 1200, 500, 5000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_0C02')
    def lambda_0C02():
        ChrMoveTo(0x000D, 77150, -3000, 39840, 4500, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_0C02)

    Sleep(200)

    @scena.Lambda('lambda_0C22')
    def lambda_0C22():
        ChrMoveTo(0x000D, 77150, -3000, 39840, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_0C22)

    Sleep(200)

    @scena.Lambda('lambda_0C42')
    def lambda_0C42():
        ChrMoveTo(0x000D, 77150, -3000, 39840, 5500, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_0C42)

    Sleep(200)

    @scena.Lambda('lambda_0C62')
    def lambda_0C62():
        ChrMoveTo(0x000D, 77150, -3000, 39840, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_0C62)

    Sleep(200)

    @scena.Lambda('lambda_0C82')
    def lambda_0C82():
        ChrMoveTo(0x000D, 77150, -3000, 39840, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_0C82)

    Sleep(200)

    @scena.Lambda('lambda_0CA2')
    def lambda_0CA2():
        ChrMoveTo(0x000D, 77150, -3000, 39840, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_0CA2)

    Sleep(200)

    @scena.Lambda('lambda_0CC2')
    def lambda_0CC2():
        ChrMoveTo(0x000D, 77150, -3000, 39840, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_0CC2)

    Sleep(200)

    @scena.Lambda('lambda_0CE2')
    def lambda_0CE2():
        ChrMoveTo(0x000D, 77150, -3000, 39840, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0000, lambda_0CE2)

    ChrTalk(
        0x0009,
        (
            '#0270061743V#144F#5P喂———！\n',
            '让我也一起去呀～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007E, 0, 0x3F0))
    NewScene('ED6_DT01/T2100._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0008 offset: 0xD3B
@scena.Code('func_08_D3B')
def func_08_D3B():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_0D51')
    def lambda_0D51():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 300)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_0D51)

    ChrSetPos(0x00FE, 115970, 2150, 29130, 0)
    ChrWalkTo(0x00FE, 115970, 2150, 31170, 6000, 0x00)
    ChrWalkTo(0x00FE, 112520, 0, 31170, 6000, 0x00)
    ChrWalkTo(0x00FE, 112460, 0, 32740, 6000, 0x00)
    ChrWalkTo(0x00FE, 116970, 0, 34020, 6000, 0x00)
    ChrWalkTo(0x00FE, 116970, -1800, 36910, 6000, 0x00)
    ChrWalkTo(0x00FE, 114030, -1800, 39970, 4000, 0x00)
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetDirection(0x00FE, 270, 0)
    ChrJumpTo(0x00FE, 112250, -2910, 39670, 1000, 6000)
    ChrSetBattleFlags(0x00FE, 0x0020)
    ChrClearFlags(0x00FE, 0x0004)
    OP_89(0x00FE, 112250, 3000, 39670, 270)
    ChrSetDirection(0x00FE, 90, 400)
    Sleep(200)

    ChrSetDirection(0x00FE, 270, 400)
    PlaySE(146, 0x00, 0x64)
    PlayEffect(0x05, 0xFF, 0x000E, 0, -300, -3000, 180, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    OP_72(0x0002, 0x0020)
    OP_6F(0x0002, 240)
    OP_70(0x0002, 300)

    @scena.Lambda('lambda_0E8A')
    def lambda_0E8A():
        ChrMoveTo(0x000E, 77150, -3000, 39840, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0E8A)

    Sleep(300)

    @scena.Lambda('lambda_0EAA')
    def lambda_0EAA():
        ChrMoveTo(0x000E, 77150, -3000, 39840, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0EAA)

    OP_73(0x0002)
    OP_71(0x0002, 0x0020)
    OP_6F(0x0002, 301)
    OP_70(0x0002, 360)
    PlayEffect(0x04, 0xFF, 0x000E, 0, 50, 2700, 180, 0, 0, 1200, 500, 5000, 0x00FF, 0, 0, 0, 0)

    @scena.Lambda('lambda_0F10')
    def lambda_0F10():
        ChrMoveTo(0x000E, 77150, -3000, 39840, 4500, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0F10)

    Sleep(200)

    @scena.Lambda('lambda_0F30')
    def lambda_0F30():
        ChrMoveTo(0x000E, 77150, -3000, 39840, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0F30)

    Sleep(200)

    @scena.Lambda('lambda_0F50')
    def lambda_0F50():
        ChrMoveTo(0x000E, 77150, -3000, 39840, 5500, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0F50)

    Sleep(200)

    @scena.Lambda('lambda_0F70')
    def lambda_0F70():
        ChrMoveTo(0x000E, 77150, -3000, 39840, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0F70)

    Sleep(200)

    @scena.Lambda('lambda_0F90')
    def lambda_0F90():
        ChrMoveTo(0x000E, 77150, -3000, 39840, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0F90)

    Sleep(200)

    @scena.Lambda('lambda_0FB0')
    def lambda_0FB0():
        ChrMoveTo(0x000E, 77150, -3000, 39840, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0FB0)

    Sleep(200)

    @scena.Lambda('lambda_0FD0')
    def lambda_0FD0():
        ChrMoveTo(0x000E, 77150, -3000, 39840, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0FD0)

    Sleep(200)

    @scena.Lambda('lambda_0FF0')
    def lambda_0FF0():
        ChrMoveTo(0x000E, 77150, -3000, 39840, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0000, lambda_0FF0)

    Return()

# id: 0x0009 offset: 0x1006
@scena.Code('func_09_1006')
def func_09_1006():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_101C')
    def lambda_101C():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 300)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_101C)

    ChrSetPos(0x00FE, 115970, 2150, 29130, 0)
    ChrWalkTo(0x00FE, 116030, 2150, 31730, 6000, 0x00)
    ChrClearFlags(0x00FE, 0x0004)
    ChrJumpTo(0x00FE, 115860, 0, 32990, 1500, 5000)
    ChrSetFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, 116970, 0, 34020, 5000, 0x00)
    ChrWalkTo(0x00FE, 116970, -1800, 36910, 5000, 0x00)
    ChrWalkTo(0x00FE, 114850, -1800, 39970, 5000, 0x00)
    ChrSetDirection(0x0101, 270, 0)
    Sleep(800)

    ChrWalkTo(0x00FE, 114300, -1800, 44650, 5000, 0x00)
    ChrWalkTo(0x00FE, 111200, -1800, 44650, 5000, 0x00)
    ChrSetFlags(0x00FE, 0x0004)
    ChrJumpTo(0x00FE, 109680, -2710, 42810, 1000, 5000)
    ChrClearFlags(0x00FE, 0x0004)
    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 3)

    Return()

# id: 0x000A offset: 0x110A
@scena.Code('func_0A_110A')
def func_0A_110A():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_1120')
    def lambda_1120():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 300)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1120)

    ChrSetPos(0x00FE, 115970, 2150, 29130, 0)
    ChrWalkTo(0x00FE, 116030, 2150, 31730, 6000, 0x00)
    ChrSetFlags(0x00FE, 0x0004)
    ChrJumpTo(0x00FE, 115860, 0, 32990, 1500, 5000)
    ChrClearFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, 116970, 0, 34020, 5000, 0x00)
    ChrWalkTo(0x00FE, 116970, -1800, 36910, 5000, 0x00)
    ChrWalkTo(0x00FE, 115820, -1800, 41930, 5000, 0x00)
    ChrWalkTo(0x00FE, 114230, -1800, 42720, 5000, 0x00)
    ChrSetFlags(0x00FE, 0x0004)
    ChrSetDirection(0x00FE, 270, 0)
    ChrJumpTo(0x00FE, 111940, -2800, 42720, 1000, 5000)
    ChrClearFlags(0x00FE, 0x0004)

    Return()

# id: 0x000B offset: 0x11EB
@scena.Code('func_0B_11EB')
def func_0B_11EB():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_1201')
    def lambda_1201():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 300)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1201)

    ChrSetPos(0x00FE, 115970, 2150, 29130, 0)
    ChrWalkTo(0x00FE, 116030, 2150, 31730, 5000, 0x00)
    ChrSetFlags(0x00FE, 0x0004)
    ChrJumpTo(0x00FE, 116190, 2720, 31990, 600, 5000)
    ChrJumpTo(0x00FE, 115860, 0, 32990, 600, 5000)
    ChrClearFlags(0x00FE, 0x0004)
    ChrWalkTo(0x00FE, 116970, 0, 34020, 5000, 0x00)
    ChrWalkTo(0x00FE, 116970, -1800, 36910, 5000, 0x00)
    ChrWalkTo(0x00FE, 114300, -1800, 44650, 5000, 0x00)
    ChrWalkTo(0x00FE, 111200, -1800, 44650, 5000, 0x00)
    ChrSetFlags(0x00FE, 0x0004)
    ChrJumpTo(0x00FE, 110870, -2800, 42720, 1000, 5000)
    ChrClearFlags(0x00FE, 0x0004)
    ChrSetFlags(0x00FE, 0x0020)
    ChrSetChipByIndex(0x00FE, 5)

    Return()

# id: 0x000C offset: 0x12E6
@scena.Code('func_0C_12E6')
def func_0C_12E6():
    ChrClearFlags(0x00FE, 0x0080)
    ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_12FC')
    def lambda_12FC():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 300)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_12FC)

    ChrSetPos(0x00FE, 115970, 2150, 29130, 0)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x00FE, 115970, 2150, 31170, 4000, 0x00)
    ChrWalkTo(0x00FE, 112520, 0, 31170, 4000, 0x00)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x00FE, 112460, 0, 32740, 4000, 0x00)
    ChrWalkTo(0x00FE, 116970, 0, 34020, 4000, 0x00)
    OP_62(0x00FE, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    ChrWalkTo(0x00FE, 116970, -1800, 36910, 4000, 0x00)
    ChrWalkTo(0x00FE, 114230, -1800, 42720, 4000, 0x00)
    ChrSetDirection(0x00FE, 270, 400)
    OP_62(0x00FE, 0x00000000, 2000, 0x0C, 0x0D, 0x000000FA, 0x02)
    PlaySE(49, 0x00, 0x64)
    ChrJumpToRelative(0x00FE, 0, 0, 0, 500, 7000)
    ChrJumpToRelative(0x00FE, 0, 0, 0, 500, 7000)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
