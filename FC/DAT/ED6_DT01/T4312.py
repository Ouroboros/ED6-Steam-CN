import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4312_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4312   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '特务兵'),
    TXT(0x02, '特务兵'),
    TXT(0x03, '特务兵'),
    TXT(0x04, '特务兵'),
    TXT(0x05, '中队长'),
    TXT(0x06, '莉安妮'),
    TXT(0x07, '基库'),
    TXT(0x08, '奈尔'),
    TXT(0x09, '科洛蒂娅公主'),
    TXT(0x0A, '尤莉亚中尉'),
    TXT(0x0B, '雪拉'),
    TXT(0x0C, '奥利维尔'),
    TXT(0x0D, '卡露娜'),
    TXT(0x0E, '亚妮拉丝'),
    TXT(0x0F, '库拉茨'),
    TXT(0x10, '克鲁茨'),
    TXT(0x11, '亲卫队员'),
    TXT(0x12, '亲卫队员'),
    TXT(0x13, '亲卫队员'),
    TXT(0x14, '亲卫队员'),
    TXT(0x15, '亲卫队员'),
    TXT(0x16, '亲卫队员'),
    TXT(0x17, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4312.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x3B0E
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
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00170._CH', 'ED6_DT07/CH00170P._CP'),
        ('ED6_DT07/CH00171._CH', 'ED6_DT07/CH00171P._CP'),
        ('ED6_DT07/CH00340._CH', 'ED6_DT07/CH00340P._CP'),
        ('ED6_DT07/CH00341._CH', 'ED6_DT07/CH00341P._CP'),
        ('ED6_DT07/CH00440._CH', 'ED6_DT07/CH00440P._CP'),
        ('ED6_DT07/CH01480._CH', 'ED6_DT07/CH01480P._CP'),
        ('ED6_DT07/CH02320._CH', 'ED6_DT07/CH02320P._CP'),
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH02340._CH', 'ED6_DT07/CH02340P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
        ('ED6_DT07/CH00030._CH', 'ED6_DT07/CH00030P._CP'),
        ('ED6_DT07/CH00122._CH', 'ED6_DT07/CH00122P._CP'),
        ('ED6_DT07/CH00444._CH', 'ED6_DT07/CH00444P._CP'),
        ('ED6_DT07/CH00443._CH', 'ED6_DT07/CH00443P._CP'),
        ('ED6_DT07/CH01240._CH', 'ED6_DT07/CH01240P._CP'),
        ('ED6_DT07/CH01630._CH', 'ED6_DT07/CH01630P._CP'),
        ('ED6_DT07/CH01260._CH', 'ED6_DT07/CH01260P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT07/CH01320._CH', 'ED6_DT07/CH01320P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
    ]

# id: 0x10002 offset: 0x172
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 7,
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
            dword_10            = 7,
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
            dword_10            = 7,
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
            dword_10            = 7,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
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
            dword_10            = 10,
            chipIndex           = 10,
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
            dword_10            = 11,
            chipIndex           = 11,
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
            dword_10            = 12,
            chipIndex           = 12,
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
            dword_10            = 13,
            chipIndex           = 13,
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
            dword_10            = 14,
            chipIndex           = 14,
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
            dword_10            = 15,
            chipIndex           = 15,
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
            dword_10            = 19,
            chipIndex           = 19,
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
            dword_10            = 20,
            chipIndex           = 20,
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
            dword_10            = 21,
            chipIndex           = 21,
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
            dword_10            = 23,
            chipIndex           = 23,
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
            dword_10            = 23,
            chipIndex           = 23,
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
            dword_10            = 23,
            chipIndex           = 23,
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
            dword_10            = 23,
            chipIndex           = 23,
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
            dword_10            = 23,
            chipIndex           = 23,
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
            dword_10            = 23,
            chipIndex           = 23,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x432
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x432
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -57400,
            y           = 1000,
            z           = 2550,
            range       = -43640,
            dword_10    = 0xFFFFFC18,
            dword_14    = 0xFFFFFCCC,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000003,
        ),
    )

# id: 0x10005 offset: 0x452
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x452
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_460',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0002)

    def _loc_460(): pass

    label('loc_460')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_477',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x65),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x0006)

    def _loc_477(): pass

    label('loc_477')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000069, 'loc_483'),
        (-1, 'loc_499'),
    )

    def _loc_483(): pass

    label('loc_483')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 1, 0x659)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 0, 0x658)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_496',
    )

    SetScenaFlags(ScenaFlag(0x00CB, 1, 0x659))
    Event(0, 0x0005)

    def _loc_496(): pass

    label('loc_496')

    Jump('loc_499')

    def _loc_499(): pass

    label('loc_499')

    ExecExpressionWithValue(
        0x000E,
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

# id: 0x0001 offset: 0x4AB
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 0, 0x658)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4BD',
    )

    OP_1C(0x01, 0x00, 0x0004)
    OP_72(0x0001, 0x0010)

    def _loc_4BD(): pass

    label('loc_4BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 1, 0x659)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4CA',
    )

    OP_1B(0x00, 0x00, 0x0007)

    def _loc_4CA(): pass

    label('loc_4CA')

    Return()

