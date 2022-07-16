import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import C3107_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('C3107   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '凯诺娜上尉'),
    TXT(0x02, '洛伦斯少尉'),
    TXT(0x03, '理查德上校'),
    TXT(0x04, '黑衣男子'),
    TXT(0x05, '黑衣男子'),
    TXT(0x06, '黑衣男子'),
    TXT(0x07, '黑衣男子'),
    TXT(0x08, '黑衣男子'),
    TXT(0x09, '黑衣男子'),
    TXT(0x0A, '特务艇'),
    TXT(0x0B, '特务艇灯光'),
    TXT(0x0C, '特务艇影子'),
    TXT(0x0D, '士兵'),
    TXT(0x0E, '士兵'),
    TXT(0x0F, '士兵'),
    TXT(0x10, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'C3107.x'
    header.mapIndex       = 1
    header.bgm            = 34
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x26E6
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
        ('ED6_DT07/CH01610._CH', 'ED6_DT07/CH01610P._CP'),
        ('ED6_DT07/CH02100._CH', 'ED6_DT07/CH02100P._CP'),
        ('ED6_DT07/CH02200._CH', 'ED6_DT07/CH02200P._CP'),
        ('ED6_DT07/CH02030._CH', 'ED6_DT07/CH02030P._CP'),
        ('ED6_DT07/CH00100._CH', 'ED6_DT07/CH00100P._CP'),
        ('ED6_DT07/CH00101._CH', 'ED6_DT07/CH00101P._CP'),
        ('ED6_DT07/CH00110._CH', 'ED6_DT07/CH00110P._CP'),
        ('ED6_DT07/CH00111._CH', 'ED6_DT07/CH00111P._CP'),
        ('ED6_DT07/CH00150._CH', 'ED6_DT07/CH00150P._CP'),
        ('ED6_DT07/CH00151._CH', 'ED6_DT07/CH00151P._CP'),
        ('ED6_DT07/CH00160._CH', 'ED6_DT07/CH00160P._CP'),
        ('ED6_DT07/CH00161._CH', 'ED6_DT07/CH00161P._CP'),
        ('ED6_DT06/CH20042._CH', 'ED6_DT06/CH20042P._CP'),
        ('ED6_DT07/CH00442._CH', 'ED6_DT07/CH00442P._CP'),
        ('ED6_DT07/CH01650._CH', 'ED6_DT07/CH01650P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
        ('ED6_DT07/CH01790._CH', 'ED6_DT07/CH01790P._CP'),
        ('ED6_DT07/CH00502._CH', 'ED6_DT07/CH00502P._CP'),
    ]

# id: 0x10002 offset: 0x13A
@scena.NpcData('NpcData')
def NpcData():
    return (
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
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 8500,
            z                   = 0,
            y                   = 33940,
            direction           = 90,
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
            x                   = 12530,
            z                   = 0,
            y                   = 33790,
            direction           = 270,
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
            x                   = 21330,
            z                   = 0,
            y                   = 25970,
            direction           = 0,
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
            x                   = 18240,
            z                   = 0,
            y                   = 25980,
            direction           = 0,
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
            x                   = 22510,
            z                   = 0,
            y                   = 25840,
            direction           = 0,
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
            x                   = 17040,
            z                   = 0,
            y                   = 25840,
            direction           = 0,
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
            x                   = 17040,
            z                   = 0,
            y                   = 25840,
            direction           = 0,
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
            x                   = 17040,
            z                   = 0,
            y                   = 25840,
            direction           = 0,
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
            x                   = 17040,
            z                   = 200,
            y                   = 25840,
            direction           = 0,
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
            direction           = 90,
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
            direction           = 90,
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
            direction           = 90,
            word_0E             = 0,
            dword_10            = 14,
            chipIndex           = 14,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
    )

# id: 0x10003 offset: 0x31A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x31A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 10390,
            y           = -1000,
            z           = 34100,
            range       = 11000,
            dword_10    = 0x00002AF8,
            dword_14    = 0x00000000,
            dword_18    = 0x00000040,
            dword_1C    = 0x00000004,
        ),
    )

# id: 0x10005 offset: 0x33A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 300,
            triggerZ            = 0,
            triggerY            = 45490,
            triggerRange        = 800,
            actorX              = 300,
            actorZ              = 1300,
            actorY              = 45490,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x35E
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_36C',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0006)

    def _loc_36C(): pass

    label('loc_36C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_37A',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x000D)

    def _loc_37A(): pass

    label('loc_37A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_388',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, 0x000C)

    def _loc_388(): pass

    label('loc_388')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 7, 0x567)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_390',
    )

    def _loc_390(): pass

    label('loc_390')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 5, 0x54D)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 6, 0x54E)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_3DD',
    )

    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    SetChrPos(0x0014, 11810, 0, 31000, 0)
    SetChrPos(0x0015, 8930, 0, 32619, 270)
    SetChrPos(0x0016, 10250, 500, 34340, 180)

    def _loc_3DD(): pass

    label('loc_3DD')

    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 0, 0x568)),
            Expr.Return,
        ),
        'loc_42E',
    )

    SetChrChipByIndex(0x000B, 12)
    SetChrChipByIndex(0x000C, 12)
    SetChrFlags(0x000B, 0x0800)
    SetChrFlags(0x000C, 0x0800)
    ClearChrFlags(0x000B, 0x0001)
    ClearChrFlags(0x000C, 0x0001)
    SetChrPos(0x000B, 7830, 0, 33420, 199)
    SetChrPos(0x000C, 11920, 0, 31940, 272)

    def _loc_42E(): pass

    label('loc_42E')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_43A'),
        (-1, 'loc_44D'),
    )

    def _loc_43A(): pass

    label('loc_43A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 5, 0x565)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 4, 0x564)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_44A',
    )

    Event(0, 0x0003)

    def _loc_44A(): pass

    label('loc_44A')

    Jump('loc_44D')

    def _loc_44D(): pass

    label('loc_44D')

    Return()

# id: 0x0001 offset: 0x44E
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 5, 0x54D)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 6, 0x54E)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_465',
    )

    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 9)

    def _loc_465(): pass

    label('loc_465')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 7, 0x567)),
            Expr.Return,
        ),
        'loc_470',
    )

    OP_64(0x00, 0x0001)

    def _loc_470(): pass

    label('loc_470')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 2, 0x56A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 1, 0x569)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_481',
    )

    OP_1B(0x00, 0x00, 0x000B)

    def _loc_481(): pass

    label('loc_481')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 0, 0x568)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 4, 0x564)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_505',
    )

    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 7, 0x567)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_505',
    )

    OP_6F(0x000B, 1200)
    OP_72(0x000B, 0x0004)
    OP_72(0x000C, 0x0004)
    SetChrPos(0x0011, 19820, 0, 15980, 180)
    SetChrPos(0x0012, 19820, 0, 15980, 180)
    SetChrFlags(0x0013, 0x0004)
    SetChrPos(0x0013, 19820, 400, 15980, 180)
    OP_A1(0x0011, 0x000B)
    OP_A1(0x0013, 0x000C)
    OP_A1(0x0012, 0x000D)
    OP_6F(0x000B, 560)
    OP_6F(0x000D, 560)

    def _loc_505(): pass

    label('loc_505')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 3, 0x56B)),
            Expr.Return,
        ),
        'loc_511',
    )

    PlaySE(172, 0x01, 0x64)

    def _loc_511(): pass

    label('loc_511')

    Return()

# id: 0x0002 offset: 0x512
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_527',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_527(): pass

    label('loc_527')

    Return()