# id: 0x0002 offset: 0x4CB
@scena.Code('ReInit')
def ReInit():
    EventBegin(0x00)
    CameraMove(640, 0, -4630, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0102, 2)
    SetChrChipByIndex(0x0108, 4)
    SetChrPos(0x0108, 190, 0, -7530, 0)
    SetChrPos(0x0101, -1330, 0, -8480, 0)
    SetChrPos(0x0102, 570, 0, -8760, 0)

    ChrTalk(
        0x0101,
        (
            '#000F这里就是『艾尔贝离宫』……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130593V唔－嗯，与城里\n',
            '相比也不惶多让的豪华啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130594V#010F啊，因为是王家的建筑嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x0008, 11320, 0, -6220, 257)
    SetChrPos(0x0009, 12050, 0, -5100, 264)
    SetChrPos(0x000A, 12230, 0, -6940, 276)
    SetChrPos(0x000B, 13520, 0, -5780, 285)
    ChrTurnDirection(0x0108, 0x0008, 400)

    ChrTalk(
        0x0108,
        (
            '#070F好的，冲进去！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0649')
    def lambda_0649():
        ChrTurnDirection(0x00FE, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0649)

    @scena.Lambda('lambda_0657')
    def lambda_0657():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0657)

    @scena.Lambda('lambda_0665')
    def lambda_0665():
        CameraMove(5840, 0, -6950, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0665)

    @scena.Lambda('lambda_067D')
    def lambda_067D():
        OP_67(0, 4710, -10000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_067D)

    @scena.Lambda('lambda_0695')
    def lambda_0695():
        OP_6C(68000, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0695)

    ChrTalk(
        0x0008,
        (
            '#2620130596V你、你们是什么人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0101, -700, 0, -6920, 5000, 0x00)
    ChrWalkTo(0x0101, 790, 0, -6100, 5000, 0x00)
    ChrTurnDirection(0x0101, 0x0009, 0)

    ChrTalk(
        0x0101,
        (
            '#000F你们这些坏人不配知道！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F不必多言，\n',
            '我们上！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0734')
    def lambda_0734():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002710, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0734)

    @scena.Lambda('lambda_074A')
    def lambda_074A():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002710, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_074A)

    @scena.Lambda('lambda_0760')
    def lambda_0760():
        OP_94(0x00, 0x00FE, 0x0000, 0x00002710, 0x00001B58, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0760)

    CameraMove(10400, 0, -6130, 700)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    Battle(0x000003AD, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_7A6'),
        (-1, 'loc_7A9'),
    )

    def _loc_7A6(): pass

    label('loc_7A6')

    OP_B4(0x00)

    Return()

    def _loc_7A9(): pass

    label('loc_7A9')

    EventBegin(0x00)
    CameraMove(9140, 0, -6380, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(44000, 0)
    OP_6E(280, 0)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    SetChrPos(0x0101, 9260, 0, -5570, 81)
    SetChrPos(0x0108, 10200, 0, -6390, 96)
    SetChrPos(0x0102, 8460, 0, -7540, 100)
    Sleep(500)

    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#000F嗯，公主殿下她们\n',
            '被关在哪里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#010F肯定在这个巨大的建筑里面。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130601V一个不漏的\n',
            '进行调查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0108, 270, 400)

    ChrTalk(
        0x0108,
        (
            '#070F如果再磨磨蹭蹭的话，\n',
            '前庭的那些家伙就会赶来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130603V尽快行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    EventEnd(0x00)

    Return()

# id: 0x0003 offset: 0x901
@scena.Code('func_03_901')
def func_03_901():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 4, 0x654)),
            Expr.Return,
        ),
        'loc_909',
    )

    Return()

    def _loc_909(): pass

    label('loc_909')

    SetScenaFlags(ScenaFlag(0x00CA, 4, 0x654))
    EventBegin(0x00)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    SetChrPos(0x0008, -52180, 0, 20500, 180)
    SetChrPos(0x0009, -50170, 0, 20530, 180)
    OP_62(0x0000, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_0957')
    def lambda_0957():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0957)

    @scena.Lambda('lambda_0965')
    def lambda_0965():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0965)

    @scena.Lambda('lambda_0973')
    def lambda_0973():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0973)

    CameraMove(-50570, 0, 17760, 2000)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0102, 2)
    SetChrChipByIndex(0x0108, 4)
    SetChrPos(0x0108, -50910, 0, 8080, 0)
    SetChrPos(0x0102, -50140, 0, 6930, 0)
    SetChrPos(0x0101, -52160, 0, 7020, 0)

    @scena.Lambda('lambda_09D4')
    def lambda_09D4():
        ChrWalkTo(0x00FE, -51000, 0, 13780, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_09D4)

    @scena.Lambda('lambda_09EF')
    def lambda_09EF():
        ChrWalkTo(0x00FE, -51970, 0, 12510, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_09EF)

    @scena.Lambda('lambda_0A0A')
    def lambda_0A0A():
        ChrWalkTo(0x00FE, -50210, 0, 12920, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0A0A)

    ChrTalk(
        0x0008,
        (
            '你们是什么人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '好像在哪儿见过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是他们！\n',
            '武术大会取得优胜的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '游击士那些家伙！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0081040028V#070F真聪明。\n',
            '为了奖励你们，就让你们尝尝我拳头的滋味吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0AD5')
    def lambda_0AD5():
        ChrWalkTo(0x00FE, -51080, 0, 39570, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0AD5)

    @scena.Lambda('lambda_0AF0')
    def lambda_0AF0():
        ChrWalkTo(0x00FE, -51080, 0, 39570, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0AF0)

    @scena.Lambda('lambda_0B0B')
    def lambda_0B0B():
        ChrWalkTo(0x00FE, -51080, 0, 39570, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0B0B)

    CameraMove(-51250, 0, 20190, 500)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x0102, 0xFF)
    Battle(0x000003AE, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_B56'),
        (-1, 'loc_B59'),
    )

    def _loc_B56(): pass

    label('loc_B56')

    OP_B4(0x00)

    Return()

    def _loc_B59(): pass

    label('loc_B59')

    EventBegin(0x00)
    CameraMove(-48790, 0, 18830, 0)
    SetChrPos(0x0008, -53840, 0, 18820, 298)
    SetChrPos(0x0009, -53890, 0, 17410, 315)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)
    SetChrPos(0x0101, -50330, 0, 18280, 295)
    SetChrPos(0x0108, -50350, 0, 16900, 285)
    SetChrPos(0x0102, -49040, 0, 18430, 283)

    ChrTalk(
        0x0101,
        (
            '#000F呼，解决掉一批。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '看起来，他们好像是在\n',
            '守卫这个豪华的大门……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0C1E')
    def lambda_0C1E():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_0C1E)

    SetChrDirection(0x0102, 315, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 6, 0x656)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C76',
    )

    ChrTalk(
        0x0102,
        (
            '#010F嗯……\n',
            '里面大概有什么重要的东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '进去调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CBA')

    def _loc_C76(): pass

    label('loc_C76')

    ChrTalk(
        0x0102,
        (
            '#010F这个就是管家先生说的\n',
            '那个大房间的门吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '进去调查一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CBA(): pass

    label('loc_CBA')

    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0xCBD
@scena.Code('func_04_CBD')
def func_04_CBD():
    SetMapFlags(0x00000080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 5, 0x655)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DEB',
    )

    SetScenaFlags(ScenaFlag(0x00CA, 5, 0x655))
    EventBegin(0x00)
    ChrTurnDirectionByPos(0x0000, -50950, 22020, 400)
    ChrTurnDirectionByPos(0x0001, -50950, 22020, 400)
    ChrTurnDirectionByPos(0x0002, -50950, 22020, 400)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0101,
        (
            '#000F唉～怎么会这样！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F真是相当坚固的锁呢……\n',
            '得先找到钥匙才行呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 6, 0x656)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DB1',
    )

    ChrTalk(
        0x0108,
        (
            '#070F唔，那就只能暂时\n',
            '先到别的地方看看了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_DE6')

    def _loc_DB1(): pass

    label('loc_DB1')

    ChrTalk(
        0x0108,
        (
            '#0080130619V#070F唔，去问问那个\n',
            '年轻的管家吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x004C, 0x01, 0x0008)

    def _loc_DE6(): pass

    label('loc_DE6')

    EventEnd(0x01)

    Jump('loc_E76')

    def _loc_DEB(): pass

    label('loc_DEB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CA, 7, 0x657)),
            Expr.Return,
        ),
        'loc_E3A',
    )

    ChrTurnDirectionByPos(0x0000, -50950, 22020, 400)
    SetScenaFlags(ScenaFlag(0x00CB, 0, 0x658))
    OP_71(0x0001, 0x0010)
    OP_1C(0x01, 0x00, 0xFFFF)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '使用了备用钥匙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    Jump('loc_E76')

    def _loc_E3A(): pass

    label('loc_E3A')

    ChrTurnDirectionByPos(0x0000, -50950, 22020, 400)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '门上着锁，无法打开。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    def _loc_E76(): pass

    label('loc_E76')

    ClearMapFlags(0x00000080)

    Return()

# id: 0x0005 offset: 0xE7C
@scena.Code('func_05_E7C')
def func_05_E7C():
    EventBegin(0x00)
    CameraMove(-20, 0, 54380, 0)
    OP_67(0, 6000, -10000, 0)
    CameraSetDistance(3000, 0)
    OP_6C(57000, 0)
    OP_6E(280, 0)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    SetChrPos(0x0010, 50, 250, 68860, 180)
    SetChrPos(0x000D, 5680, 0, 58650, 180)
    SetChrPos(0x000F, 3070, 0, 58560, 249)
    SetChrChipByIndex(0x0101, 0)
    SetChrChipByIndex(0x0102, 2)
    SetChrChipByIndex(0x0108, 4)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0108, 255, 255, 255, 0, 0)
    SetChrPos(0x0101, -110, 0, 50960, 0)
    SetChrPos(0x0102, -110, 0, 50960, 0)
    SetChrPos(0x0108, -110, 0, 50960, 0)
    SetChrPos(0x000E, -110, 0, 50960, 0)
    SetChrPos(0x0013, -110, 0, 50960, 0)
    SetChrPos(0x0011, -110, 0, 50960, 0)
    SetChrPos(0x0012, -110, 0, 50960, 0)

    @scena.Lambda('lambda_0FAA')
    def lambda_0FAA():
        CameraMove(750, 0, 56890, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_0FAA)

    @scena.Lambda('lambda_0FC2')
    def lambda_0FC2():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_0FC2)

    @scena.Lambda('lambda_0FD4')
    def lambda_0FD4():
        ChrWalkTo(0x00FE, -60, 0, 57340, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0FD4)

    Sleep(500)

    @scena.Lambda('lambda_0FF4')
    def lambda_0FF4():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_0FF4)

    @scena.Lambda('lambda_1006')
    def lambda_1006():
        ChrWalkTo(0x00FE, 770, 0, 56300, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1006)

    Sleep(500)

    @scena.Lambda('lambda_1026')
    def lambda_1026():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_1026)

    @scena.Lambda('lambda_1038')
    def lambda_1038():
        ChrWalkTo(0x00FE, -950, 0, 55860, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1038)

    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x000F,
        (
            '#140F你、你们……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1073')
    def lambda_1073():
        CameraMove(2460, 0, 58180, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1073)

    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0108, 65535)

    @scena.Lambda('lambda_109A')
    def lambda_109A():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_109A)

    @scena.Lambda('lambda_10A8')
    def lambda_10A8():
        ChrTurnDirection(0x00FE, 0x000F, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_10A8)

    ChrTurnDirection(0x0101, 0x000F, 400)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#000F呀呵～我们来救你们了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130707V#010F奈尔先生，\n',
            '看起来安然无恙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#140F来救我们的，真的！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0060130709V艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0060130710V没想到能在这里相会……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1173')
    def lambda_1173():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1173)

    @scena.Lambda('lambda_1181')
    def lambda_1181():
        ChrTurnDirection(0x00FE, 0x0010, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1181)

    ChrTurnDirection(0x0101, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#000F……嗯？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_11A9')
    def lambda_11A9():
        CameraMove(70, 250, 68760, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_11A9)

    @scena.Lambda('lambda_11C1')
    def lambda_11C1():
        OP_67(0, 4420, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_11C1)

    @scena.Lambda('lambda_11D9')
    def lambda_11D9():
        OP_6C(11000, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_11D9)

    Sleep(1500)

    @scena.Lambda('lambda_11EE')
    def lambda_11EE():
        ChrWalkTo(0x00FE, -540, 0, 66590, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_11EE)

    Sleep(100)

    @scena.Lambda('lambda_120E')
    def lambda_120E():
        ChrWalkTo(0x00FE, 490, 0, 66590, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_120E)

    Sleep(300)

    @scena.Lambda('lambda_122E')
    def lambda_122E():
        ChrWalkTo(0x00FE, -2330, 0, 66150, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_122E)

    Sleep(100)

    @scena.Lambda('lambda_124E')
    def lambda_124E():
        ChrWalkTo(0x00FE, 2220, 0, 66920, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_124E)

    @scena.Lambda('lambda_1269')
    def lambda_1269():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_1269')

    DispatchAsync2(0x0108, 0x0001, lambda_1269)

    @scena.Lambda('lambda_127A')
    def lambda_127A():
        ChrTurnDirection(0x00FE, 0x0010, 0)
        Yield()

        Jump('lambda_127A')

    DispatchAsync2(0x000F, 0x0001, lambda_127A)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#000F您、您就是公主殿下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '初次见面，我们是\n',
            '游击士协会的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0060940017V不是初次见面呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '艾丝蒂尔、约修亚。\n',
            '终于按照约定再会了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎……？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130717V……………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#000F啊啊，你不是科洛丝吗！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#040F艾丝蒂尔你真是的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130720V虽没有立刻察觉，\n',
            '但也不至于那么惊讶嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F话、话虽这么说，\n',
            '可是身着礼服，长发披肩……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '究竟是怎么回事呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……对不起呢，科洛丝。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130724V艾丝蒂尔这个人\n',
            '没有什么疑心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F我说！\n',
            '你那是什～么意思！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#040F呵呵，我认为那是艾丝蒂尔\n',
            '的一个优点哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对了，约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130728V请依旧称呼我……\n',
            '那个名字好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯，我也感觉\n',
            '你希望如此。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130730V不用本名可以吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#040F完全可以呀……\n',
            '谢谢，我好开心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150088V#000F？？？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130733V话说回来，为什么\n',
            '科洛丝会在这里呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130734V还有，原本应该在这儿的公主殿下\n',
            '为何到处都没有看见呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#140F我说啊，不就在你的面前吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这位就是陛下的孙女，\n',
            '科洛蒂娅公主殿下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_162F')
    def lambda_162F():
        OP_67(0, 6000, -10000, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_162F)

    OP_6C(45000, 1500)

    ChrTalk(
        0x0101,
        (
            '#000F…………哦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '………………………………\n',
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F#10A啊啊啊啊啊啊？',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_6E(253, 1000)
    TerminateThread(0x0108, 0xFF)
    TerminateThread(0x000F, 0xFF)

    ChrTalk(
        0x0010,
        (
            '对不起呀，我一直没说……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0060940018V我本来打算与艾丝蒂尔\n',
            '你们在王都再会的时候\n',
            '告诉你们的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0060940019V结果被情报部的人拘捕了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F可、可是，为什么？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130743V为什么公主殿下要藏身\n',
            '于一个普通的学校呢……！？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130744V而、而且我们称呼\n',
            '你科洛丝，这可以吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '以后也请务必\n',
            '叫我科洛丝。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '科洛蒂娅·\n',
            '冯·奥赛雷丝……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0060940020V乔儿把我本名的开始和末尾放在一起，\n',
            '给我起了这样一个爱称。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F是这样啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130749V嗯，那么头发呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '啊，这是假发。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0060130751V如果真的是这种发型，\n',
            '在学院里面的生活就不方便了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000F,
        (
            '#140F我也有够粗心的了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270130753V虽然以前看过您的照片，\n',
            '但在市长官邸事件中见到您时\n',
            '竟然完全没有注意到。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0060940021V呵呵，对不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0060940022V杜南王叔和戴尔蒙市长\n',
            '都没有察觉，\n',
            '真是有些意外的效果呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哦，说起来\n',
            '那个公爵还是你的亲戚呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '嗯，对了。\n',
            '最重要的事情反而忘记了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_92(0x0101, 0x0010, 700, 3000, 0x00)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '把至今为止的事情经过一一道来，\n',
            '也说明了接受女王的委托\n',
            '前来营救的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    ChrMoveTo(0x0101, -540, 0, 66590, 2000, 0x00)

    ChrTalk(
        0x0010,
        (
            '是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '艾丝蒂尔、约修亚。\n',
            '还有那位金大哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '你们能来营救我们，\n',
            '真是太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊哈哈，不用那么在意啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130762V如果知道被拘捕的\n',
            '是科洛丝的话，\n',
            '就算不委托我们也会来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0060940023V艾丝蒂尔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F哈哈，的确如此呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '与我们相比，\n',
            '更应该感谢的是陛下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '她不顾自己的所处的境况\n',
            '也要委托我们来救你。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0081040029V#070F的确，公主殿下既然已经平安无事，\n',
            '那么陛下就可以拒绝上校的要求了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0081040030V也许陛下已经视死如归了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '好……\n',
            '祖母大人就是那样的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0060130770V无论如何也不会妥协，\n',
            '可是这样祖母大人她……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x000D, -230, 0, 55310, 346)
    SetChrChipByIndex(0x0008, 8)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x0008, 0x0080)
    SetChrPos(0x000C, 1020, 0, 56140, 0)
    SetChrPos(0x0008, 50, 0, 54770, 0)

    ChrTalk(
        0x000C,
        (
            '所谓闹剧，就是\n',
            '这样的吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1D0A')
    def lambda_1D0A():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1D0A)

    @scena.Lambda('lambda_1D18')
    def lambda_1D18():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1D18)

    @scena.Lambda('lambda_1D26')
    def lambda_1D26():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1D26)

    @scena.Lambda('lambda_1D34')
    def lambda_1D34():
        ChrTurnDirection(0x00FE, 0x000C, 400)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_1D34)

    @scena.Lambda('lambda_1D42')
    def lambda_1D42():
        CameraMove(800, 0, 61890, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1D42)

    @scena.Lambda('lambda_1D5A')
    def lambda_1D5A():
        OP_6E(297, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1D5A)

    Sleep(2000)

    ChrTalk(
        0x000D,
        (
            '公、公主殿下～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '小莉安妮！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1D99')
    def lambda_1D99():
        CameraMove(850, 0, 60760, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1D99)

    @scena.Lambda('lambda_1DB1')
    def lambda_1DB1():
        OP_6E(261, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1DB1)

    SetChrChipByIndex(0x0101, 0)

    @scena.Lambda('lambda_1DC6')
    def lambda_1DC6():
        ChrWalkTo(0x00FE, -730, 0, 63960, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1DC6)

    Sleep(200)

    SetChrChipByIndex(0x0102, 2)

    @scena.Lambda('lambda_1DEB')
    def lambda_1DEB():
        ChrWalkTo(0x00FE, 400, 0, 63850, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1DEB)

    Sleep(100)

    SetChrChipByIndex(0x0108, 4)

    @scena.Lambda('lambda_1E10')
    def lambda_1E10():
        ChrWalkTo(0x00FE, -2420, 0, 62980, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1E10)

    Sleep(200)

    @scena.Lambda('lambda_1E30')
    def lambda_1E30():
        ChrWalkTo(0x00FE, 10, 0, 65519, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_1E30)

    WaitForThreadExit(0x0101, 0x0002)
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#000F那、那个小女孩是谁！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0010, 0x0001)

    ChrTalk(
        0x0010,
        (
            '摩尔根将军的孙女……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0060130776V为了动摇囚禁在哈肯大门\n',
            '的将军的意志，\n',
            '而被带到这里来的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F你们的所作所为\n',
            '是在与女王陛下作对……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '你说的我收下了，\n',
            '但是不要以为这样就可以威胁我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '我们情报部的队员，为了理想，\n',
            '就算化成鬼、化成修罗也在所不惜！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F这、这种事\n',
            '还有脸自吹自擂！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '中队长，我和你做一笔交易。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0060130782V请让我代替那个\n',
            '孩子，作为人质。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '哦……\n',
            '我才不会上当呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '对于我们这些人而言，\n',
            '是没有亲手杀死王族的勇气的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '与之相比，摩尔根将军的\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '既有作为人质的价值，\n',
            '要打伤她又不会很难下手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0060940024V……你们…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F……无耻～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F哎呀呀，无可救药的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '哼，随便你们怎么胡说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '很快就要到巡回部队\n',
            '从队空中庭园归来的时刻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '到时候会把亲卫队还有游击士\n',
            '在这儿一网打尽！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '啊～那已经不可能了哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '他们在来这儿的途中\n',
            '就已经被我们全部消灭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_21D4')
    def lambda_21D4():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_21D4)

    @scena.Lambda('lambda_21E2')
    def lambda_21E2():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_21E2)

    @scena.Lambda('lambda_21F0')
    def lambda_21F0():
        ChrTurnDirection(0x00FE, 0x0012, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_21F0)

    @scena.Lambda('lambda_21FE')
    def lambda_21FE():
        CameraMove(500, 0, 59390, 800)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_21FE)

    OP_6E(280, 800)

    @scena.Lambda('lambda_221F')
    def lambda_221F():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_221F')

    DispatchAsync2(0x000C, 0x0001, lambda_221F)

    @scena.Lambda('lambda_2230')
    def lambda_2230():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_2230')

    DispatchAsync2(0x0008, 0x0001, lambda_2230)

    @scena.Lambda('lambda_2241')
    def lambda_2241():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_2241')

    DispatchAsync2(0x000D, 0x0001, lambda_2241)

    SetChrFlags(0x0008, 0x0020)
    SetChrFlags(0x000C, 0x0020)
    SetChrFlags(0x0012, 0x0020)

    ExecExpressionWithValue(
        0x0012,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0012, 16)
    ClearChrFlags(0x0012, 0x0080)

    @scena.Lambda('lambda_2276')
    def lambda_2276():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_2276')

    DispatchAsync2(0x0012, 0x0001, lambda_2276)

    ChrJumpTo(0x0012, -2140, 0, 54720, 1000, 8000)
    OP_99(0x0012, 0x02, 0x04, 3000)
    PlayEffect(0x08, 0xFF, 0x00FF, 50, 1000, 54770, 0, 0, 0, 400, 400, 400, 0x00FF, 0, 0, 0, 0)
    ChrTurnDirection(0x0008, 0x0012, 0)

    ExecExpressionWithValue(
        0x0008,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0008, 18)

    @scena.Lambda('lambda_22F3')
    def lambda_22F3():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000BB8, 0x00002AF8, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_22F3)

    OP_99(0x0012, 0x04, 0x09, 3000)
    TerminateThread(0x000D, 0xFF)
    TerminateThread(0x0008, 0xFF)

    ChrTalk(
        0x0008,
        (
            '#10A啊！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    WaitForThreadExit(0x0008, 0x0001)
    SetChrChipByIndex(0x0008, 17)

    @scena.Lambda('lambda_2332')
    def lambda_2332():
        OP_99(0x00FE, 0x00, 0x03, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_2332)

    Sleep(500)

    @scena.Lambda('lambda_2347')
    def lambda_2347():
        ChrWalkTo(0x00FE, -2850, 0, 55570, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2347)

    Sleep(100)

    ChrMoveTo(0x000C, 1740, 0, 56010, 5000, 0x00)
    WaitForThreadExit(0x000D, 0x0001)
    ChrJumpTo(0x0012, -1960, 0, 55830, 500, 8000)
    ChrTurnDirection(0x000D, 0x0012, 400)
    Sleep(200)

    ChrTalk(
        0x000C,
        (
            '什么……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '呜……呜呜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '呜哇哇啊啊啊啊啊啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_23E3')
    def lambda_23E3():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_23E3')

    DispatchAsync2(0x0101, 0x0001, lambda_23E3)

    @scena.Lambda('lambda_23F4')
    def lambda_23F4():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_23F4')

    DispatchAsync2(0x0102, 0x0001, lambda_23F4)

    @scena.Lambda('lambda_2405')
    def lambda_2405():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_2405')

    DispatchAsync2(0x0108, 0x0001, lambda_2405)

    @scena.Lambda('lambda_2416')
    def lambda_2416():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_2416')

    DispatchAsync2(0x000F, 0x0001, lambda_2416)

    @scena.Lambda('lambda_2427')
    def lambda_2427():
        ChrTurnDirection(0x00FE, 0x0012, 0)
        Yield()

        Jump('lambda_2427')

    DispatchAsync2(0x0010, 0x0001, lambda_2427)

    ChrTalk(
        0x0012,
        (
            '#020F好了好了，已经没事了哟。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '艾丝蒂尔、约修亚。\n',
            '真是好久不见了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F雪、雪拉姐姐！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F终于来了吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '哪、哪里有这么\n',
            '慢条斯理的打招呼！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '哎哟哟，简直不解风情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlayEffect(0x08, 0xFF, 0x00FF, 1590, 1000, 54930, 0, 0, 0, 400, 400, 400, 0x00FF, 0, 0, 0, 0)

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x000C, 18)

    @scena.Lambda('lambda_253E')
    def lambda_253E():
        ChrJumpTo(0x00FE, 3030, 0, 57340, 2000, 3000)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_253E)

    ChrTalk(
        0x000C,
        (
            '#2680130805V#10A呜哦……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    Sleep(400)

    @scena.Lambda('lambda_257A')
    def lambda_257A():
        ChrTurnDirection(0x00FE, 0x000C, 0)
        Yield()

        Jump('lambda_257A')

    DispatchAsync2(0x0012, 0x0001, lambda_257A)

    ExecExpressionWithValue(
        0x0012,
        0x08,
        (
            (Expr.PushLong, 0x2),
            Expr.Nop,
            Expr.Return,
        ),
    )

    @scena.Lambda('lambda_2596')
    def lambda_2596():
        ChrJumpTo(0x00FE, 1090, 0, 56780, 1000, 5000)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_2596)

    Sleep(200)

    OP_99(0x0012, 0x02, 0x04, 4000)
    PlayEffect(0x08, 0xFF, 0x00FF, 3180, 1500, 56940, 0, 0, 0, 400, 400, 400, 0x00FF, 0, 0, 0, 0)
    SetChrFlags(0x000C, 0x0004)

    @scena.Lambda('lambda_25FC')
    def lambda_25FC():
        CameraMove(6320, 0, 57730, 1000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_25FC)

    @scena.Lambda('lambda_2614')
    def lambda_2614():
        ChrMoveTo(0x00FE, 9480, 500, 56550, 12000, 0x00)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2614)

    OP_99(0x0012, 0x04, 0x09, 2000)
    WaitForThreadExit(0x000C, 0x0001)

    ExecExpressionWithValue(
        0x000C,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x000C, 17)

    ChrTalk(
        0x000C,
        (
            '#2680130806V#10A呜啊！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    PlayEffect(0x12, 0xFF, 0x000C, 0, 0, -500, 0, 0, 0, 2000, 2000, 2000, 0x00FF, 0, 0, 0, 0)
    CameraSetDistance(3070, 0)
    CameraSetDistance(3000, 80)
    Sleep(500)

    ChrMoveTo(0x000C, 9490, 0, 56550, 1000, 0x00)
    OP_99(0x000C, 0x00, 0x03, 2000)

    ChrTalk(
        0x0012,
        (
            '#0030840025V#020F刚才那是附赠品哟。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    CameraMove(280, 0, 58100, 2000)

    ChrTalk(
        0x0101,
        (
            '#000F好、好狠啊～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '咦，刚才发起攻击的是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……奥利维尔吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ExecExpressionWithValue(
        0x0012,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    SetChrChipByIndex(0x0012, 14)
    ChrTurnDirection(0x0012, 0x0013, 400)

    ChrTalk(
        0x0013,
        (
            'Bingo⊙',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2772')
    def lambda_2772():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_2772')

    DispatchAsync2(0x0012, 0x0001, lambda_2772)

    @scena.Lambda('lambda_2783')
    def lambda_2783():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_2783')

    DispatchAsync2(0x000D, 0x0001, lambda_2783)

    @scena.Lambda('lambda_2794')
    def lambda_2794():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_2794')

    DispatchAsync2(0x0101, 0x0001, lambda_2794)

    @scena.Lambda('lambda_27A5')
    def lambda_27A5():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_27A5')

    DispatchAsync2(0x0102, 0x0001, lambda_27A5)

    @scena.Lambda('lambda_27B6')
    def lambda_27B6():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_27B6')

    DispatchAsync2(0x0108, 0x0001, lambda_27B6)

    @scena.Lambda('lambda_27C7')
    def lambda_27C7():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_27C7')

    DispatchAsync2(0x000F, 0x0001, lambda_27C7)

    @scena.Lambda('lambda_27D8')
    def lambda_27D8():
        ChrTurnDirection(0x00FE, 0x0013, 0)
        Yield()

        Jump('lambda_27D8')

    DispatchAsync2(0x0010, 0x0001, lambda_27D8)

    ClearChrFlags(0x0013, 0x0080)
    ChrSetRGBAMask(0x0013, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_27F9')
    def lambda_27F9():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_27F9)

    @scena.Lambda('lambda_280B')
    def lambda_280B():
        ChrWalkTo(0x00FE, 30, 0, 55280, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_280B)

    Sleep(100)

    CameraMove(550, 0, 58110, 2000)

    ChrTalk(
        0x0013,
        (
            '#030F哎呀呀。\n',
            '主角华丽登场了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x0101, 65535)

    @scena.Lambda('lambda_2865')
    def lambda_2865():
        ChrWalkTo(0x00FE, -1160, 0, 57640, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2865)

    Sleep(100)

    SetChrChipByIndex(0x0102, 65535)

    @scena.Lambda('lambda_288A')
    def lambda_288A():
        ChrWalkTo(0x00FE, 240, 0, 58050, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_288A)

    Sleep(300)

    @scena.Lambda('lambda_28AA')
    def lambda_28AA():
        ChrWalkTo(0x00FE, 120, 0, 59660, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0002, lambda_28AA)

    Sleep(500)

    SetChrChipByIndex(0x0108, 65535)

    @scena.Lambda('lambda_28CF')
    def lambda_28CF():
        ChrWalkTo(0x00FE, -1840, 0, 58450, 4000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_28CF)

    Sleep(100)

    @scena.Lambda('lambda_28EF')
    def lambda_28EF():
        ChrWalkTo(0x00FE, 2470, 0, 59650, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0002, lambda_28EF)

    Sleep(100)

    Sleep(2000)

    TerminateThread(0x0012, 0xFF)

    ChrTalk(
        0x0108,
        (
            '#070F哈哈，这不是那位\n',
            '怪腔怪调的兄弟吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对了，雪拉扎德，\n',
            '真是好久不见了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0012, 0x0108, 400)

    ChrTalk(
        0x0012,
        (
            '#020F你好，久疏问候了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '没想到金兄你也\n',
            '到利贝尔来了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030130817V听说你和艾丝蒂尔\n',
            '他们在一起时，\n',
            '我就没有那么担心了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F哈哈，你真是太过\n',
            '高估我了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过我说你啊……\n',
            '变得相当漂亮了呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130820V说实话，我都有些认不出来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#020F哎、哎呀，真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0013, 0x0012, 400)
    Sleep(500)

    ChrTurnDirection(0x0013, 0x0108, 400)
    Sleep(500)

    ChrTurnDirection(0x0013, 0x0012, 400)

    ChrTalk(
        0x0013,
        (
            '#030F哼·哼·哼，\n',
            '我好生嫉妒。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在把我\n',
            '尽情的享用了之后，\n',
            '又像垃圾一样抛弃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0012, 0x0013, 400)

    ChrTalk(
        0x0012,
        (
            '#020F哎呀，奥利维尔，\n',
            '你不是与爱娜小姐相逢了吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030130825V还想脚踏两只船啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0013, 0x0102, 400)

    ChrTalk(
        0x0013,
        (
            '#030F对不起呢。\n',
            '都是我的错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F还真是的……\n',
            '大家都还是老样子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F可是雪拉姐姐，\n',
            '竟然来到王都了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130829V王国军不是把\n',
            '关所全部封锁了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0012, 0x0102, 400)

    ChrTalk(
        0x0012,
        (
            '#020F嗯，所以我们是用小船\n',
            '从瓦雷利亚湖过来的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030130831V在王都的码头上的岸。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130832V#010F原来如此，深思熟虑呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F可是，为何会又和\n',
            '这个骗吃骗喝的演奏家在一起呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#020F我刚踏出\n',
            '王都的协会就撞见他了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030130835V他死皮赖脸的跟着我，甩都甩不掉，\n',
            '没办法，我就只有带他来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#030F哈·哈·哈。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040130837V如此有趣的事情\n',
            '怎么能缺少了我的参与呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对了，那位小姐是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0101, 0xFF)
    ChrWalkTo(0x0102, 940, 0, 58220, 2000, 0x00)
    ChrTurnDirection(0x0102, 0x0010, 400)
    ChrTurnDirection(0x0101, 0x0010, 400)

    ChrTalk(
        0x0101,
        (
            '#000F啊，我给你介绍一下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130840V女王陛下的孙女－\n',
            '科洛蒂娅公主殿下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130841V是我和约修亚的朋友。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2E07')
    def lambda_2E07():
        ChrTurnDirection(0x00FE, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2E07)

    @scena.Lambda('lambda_2E15')
    def lambda_2E15():
        ChrTurnDirection(0x00FE, 0x0013, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2E15)

    TerminateThread(0x0010, 0xFF)

    ChrTalk(
        0x0010,
        (
            '两位，初次见面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0060130843V你们能来协助我\n',
            '真是太感谢了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#020F不用在意，\n',
            '这也是游击士的义务嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#030F呵，拯救美丽的公主\n',
            '是绅士的无上荣誉呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '能见到您是我的光荣，公主殿下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrPos(0x0011, -110, 0, 50960, 0)
    SetChrPos(0x000E, -110, 0, 50960, 0)
    ChrSetRGBAMask(0x0011, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x000E, 255, 255, 255, 0, 0)

    ChrTalk(
        0x0011,
        (
            '#0101060022V科洛丝，你没事吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2F3C')
    def lambda_2F3C():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2F3C)

    @scena.Lambda('lambda_2F4A')
    def lambda_2F4A():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2F4A)

    @scena.Lambda('lambda_2F58')
    def lambda_2F58():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_2F58)

    @scena.Lambda('lambda_2F66')
    def lambda_2F66():
        ChrTurnDirection(0x00FE, 0x0011, 400)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_2F66)

    @scena.Lambda('lambda_2F74')
    def lambda_2F74():
        ChrMoveTo(0x00FE, 1190, 0, 55790, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_2F74)

    @scena.Lambda('lambda_2F8F')
    def lambda_2F8F():
        ChrMoveTo(0x00FE, -1720, 0, 57080, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2F8F)

    Sleep(500)

    @scena.Lambda('lambda_2FAF')
    def lambda_2FAF():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_2FAF')

    DispatchAsync2(0x0101, 0x0001, lambda_2FAF)

    @scena.Lambda('lambda_2FC0')
    def lambda_2FC0():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_2FC0')

    DispatchAsync2(0x0102, 0x0001, lambda_2FC0)

    @scena.Lambda('lambda_2FD1')
    def lambda_2FD1():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_2FD1')

    DispatchAsync2(0x0108, 0x0001, lambda_2FD1)

    @scena.Lambda('lambda_2FE2')
    def lambda_2FE2():
        ChrTurnDirection(0x00FE, 0x0011, 0)
        Yield()

        Jump('lambda_2FE2')

    DispatchAsync2(0x0013, 0x0001, lambda_2FE2)

    ClearChrFlags(0x0011, 0x0080)

    @scena.Lambda('lambda_2FF8')
    def lambda_2FF8():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2FF8)

    @scena.Lambda('lambda_300A')
    def lambda_300A():
        ChrWalkTo(0x00FE, -350, 0, 57210, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_300A)

    Sleep(1000)

    ClearChrFlags(0x000E, 0x0080)
    SetChrFlags(0x000E, 0x0040)
    SetChrFlags(0x000E, 0x0004)

    @scena.Lambda('lambda_3039')
    def lambda_3039():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x000E, 0x0002, lambda_3039)

    @scena.Lambda('lambda_304B')
    def lambda_304B():
        ChrWalkTo(0x00FE, -850, 1000, 57190, 5000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_304B)

    Sleep(1000)

    ChrTalk(
        0x0010,
        (
            '尤莉亚中尉，基库！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '啾！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '啾啾！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '啾——啾！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '呵呵，太好了。\n',
            '又和你见面了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#170F殿下，您平安无事就好……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130854V真的……真的太好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '尤莉亚中尉你也是……\n',
            '精神焕发呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '之后，大家和伪装行动的\n',
            '游击士们还有亲卫队队员汇合了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '安顿好其他的人质之后，\n',
            '艾丝蒂尔她们决定去确认当前的状况。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    OP_28(0x004B, 0x04, 0x10)
    OP_28(0x004C, 0x01, 0x0040)
    OP_28(0x004C, 0x01, 0x0080)
    OP_28(0x004C, 0x01, 0x0100)
    OP_28(0x004D, 0x04, 0x02)
    OP_28(0x004D, 0x04, 0x04)
    OP_28(0x004D, 0x01, 0x0001)
    OP_28(0x004D, 0x01, 0x0002)
    OP_1B(0x00, 0x00, 0xFFFF)
    SetScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    NewScene('ED6_DT01/T4300._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0x31FC
@scena.Code('func_06_31FC')
def func_06_31FC():
    EventBegin(0x00)
    CameraMove(920, 250, 64110, 0)
    OP_67(0, 5940, -10000, 0)
    CameraSetDistance(1560, 0)
    OP_6C(45000, 0)
    OP_6E(588, 0)
    ClearChrFlags(0x0011, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x001B, 0x0080)
    ClearChrFlags(0x001C, 0x0080)
    ClearChrFlags(0x001D, 0x0080)
    SetChrPos(0x0011, -140, 250, 68110, 180)
    SetChrPos(0x0102, -2000, 0, 66540, 90)
    SetChrPos(0x0013, -3440, 0, 65990, 90)
    SetChrPos(0x0108, -3210, 0, 67070, 90)
    SetChrPos(0x0101, 2020, 0, 66210, 270)
    SetChrPos(0x0010, 2630, 0, 67290, 270)
    SetChrPos(0x0012, 2980, 0, 66110, 270)
    SetChrPos(0x0017, -50, 0, 65269, 0)
    SetChrPos(0x0016, 930, 0, 64510, 0)
    SetChrPos(0x0014, -1040, 0, 64410, 0)
    SetChrPos(0x0015, -50, 0, 63940, 0)
    SetChrPos(0x0018, -940, 0, 61330, 0)
    SetChrPos(0x0019, 50, 0, 61320, 0)
    SetChrPos(0x001A, 1030, 0, 61320, 0)
    SetChrPos(0x001B, -940, 0, 60000, 0)
    SetChrPos(0x001C, 50, 0, 60000, 0)
    SetChrPos(0x001D, 1030, 0, 60000, 0)
    SetChrChipByIndex(0x0010, 24)
    CameraMove(920, 250, 67890, 2000)

    ChrTalk(
        0x0011,
        (
            '#0100130943V#170F#5P现在我就对解放格兰赛尔城\n',
            '和营救女王陛下的作战进行说明。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0011, 0x0102, 400)
    Sleep(400)

    ChrTalk(
        0x0011,
        (
            '#0100130944V#170F#5P首先，由约修亚等三人为一组\n',
            '从地下水路攻入格兰赛尔城的地下。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130945V然后迅速赶往亲卫队值勤室，\n',
            '启动城门的开关装置。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130946V#010F明白了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130947V#070F嗯，巨大的烟花就要开始燃放了啊。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0013,
        (
            '#0040130948V#035F哼哼……不管怎样，\n',
            '舞台剧最后一幕终于开演了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0011, 180, 400)
    Sleep(400)

    ChrTalk(
        0x0011,
        (
            '#0100130949V#170F#5P在城门打开的同时，\n',
            '全体亲卫队成员以及四名游击士\n',
            '就从市街区直接冲进城内。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130950V尽量制造草木皆兵的效果，\n',
            '将敌人全部引入城内集中。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0017,
        (
            '#0330130951V好的，交给我们去办吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#0310130952V太好了，我已经跃跃欲试了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0100130953V#176F#5P最后还要说的是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0011, 0x0010, 400)
    Sleep(400)

    ChrTalk(
        0x0011,
        (
            '#0100130954V#175F#5P……公主殿下，\n',
            '您真的下定决心要参战吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0010,
        (
            '#0060130955V#049F#2P对不起……\n',
            '我一定要救出祖母大人。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130956V#040F而且，我还会操纵飞艇……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060130957V所以请让我也尽一份力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0100130958V#175F#5P唉……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130959V如果早知道会发生这样的事情，\n',
            '当初就不教你操纵飞艇的方法了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130960V#006F#2P不用担心啦，尤莉亚中尉。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130961V科洛丝就交给我们来照顾吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0012,
        (
            '#0030130962V#020F#2P我以『银闪』之名作担保，\n',
            '发誓一定会保护公主的安全。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0011,
        (
            '#0100130963V#176F#5P我知道了……拜托你们了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130964V#170F在将敌人的兵力集中于城内之后，\n',
            '艾丝蒂尔等三人为一组就乘坐\n',
            '特务飞艇在空中庭园强行着陆。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130965V然后就冲入女王宫，\n',
            '救出艾莉茜雅女王陛下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130966V#006F#2P明白了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0011, 180, 400)
    Sleep(400)

    ChrTalk(
        0x0011,
        (
            '#0100130967V#176F#5P正午钟响的同时开始作战，\n',
            '在此之前请在各自的地点等候。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0100130968V#177F全体听命，行动开始！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(400)

    SetMessageWindowPos(300, 200, -1, -1)
    SetChrName('全员')

    Talk(
        (
            '#2690130969V',
            (TxtCtl.SetColor, 0x0),
            '#5SYes，Madam！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()
    OP_56(0x00)
    FadeOut(1500, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 5, 0x3FD))
    NewScene('ED6_DT01/T4302._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x39B4
@scena.Code('func_07_39B4')
def func_07_39B4():
    EventBegin(0x01)

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A17',
    )

    ChrTalk(
        0x0101,
        (
            '#0010130699V#002F还没有完成女王陛下的委托呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130700V快点把公主殿下找出来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3AE2')

    def _loc_3A17(): pass

    label('loc_3A17')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3A81',
    )

    ChrTalk(
        0x0102,
        (
            '#0020130701V#012F等把人质都解放了，\n',
            '再离开这里吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130702V总之要先把里面彻底调查一番。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_3AE2')

    def _loc_3A81(): pass

    label('loc_3A81')

    ChrTalk(
        0x0108,
        (
            '#0080130703V#072F还没有找到公主殿下和其他人质呢。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130704V先把那些坏家伙们\n',
            '一个不留地干掉吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_3AE2(): pass

    label('loc_3AE2')

    ChrMoveToRelative(0x0000, 0, 0, 1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