# id: 0x0003 offset: 0x528
@scena.Code('func_03_528')
def func_03_528():
    EventBegin(0x00)
    CameraMove(20, 0, 6550, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, 2130, 0, 2640, 0)
    SetChrPos(0x0102, 870, 0, 2190, 0)
    SetChrPos(0x0106, 1560, 0, 3520, 0)
    SetChrPos(0x0107, 1680, 0, 1380, 0)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010090967V#004F啊……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090968V#012F他们是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_66(0x0000)

    @scena.Lambda('lambda_05F4')
    def lambda_05F4():
        CameraMove(23090, 0, 16160, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_05F4)

    Sleep(5000)

    SetChrPos(0x0101, -12410, 0, 6160, 45)
    SetChrPos(0x0106, -12420, 0, 5400, 45)
    SetChrPos(0x0102, -12450, 0, 7280, 45)
    SetChrPos(0x0107, -13200, 0, 6480, 45)
    CameraMove(10200, 0, 35370, 3000)
    Sleep(1000)

    CameraMove(-12420, 0, 7490, 3000)

    ChrTalk(
        0x0106,
        (
            '#0050090969V#051F哼……\n',
            '还真是阴魂不散的家伙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090970V#065F还有那艘飞艇也是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090971V#002F那帮家伙果然和军队有关……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010090972V不过他们好像和普通的士兵不同……\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090973V#012F那些黑衣人大概是被训练成\n',
            '专门从事破坏工作的特殊部队吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090974V难怪他们的实力那么强悍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070090975V#065F爷、爷爷被抓到那里去了吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090976V#057F嗯，可能性越来越高了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050090977V不过……\n',
            '要是在这里和他们产生冲突就糟了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090978V#012F是啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090979V不小心引起骚动的话，\n',
            '恐怕要塞里的士兵都会被引来的。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010090980V#002F趁现在还没被发现，\n',
            '我们快想办法潜进那房子里去吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00AC, 5, 0x565))
    OP_28(0x0044, 0x01, 0x0004)
    Sleep(100)

    Fade(1000)
    OP_66(0x0001)
    CameraMove(-13020, 0, 7160, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -13020, 0, 7160, 0)
    SetChrPos(0x0102, -13020, 0, 7160, 0)
    SetChrPos(0x0106, -13020, 0, 7160, 0)
    SetChrPos(0x0107, -13020, 0, 7160, 0)
    OP_0D()
    EventEnd(0x00)

    Return()

# id: 0x0004 offset: 0x953
@scena.Code('func_04_953')
def func_04_953():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 5, 0x54D)),
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 6, 0x54E)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_BC3',
    )

    EventBegin(0x00)
    CameraMove(10780, 0, 34400, 1500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 7, 0x54F)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A58',
    )

    SetScenaFlags(ScenaFlag(0x00A9, 7, 0x54F))

    ChrTalk(
        0x0014,
        (
            '#4190091085V喂喂……他们被打晕了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0015,
        (
            '#2490091086V能把这些人打晕，\n',
            '真是不简单的家伙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0016,
        (
            '#2440091087V建筑物里面是空的！\n',
            '赶快在营地里面搜索！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091088V#004F（哇哇……被发现了！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091089V#012F（我们暂且先回去！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B4D')

    def _loc_A58(): pass

    label('loc_A58')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_A98',
    )

    ChrTalk(
        0x0101,
        (
            '#0010091090V#002F（糟了！\n',
            '　只能暂且先回去了！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B4D')

    def _loc_A98(): pass

    label('loc_A98')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_AD8',
    )

    ChrTalk(
        0x0102,
        (
            '#0020091091V#012F（不好……\n',
            '　暂时先撤退吧……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B4D')

    def _loc_AD8(): pass

    label('loc_AD8')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B14',
    )

    ChrTalk(
        0x0106,
        (
            '#0050091092V#057F（嘁……\n',
            '　得重来一遍吗！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B4D')

    def _loc_B14(): pass

    label('loc_B14')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_B4D',
    )

    ChrTalk(
        0x0107,
        (
            '#0070091093V#065F（哇哇……\n',
            '　被发现了～！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B4D(): pass

    label('loc_B4D')

    Sleep(100)

    Fade(1000)
    SetChrPos(0x0101, -12410, 0, 6160, 45)
    SetChrPos(0x0106, -12420, 0, 5400, 45)
    SetChrPos(0x0102, -12450, 0, 7280, 45)
    SetChrPos(0x0107, -13200, 0, 7280, 45)
    SetChrPos(0x010B, -13200, 0, 6480, 45)
    CameraMove(-12420, 0, 7490, 0)
    OP_0D()
    EventEnd(0x00)

    Jump('loc_1325')

    def _loc_BC3(): pass

    label('loc_BC3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 4, 0x564)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AD, 0, 0x568)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1325',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 7, 0x567)),
            Expr.Return,
        ),
        'loc_1135',
    )

    EventBegin(0x00)
    ChrTurnDirection(0x000B, 0x000C, 0)
    ChrTurnDirection(0x000C, 0x000B, 0)
    CameraMove(10780, 0, 34400, 1500)
    SetChrChipByIndex(0x0101, 4)
    SetChrChipByIndex(0x0102, 6)
    SetChrChipByIndex(0x0106, 8)
    SetChrChipByIndex(0x0107, 10)
    SetChrPos(0x0106, 7580, 0, 27490, 0)
    SetChrPos(0x0101, 8140, 0, 26150, 0)
    SetChrPos(0x0102, 6300, 0, 26560, 0)
    SetChrPos(0x0107, 7180, 0, 25690, 0)

    ChrTalk(
        0x000B,
        (
            '#2620091069V唉……\n',
            '难得王都有那么大的作战行动。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '#2620091070V我们竟被派在这里\n',
            '看守一个老头。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2630091071V别抱怨、别抱怨。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2630091072V为了王国，为了理想，\n',
            '为了协助上校成就一番伟业……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '#2630091073V看守老头也是我们情报部隐秘部队——\n',
            '『特务兵』的使命啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091074V哼！\n',
            '你们的口号喊得还真响！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrFlags(0x000B, 0x0020)
    SetChrFlags(0x000C, 0x0020)

    @scena.Lambda('lambda_0D82')
    def lambda_0D82():
        ChrTurnDirection(0x00FE, 0x0106, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_0D82)

    ChrTurnDirection(0x000B, 0x0106, 400)

    NpcTalk(
        0x000B,
        '特务兵',
        (
            '#2620091075V什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0DB5')
    def lambda_0DB5():
        CameraMove(9740, 0, 30350, 1500)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0DB5)

    OP_6C(52000, 1500)

    NpcTalk(
        0x000B,
        '特务兵',
        (
            '#2620091076V不、不可能……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x000C,
        '特务兵',
        (
            '#2630091077V#4P阿加特·科洛斯纳！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    OP_62(0x000C, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)
    SetChrChipByIndex(0x000B, 13)
    SetChrSubChip(0x000B, 0)
    Sleep(100)

    SetChrChipByIndex(0x000C, 13)
    SetChrSubChip(0x000C, 0)

    ChrTalk(
        0x0106,
        (
            '#0050091078V#054F太晚了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0E7C')
    def lambda_0E7C():
        ChrWalkTo(0x00FE, 10650, 0, 33910, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_0E7C)

    Sleep(50)

    @scena.Lambda('lambda_0E9C')
    def lambda_0E9C():
        OP_92(0x00FE, 0x000C, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0E9C)

    Sleep(50)

    @scena.Lambda('lambda_0EB6')
    def lambda_0EB6():
        OP_92(0x00FE, 0x000B, 1000, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_0EB6)

    Sleep(100)

    @scena.Lambda('lambda_0ED0')
    def lambda_0ED0():
        ChrWalkTo(0x00FE, 10650, 0, 33910, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_0ED0)

    Sleep(300)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0107, 0xFF)
    TerminateThread(0x0106, 0xFF)
    Battle(0x00000252, 0x00000000, 0x00, 0x0000, 0xFF)

    Switch(
        (
            (Expr.PushValueByIndex, 0x3),
            Expr.Return,
        ),
        (0x00000001, 'loc_F13'),
        (-1, 'loc_F16'),
    )

    def _loc_F13(): pass

    label('loc_F13')

    OP_B4(0x00)

    Return()

    def _loc_F16(): pass

    label('loc_F16')

    EventBegin(0x00)
    SetChrChipByIndex(0x0101, 65535)
    SetChrChipByIndex(0x0102, 65535)
    SetChrChipByIndex(0x0106, 65535)
    SetChrChipByIndex(0x0107, 65535)
    SetChrChipByIndex(0x000B, 12)
    SetChrChipByIndex(0x000C, 12)
    SetChrSubChip(0x000B, 0)
    SetChrSubChip(0x000C, 0)
    CameraMove(8250, 0, 31140, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(44000, 0)
    OP_6E(262, 0)
    SetChrPos(0x000B, 7830, 0, 33420, 199)
    SetChrPos(0x000C, 11920, 0, 31940, 272)
    SetChrChipByIndex(0x000B, 12)
    SetChrChipByIndex(0x000C, 12)
    ClearChrFlags(0x000B, 0x0001)
    ClearChrFlags(0x000C, 0x0001)
    SetChrFlags(0x000B, 0x0800)
    SetChrFlags(0x000C, 0x0800)
    SetChrPos(0x0106, 8240, 0, 31790, 45)
    SetChrPos(0x0101, 8960, 0, 30390, 45)
    SetChrPos(0x0102, 6540, 0, 31580, 45)
    SetChrPos(0x0107, 7210, 0, 30100, 45)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0106,
        (
            '#0050091079V#051F嘁……\n',
            '两个活该的家伙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091080V以前欠下这些家伙的旧帐，\n',
            '这下总算连本带利还清了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0106, 400)

    ChrTalk(
        0x0101,
        (
            '#0010091081V#506F又在公报私仇了～\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_10A0')
    def lambda_10A0():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_10A0)

    @scena.Lambda('lambda_10AE')
    def lambda_10AE():
        ChrTurnDirection(0x00FE, 0x0101, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_10AE)

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020091082V#012F现在开始就要抓紧时间了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091083V闲话少说，\n',
            '尽快带博士一起逃走吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070091084V#560F是！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00AD, 0, 0x568))
    OP_28(0x0044, 0x01, 0x0020)
    EventEnd(0x00)

    Jump('loc_1325')

    def _loc_1135(): pass

    label('loc_1135')

    EventBegin(0x00)
    CameraMove(10780, 0, 34400, 1500)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 6, 0x566)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_11CE',
    )

    SetScenaFlags(ScenaFlag(0x00AC, 6, 0x566))

    ChrTalk(
        0x000B,
        (
            '#2620091094V唔……？\n',
            '好像有什么动静……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091095V#004F（哇哇……被发现了！？）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091096V#012F（我们暂且先回去！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12C3')

    def _loc_11CE(): pass

    label('loc_11CE')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_120E',
    )

    ChrTalk(
        0x0101,
        (
            '#0010091097V#002F（糟了！\n',
            '　只能暂且先回去了！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12C3')

    def _loc_120E(): pass

    label('loc_120E')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_124E',
    )

    ChrTalk(
        0x0102,
        (
            '#0020091098V#012F（不好……\n',
            '　暂时先撤退吧……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12C3')

    def _loc_124E(): pass

    label('loc_124E')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_128A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050091099V#057F（嘁……\n',
            '　得重来一遍吗！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_12C3')

    def _loc_128A(): pass

    label('loc_128A')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12C3',
    )

    ChrTalk(
        0x0107,
        (
            '#0070091100V#065F（哇哇……\n',
            '　被发现了～！）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_12C3(): pass

    label('loc_12C3')

    Sleep(100)

    Fade(1000)
    SetChrPos(0x0101, -12410, 0, 6160, 45)
    SetChrPos(0x0106, -12420, 0, 5400, 45)
    SetChrPos(0x0102, -12450, 0, 7280, 45)
    SetChrPos(0x0107, -13200, 0, 6480, 45)
    CameraMove(-12420, 0, 7490, 0)
    OP_0D()
    EventEnd(0x00)

    def _loc_1325(): pass

    label('loc_1325')

    Return()

# id: 0x0005 offset: 0x1326
@scena.Code('func_05_1326')
def func_05_1326():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 4, 0x564)),
            (Expr.TestScenaFlags, ScenaFlag(0x00AC, 7, 0x567)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1509',
    )

    SetScenaFlags(ScenaFlag(0x00AC, 7, 0x567))
    OP_28(0x0044, 0x01, 0x0008)
    EventBegin(0x00)
    Fade(1000)
    CameraMove(-490, 0, 45500, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(63000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0101, -490, 0, 45980, 90)
    SetChrPos(0x0102, -1420, 0, 46110, 90)
    SetChrPos(0x0107, -490, 0, 45040, 90)
    SetChrPos(0x0106, -1380, 0, 45220, 90)
    OP_0D()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010090981V#006F我说，\n',
            '从这里潜进去不就行了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020090982V#013F不行……\n',
            '窗户上有铁栏杆挡着。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020090983V要做到一声不响地钻进去，\n',
            '恐怕不是件容易的事……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0107, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0107,
        (
            '#0070090984V#065F……………啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050090985V#057F这可真是中头彩了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0101, 90, 400)

    ChrTalk(
        0x0101,
        (
            '#0010090986V#004F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/C3115._SN', 100, 0, 0)
    IdleLoop()

    def _loc_1509(): pass

    label('loc_1509')

    Return()

# id: 0x0006 offset: 0x150A
@scena.Code('func_06_150A')
def func_06_150A():
    EventBegin(0x00)
    OP_6F(0x000B, 1200)
    OP_72(0x000B, 0x0004)
    OP_72(0x000C, 0x0004)
    SetChrPos(0x0011, 19820, 0, 15980, 180)
    SetChrPos(0x0012, 19820, 0, 15980, 180)
    SetChrFlags(0x0013, 0x0004)
    SetChrPos(0x0013, 19820, 400, 15980, 180)
    OP_A1(0x0011, 0x000B)
    OP_A1(0x0013, 0x000C)
    OP_A1(0x0012, 0x000D)
    OP_6F(0x000B, 560)
    OP_6F(0x000D, 560)
    CameraMove(-1910, 0, 45400, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0107, -1470, 0, 45910, 0)
    SetChrPos(0x0106, -1230, 0, 44430, 0)
    SetChrPos(0x0101, -2870, 0, 44560, 0)
    SetChrPos(0x0102, -3200, 0, 46380, 0)
    ChrTurnDirection(0x0101, 0x0107, 0)
    ChrTurnDirection(0x0107, 0x0101, 0)
    ChrTurnDirection(0x0102, 0x0101, 0)
    ChrTurnDirection(0x0106, 0x0101, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010091047V#002F理查德上校……\n',
            '那个人竟然就是幕后主谋啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091048V而且他好像也在找父亲呢……\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091049V#013F啊啊……\n',
            '这到底是怎么回事呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091050V而且那个带面具的男人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091051V#057F那个混帐……\n',
            '竟然在这种地方出现了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0106, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    SetChrDirection(0x0106, 135, 400)

    ChrTalk(
        0x0106,
        (
            '#0050091052V#052F啊，少校好像要走了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(21250, 0, 16520, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(4170, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    PlaySE(117, 0x01, 0x64)
    OP_6F(0x000B, 1200)
    OP_6F(0x000D, 1200)
    SetChrPos(0x0008, 20330, 0, 28410, 180)
    SetChrPos(0x0009, 19810, 0, 30280, 180)
    SetChrPos(0x000A, 19810, 0, 27620, 180)
    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    CreateThread(0x000A, 0x01, 0x00, 0x0007)
    Sleep(300)

    CreateThread(0x0008, 0x01, 0x00, 0x0007)

    @scena.Lambda('lambda_1809')
    def lambda_1809():
        OP_6C(102000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1809)

    @scena.Lambda('lambda_1819')
    def lambda_1819():
        CameraMove(19600, 3300, 18970, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1819)

    Sleep(1000)

    CreateThread(0x000D, 0x01, 0x00, 0x0008)
    Sleep(500)

    CreateThread(0x000E, 0x01, 0x00, 0x0008)
    Sleep(400)

    CreateThread(0x000F, 0x01, 0x00, 0x0008)
    Sleep(500)

    CreateThread(0x0010, 0x01, 0x00, 0x0008)
    SetChrBattleFlags(0x0009, 0x0020)
    ChrWalkTo(0x0009, 19840, 3300, 18550, 2000, 0x00)
    Sleep(1000)

    ChrTurnDirection(0x0009, 0x0102, 400)
    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0140091053V#280F呵呵……\n',
            '你们能顺利逃走吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetChrDirection(0x0009, 180, 400)
    Sleep(100)

    ChrWalkTo(0x0009, 19840, 3300, 17810, 3000, 0x00)

    @scena.Lambda('lambda_18D8')
    def lambda_18D8():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0003, lambda_18D8)

    ChrWalkTo(0x0009, 19840, 3300, 15440, 3000, 0x00)
    SetChrFlags(0x0009, 0x0080)
    Sleep(1000)

    CreateThread(0x0011, 0x01, 0x00, 0x0009)
    WaitForThreadExit(0x0011, 0x0001)
    Sleep(3000)

    TerminateThread(0x0101, 0xFF)
    Fade(1000)
    CameraMove(-1180, 0, 35690, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0106, -1920, 0, 35410, 135)
    SetChrPos(0x0101, -840, 0, 35470, 135)
    SetChrPos(0x0102, -2220, 0, 36430, 135)
    SetChrPos(0x0107, -1130, 0, 36470, 135)
    OP_0D()

    ChrTalk(
        0x0106,
        (
            '#0050091054V#051F好了……\n',
            '一下子就全走光了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091055V虽然很想和那混蛋做个了断，\n',
            '但眼下还是把老爷子救出要紧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091056V#006F既然不能从窗户钻进去，\n',
            '那么就只有打倒看守的黑衣人了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010091057V速战速决！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070091058V#062F嗯、嗯！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091059V#510F……………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#0010091060V#004F约修亚？\n',
            '你刚才没在听我们说话吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1AED')
    def lambda_1AED():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1AED)

    @scena.Lambda('lambda_1AFB')
    def lambda_1AFB():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0107, 0x0001, lambda_1AFB)

    @scena.Lambda('lambda_1B09')
    def lambda_1B09():
        ChrTurnDirection(0x00FE, 0x0102, 400)

        ExitThread()

    DispatchAsync(0x0106, 0x0001, lambda_1B09)

    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#0020091061V#014F啊……艾丝蒂尔？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0107,
        (
            '#0070091062V#065F没、没事吧？\n',
            '约修亚哥哥。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091063V#052F喂喂，小子，没事吧。\n',
            '这可不像平常那个冷静的你啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091064V#013F抱、抱歉。\n',
            '刚才发了一下呆……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010091065V#002F约修亚……\n',
            '哪里不舒服吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091066V#010F不要紧，没问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020091067V要先打倒门口那里的黑衣人吧？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091068V#050F啊……快点开始吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0044, 0x01, 0x0010)
    TerminateThread(0x0011, 0xFF)
    OP_71(0x000B, 0x0004)
    OP_71(0x000C, 0x0004)
    OP_71(0x000D, 0x0004)
    EventEnd(0x00)

    Return()

# id: 0x0007 offset: 0x1C8E
@scena.Code('func_07_1C8E')
def func_07_1C8E():
    SetChrBattleFlags(0x00FE, 0x0020)
    ChrWalkTo(0x00FE, 19840, 3300, 17810, 3000, 0x00)

    @scena.Lambda('lambda_1CAD')
    def lambda_1CAD():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1CAD)

    ChrWalkTo(0x00FE, 19840, 3300, 15440, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0008 offset: 0x1CD3
@scena.Code('func_08_1CD3')
def func_08_1CD3():
    SetChrBattleFlags(0x00FE, 0x0020)
    ChrWalkTo(0x00FE, 19840, 0, 26180, 3000, 0x00)
    ChrWalkTo(0x00FE, 19840, 3300, 17810, 3000, 0x00)

    @scena.Lambda('lambda_1D06')
    def lambda_1D06():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x00FE, 0x0003, lambda_1D06)

    ChrWalkTo(0x00FE, 19840, 3300, 15440, 3000, 0x00)
    SetChrFlags(0x00FE, 0x0080)

    Return()

# id: 0x0009 offset: 0x1D2C
@scena.Code('func_09_1D2C')
def func_09_1D2C():
    SetChrFlags(0x0011, 0x0004)
    SetChrFlags(0x0013, 0x0004)
    SetChrFlags(0x0012, 0x0004)
    OP_71(0x000B, 0x0002)
    OP_71(0x000C, 0x0002)
    OP_71(0x000D, 0x0002)
    PlaySE(230, 0x00, 0x64)
    OP_6F(0x000B, 1200)
    OP_6F(0x000D, 1200)
    OP_70(0x000B, 1140)
    OP_70(0x000D, 1140)
    OP_73(0x000B)

    @scena.Lambda('lambda_1D74')
    def lambda_1D74():
        OP_6C(0, 15000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1D74)

    @scena.Lambda('lambda_1D84')
    def lambda_1D84():
        CameraMove(19690, 3300, 12830, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1D84)

    PlaySE(118, 0x00, 0x64)
    OP_6F(0x000B, 361)
    OP_6F(0x000D, 361)
    OP_70(0x000B, 560)
    OP_70(0x000D, 560)
    OP_73(0x000B)
    WaitForThreadExit(0x0101, 0x0002)
    OP_72(0x000D, 0x0004)
    Sleep(500)

    LoadEffect(0x01, 'map\\\\mp021_00.eff')
    PlayEffect(0x01, 0x01, 0x0013, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x00FF, 0, 0, 0, 0)
    PlaySE(119, 0x00, 0x64)
    OP_6F(0x000B, 561)
    OP_6F(0x000D, 561)
    OP_70(0x000B, 580)
    OP_70(0x000D, 580)
    OP_73(0x000B)
    OP_6F(0x000B, 581)
    OP_6F(0x000D, 581)
    OP_70(0x000B, 650)
    OP_70(0x000D, 650)

    @scena.Lambda('lambda_1E58')
    def lambda_1E58():
        CameraMove(19690, 8020, 12830, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1E58)

    @scena.Lambda('lambda_1E70')
    def lambda_1E70():
        ChrMoveToRelativeAsync(0x0012, 0, 500, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_1E70)

    ChrMoveToRelativeAsync(0x0011, 0, 500, 0, 1000, 0x00)

    @scena.Lambda('lambda_1E9F')
    def lambda_1E9F():
        ChrMoveToRelativeAsync(0x0012, 0, 1000, 0, 1500, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_1E9F)

    ChrMoveToRelativeAsync(0x0011, 0, 1000, 0, 1500, 0x00)

    @scena.Lambda('lambda_1ECE')
    def lambda_1ECE():
        ChrMoveToRelativeAsync(0x0012, 0, 1000, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_1ECE)

    ChrMoveToRelativeAsync(0x0011, 0, 1000, 0, 2000, 0x00)

    @scena.Lambda('lambda_1EFD')
    def lambda_1EFD():
        ChrMoveToRelativeAsync(0x0012, 0, 1000, 0, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_1EFD)

    ChrMoveToRelativeAsync(0x0011, 0, 1000, 0, 3000, 0x00)

    @scena.Lambda('lambda_1F2C')
    def lambda_1F2C():
        ChrMoveToRelativeAsync(0x0012, 0, 500, 0, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_1F2C)

    ChrMoveToRelativeAsync(0x0011, 0, 500, 0, 2000, 0x00)

    @scena.Lambda('lambda_1F5B')
    def lambda_1F5B():
        ChrMoveToRelativeAsync(0x0012, 0, 500, 0, 1000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0003, lambda_1F5B)

    ChrMoveToRelativeAsync(0x0011, 0, 500, 0, 1000, 0x00)

    @scena.Lambda('lambda_1F8A')
    def lambda_1F8A():
        ChrMoveTo(0x0011, 21360, 20000, -33590, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_1F8A)

    @scena.Lambda('lambda_1FA5')
    def lambda_1FA5():
        ChrMoveTo(0x0012, 21360, 20000, -33590, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_1FA5)

    @scena.Lambda('lambda_1FC0')
    def lambda_1FC0():
        ChrMoveTo(0x0013, 21360, 300, -33590, 6000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_1FC0)

    @scena.Lambda('lambda_1FDB')
    def lambda_1FDB():
        CameraMove(20020, 10000, -13080, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1FDB)

    OP_6F(0x000B, 651)
    OP_6F(0x000D, 651)
    OP_70(0x000B, 680)
    OP_70(0x000D, 680)
    OP_73(0x000B)
    CreateThread(0x0012, 0x00, 0x00, 0x000A)

    @scena.Lambda('lambda_2019')
    def lambda_2019():
        ChrMoveTo(0x0011, 21360, 20000, -33590, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2019)

    @scena.Lambda('lambda_2034')
    def lambda_2034():
        ChrMoveTo(0x0012, 21360, 20000, -33590, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2034)

    @scena.Lambda('lambda_204F')
    def lambda_204F():
        ChrMoveTo(0x0013, 21360, 300, -33590, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_204F)

    OP_71(0x000B, 0x0020)
    OP_71(0x000D, 0x0020)
    OP_6F(0x000B, 680)
    OP_6F(0x000D, 680)
    OP_70(0x000B, 780)
    OP_70(0x000D, 780)
    Sleep(1000)

    @scena.Lambda('lambda_2095')
    def lambda_2095():
        ChrMoveTo(0x0011, 21360, 20000, -63590, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2095)

    @scena.Lambda('lambda_20B0')
    def lambda_20B0():
        ChrMoveTo(0x0012, 21360, 20000, -63590, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_20B0)

    @scena.Lambda('lambda_20CB')
    def lambda_20CB():
        ChrMoveTo(0x0013, 21360, 300, -63590, 15000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_20CB)

    Sleep(500)

    @scena.Lambda('lambda_20EB')
    def lambda_20EB():
        ChrMoveTo(0x0011, 21360, 20000, -63590, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_20EB)

    @scena.Lambda('lambda_2106')
    def lambda_2106():
        ChrMoveTo(0x0012, 21360, 20000, -63590, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_2106)

    @scena.Lambda('lambda_2121')
    def lambda_2121():
        ChrMoveTo(0x0013, 21360, 300, -63590, 18000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_2121)

    Sleep(500)

    @scena.Lambda('lambda_2141')
    def lambda_2141():
        ChrMoveTo(0x0011, 21360, 20000, -63590, 21000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2141)

    @scena.Lambda('lambda_215C')
    def lambda_215C():
        ChrMoveTo(0x0012, 21360, 20000, -63590, 21000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_215C)

    @scena.Lambda('lambda_2177')
    def lambda_2177():
        ChrMoveTo(0x0013, 21360, 300, -63590, 21000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_2177)

    Sleep(500)

    @scena.Lambda('lambda_2197')
    def lambda_2197():
        ChrMoveTo(0x0011, 21360, 20000, -63590, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0002, lambda_2197)

    @scena.Lambda('lambda_21B2')
    def lambda_21B2():
        ChrMoveTo(0x0012, 21360, 20000, -63590, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0002, lambda_21B2)

    @scena.Lambda('lambda_21CD')
    def lambda_21CD():
        ChrMoveTo(0x0013, 21360, 300, -63590, 25000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0002, lambda_21CD)

    Return()

# id: 0x000A offset: 0x21E3
@scena.Code('func_0A_21E3')
def func_0A_21E3():
    OP_24(0x0075, 0x5A)
    OP_24(0x0077, 0x5A)
    Sleep(200)

    OP_24(0x0075, 0x50)
    OP_24(0x0077, 0x50)
    Sleep(200)

    OP_24(0x0075, 0x46)
    OP_24(0x0077, 0x46)
    Sleep(200)

    OP_24(0x0075, 0x3C)
    OP_24(0x0077, 0x3C)
    Sleep(200)

    OP_24(0x0075, 0x32)
    OP_24(0x0077, 0x32)
    Sleep(200)

    OP_24(0x0075, 0x28)
    OP_24(0x0077, 0x28)
    Sleep(200)

    OP_24(0x0075, 0x1E)
    OP_24(0x0077, 0x1E)
    Sleep(200)

    OP_23(0x0075)
    OP_23(0x0077)
    OP_23(0x00CF)

    Return()

# id: 0x000B offset: 0x2248
@scena.Code('func_0B_2248')
def func_0B_2248():
    EventBegin(0x00)
    Fade(1000)
    CameraMove(11490, 0, 31730, 0)
    OP_0D()
    OP_62(0x000C, 0xFFFFFE0C, 1200, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(2000)

    OP_63(0x000C)

    NpcTalk(
        0x000C,
        '特务兵',
        (
            '#2630091152V呜……啊……\n',
            '怎么能让你们逃走……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(2000, 0, -1)
    OP_0D()
    PlaySE(172, 0x01, 0x64)
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    SetScenaFlags(ScenaFlag(0x00AD, 2, 0x56A))
    OP_28(0x0044, 0x01, 0x0080)
    NewScene('ED6_DT01/C3105._SN', 103, 0, 0)
    IdleLoop()

    Return()

# id: 0x000C offset: 0x22D6
@scena.Code('func_0C_22D6')
def func_0C_22D6():
    EventBegin(0x00)
    CameraMove(-12420, 0, 7490, 0)
    SetChrPos(0x0101, -12410, 0, 6160, 45)
    SetChrPos(0x0106, -12420, 0, 5400, 45)
    SetChrPos(0x0102, -12450, 0, 7280, 45)
    SetChrPos(0x0107, -13200, 0, 7280, 45)
    SetChrPos(0x010B, -13200, 0, 6480, 45)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x010B,
        (
            '#0540091153V#102F要绕开飞艇坪到达码头\n',
            '实在是太困难了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0540091154V还是找找其它的逃跑路线吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091155V#012F嗯，\n',
            '我们最好不要再靠近飞艇坪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    SetChrPos(0x0014, 11810, 0, 31000, 0)
    SetChrPos(0x0015, 8930, 0, 32619, 270)
    SetChrPos(0x0016, 10250, 500, 34340, 180)
    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 9)

    If(
        (
            (Expr.Eval, "OP_29(0x0044, 0x01, 0x2000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2438',
    )

    OP_28(0x0044, 0x01, 0x2000)

    Jump('loc_245F')

    def _loc_2438(): pass

    label('loc_2438')

    If(
        (
            (Expr.Eval, "OP_29(0x0044, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_244D',
    )

    OP_28(0x0044, 0x01, 0x4000)

    Jump('loc_245F')

    def _loc_244D(): pass

    label('loc_244D')

    If(
        (
            (Expr.Eval, "OP_29(0x0044, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_245F',
    )

    OP_28(0x0044, 0x01, 0x8000)

    def _loc_245F(): pass

    label('loc_245F')

    SetScenaFlags(ScenaFlag(0x00A9, 5, 0x54D))
    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x2465
@scena.Code('func_0D_2465')
def func_0D_2465():
    If(
        (
            (Expr.Eval, "OP_29(0x0044, 0x01, 0x2000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_247A',
    )

    OP_28(0x0044, 0x01, 0x2000)

    Jump('loc_24A1')

    def _loc_247A(): pass

    label('loc_247A')

    If(
        (
            (Expr.Eval, "OP_29(0x0044, 0x01, 0x4000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_248F',
    )

    OP_28(0x0044, 0x01, 0x4000)

    Jump('loc_24A1')

    def _loc_248F(): pass

    label('loc_248F')

    If(
        (
            (Expr.Eval, "OP_29(0x0044, 0x01, 0x8000)"),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_24A1',
    )

    OP_28(0x0044, 0x01, 0x8000)

    def _loc_24A1(): pass

    label('loc_24A1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00A9, 6, 0x54E)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2661',
    )

    EventBegin(0x00)
    CameraMove(-12420, 0, 7490, 0)
    SetChrPos(0x0101, -12410, 0, 6160, 45)
    SetChrPos(0x0106, -12420, 0, 5400, 45)
    SetChrPos(0x0102, -12450, 0, 7280, 45)
    SetChrPos(0x0107, -13200, 0, 7280, 45)
    SetChrPos(0x010B, -13200, 0, 6480, 45)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0107,
        (
            '#0070091156V#561F哈啊哈啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070091157V#063F不、不要紧吗……\n',
            '那些士兵们……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0106,
        (
            '#0050091158V#053F啊～不要担心了。\n',
            '只是让他们晕过去了而已。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050091159V#552F不过不管怎么说，\n',
            '还是尽量避免战斗吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020091160V#012F要避开士兵们的搜索\n',
            '找到逃出去的路线。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    SetChrPos(0x0014, 11810, 0, 31000, 0)
    SetChrPos(0x0015, 8930, 0, 32619, 270)
    SetChrPos(0x0016, 10250, 500, 34340, 180)
    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 9)
    SetScenaFlags(ScenaFlag(0x00A9, 6, 0x54E))
    EventEnd(0x00)

    Jump('loc_26C9')

    def _loc_2661(): pass

    label('loc_2661')

    CameraMove(-12420, 0, 7490, 0)
    SetChrPos(0x0000, -12410, 0, 6160, 45)
    SetChrPos(0x0106, -12420, 0, 5400, 45)
    SetChrPos(0x0102, -12450, 0, 7280, 45)
    SetChrPos(0x0107, -13200, 0, 7280, 45)
    SetChrPos(0x010B, -13200, 0, 6480, 45)
    OP_30(0x01)

    def _loc_26C9(): pass

    label('loc_26C9')

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
