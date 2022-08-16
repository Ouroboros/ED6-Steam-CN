import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4120_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4120   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4120.x'
    header.mapIndex       = 1
    header.bgm            = 14
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
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
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01140._CH', 'ED6_DT07/CH01140P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01043._CH', 'ED6_DT07/CH01043P._CP'),
        ('ED6_DT07/CH01680._CH', 'ED6_DT07/CH01680P._CP'),
    ]

# id: 0x10001 offset: 0xD2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '夏伊',
            x                   = 1260,
            z                   = 0,
            y                   = -240,
            direction           = 236,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '史帕德',
            x                   = -500,
            z                   = 0,
            y                   = 129840,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
        ScenaNpcData(
            name                = '塞森',
            x                   = 58580,
            z                   = 0,
            y                   = 360,
            direction           = 102,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '多姆',
            x                   = 120030,
            z                   = 0,
            y                   = -1260,
            direction           = 10,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
    )

# id: 0x10002 offset: 0x152
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x152
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x152
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -10,
            triggerZ            = 0,
            triggerY            = -1600,
            triggerRange        = 800,
            actorX              = 1260,
            actorZ              = 1500,
            actorY              = -240,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0005,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 60410,
            triggerZ            = 0,
            triggerY            = 390,
            triggerRange        = 800,
            actorX              = 58580,
            actorZ              = 1500,
            actorY              = 360,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0003,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 119960,
            triggerZ            = 0,
            triggerY            = 650,
            triggerRange        = 800,
            actorX              = 120030,
            actorZ              = 1500,
            actorY              = -1260,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1BE
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_1DC',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000B, 0x0080)
    ChrSetFlags(0x0009, 0x0080)
    ChrSetFlags(0x0008, 0x0080)

    Jump('loc_2FC')

    def _loc_1DC(): pass

    label('loc_1DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1E6',
    )

    Jump('loc_2FC')

    def _loc_1E6(): pass

    label('loc_1E6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1F0',
    )

    Jump('loc_2FC')

    def _loc_1F0(): pass

    label('loc_1F0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Return,
        ),
        'loc_1FA',
    )

    Jump('loc_2FC')

    def _loc_1FA(): pass

    label('loc_1FA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            Expr.Return,
        ),
        'loc_22D',
    )

    TerminateThread(0x000B, 0x00)
    ChrSetSubChip(0x000B, 0)
    ChrSetChipByIndex(0x000B, 3)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000B, 0x0010)
    ChrSetPos(0x000B, 125240, 200, -1310, 90)

    Jump('loc_2FC')

    def _loc_22D(): pass

    label('loc_22D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 0, 0x1638)),
            Expr.Return,
        ),
        'loc_237',
    )

    Jump('loc_2FC')

    def _loc_237(): pass

    label('loc_237')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C6, 6, 0x1636)),
            Expr.Return,
        ),
        'loc_241',
    )

    Jump('loc_2FC')

    def _loc_241(): pass

    label('loc_241')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_24B',
    )

    Jump('loc_2FC')

    def _loc_24B(): pass

    label('loc_24B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_27E',
    )

    TerminateThread(0x000B, 0x00)
    ChrSetSubChip(0x000B, 0)
    ChrSetChipByIndex(0x000B, 3)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000B, 0x0010)
    ChrSetPos(0x000B, 125240, 200, -1310, 90)

    Jump('loc_2FC')

    def _loc_27E(): pass

    label('loc_27E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Return,
        ),
        'loc_2B1',
    )

    TerminateThread(0x000B, 0x00)
    ChrSetSubChip(0x000B, 0)
    ChrSetChipByIndex(0x000B, 3)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000B, 0x0010)
    ChrSetPos(0x000B, 125240, 200, -1310, 90)

    Jump('loc_2FC')

    def _loc_2B1(): pass

    label('loc_2B1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2E8',
    )

    TerminateThread(0x000B, 0x00)
    ChrSetSubChip(0x000B, 0)
    ChrSetChipByIndex(0x000B, 3)
    ChrSetFlags(0x000B, 0x0004)
    ChrSetFlags(0x000B, 0x0010)
    ChrSetPos(0x000B, 125240, 200, -1310, 90)

    Jump('loc_2FC')

    def _loc_2E8(): pass

    label('loc_2E8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_2F2',
    )

    Jump('loc_2FC')

    def _loc_2F2(): pass

    label('loc_2F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_2FC',
    )

    Jump('loc_2FC')

    def _loc_2FC(): pass

    label('loc_2FC')

    Return()

# id: 0x0001 offset: 0x2FD
@scena.Code('func_01_2FD')
def func_01_2FD():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0407, 3, 0x203B)),
            Expr.Return,
        ),
        'loc_310',
    )

    OP_64(0x00, 0x0001)
    OP_64(0x01, 0x0001)
    OP_64(0x02, 0x0001)

    def _loc_310(): pass

    label('loc_310')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_324',
    )

    OP_64(0x02, 0x0001)

    def _loc_324(): pass

    label('loc_324')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 2, 0x162A)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_340',
    )

    OP_B1('t4120_y')

    Jump('loc_349')

    def _loc_340(): pass

    label('loc_340')

    OP_B1('t4120_n')

    def _loc_349(): pass

    label('loc_349')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_369',
    )

    OP_72(0x0001, 0x0020)
    OP_72(0x0001, 0x0008)
    OP_72(0x0002, 0x0020)
    OP_72(0x0002, 0x0008)

    def _loc_369(): pass

    label('loc_369')

    Return()

# id: 0x0002 offset: 0x36A
@scena.Code('func_02_36A')
def func_02_36A():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_38D',
    )

    OP_8D(0x0009, 1470, 131290, -1690, 128210, 2000)

    Jump('func_02_36A')

    def _loc_38D(): pass

    label('loc_38D')

    Return()

# id: 0x0003 offset: 0x38E
@scena.Code('func_03_38E')
def func_03_38E():
    Call(0, 0x0004)

    Return()

# id: 0x0004 offset: 0x393
@scena.Code('func_04_393')
def func_04_393():
    TalkBegin(0x000A)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Neq,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 5, 0x20E5)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_3E2',
    )

    Call(6, 0x0003)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_3CE',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_3C8',
    )

    OP_A9(0xDB)

    Jump('loc_3CA')

    def _loc_3C8(): pass

    label('loc_3C8')

    OP_A9(0xC8)

    def _loc_3CA(): pass

    label('loc_3CA')

    TalkEnd(0x000A)

    Return()

    def _loc_3CE(): pass

    label('loc_3CE')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_3DF',
    )

    TalkEnd(0x000A)

    Return()

    def _loc_3DF(): pass

    label('loc_3DF')

    Jump('loc_ED9')

    def _loc_3E2(): pass

    label('loc_3E2')

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_ED9',
    )

    EventBegin(0x00)
    Fade(1000)
    ChrSetPos(0x0101, 60400, 0, -60, 270)
    ChrSetPos(0x0102, 60400, 0, 800, 270)

    If(
        (
            (Expr.Eval, "OP_CB(0xF8)"),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_449',
    )

    ChrSetPos(0x00F9, 61510, 0, -60, 270)
    ChrSetPos(0x00F8, 61510, 0, 800, 270)

    Jump('loc_46B')

    def _loc_449(): pass

    label('loc_449')

    ChrSetPos(0x00F8, 61510, 0, -60, 270)
    ChrSetPos(0x00F9, 61510, 0, 800, 270)

    def _loc_46B(): pass

    label('loc_46B')

    ChrSetDirection(0x000A, 90, 0)
    CameraMove(60390, 0, 280, 0)
    OP_0D()
    Sleep(400)

    ChrTalk(
        0x000A,
        (
            '啊，不好意思，\n',
            '工房现在不能用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '前几天导力驱动的\n',
            '器材就全部不动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真是莫名其妙……\n',
            '这样的话生意都没法做了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 2, 0x20E2)),
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 3, 0x20E3)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 4, 0x20E4)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 5, 0x20E5)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 6, 0x20E6)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_563',
    )

    ChrTalk(
        0x0101,
        (
            '#1018F#4P啊，那个不用担心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我们带了好东西来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '好东西？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9D2')

    def _loc_563(): pass

    label('loc_563')

    ChrTalk(
        0x0101,
        (
            '#1026F#4P啊，是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1015F唔，不过还是很麻烦啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '结晶回路的合成和结晶孔的强化\n',
            '都完全不能进行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_62F',
    )

    ChrTalk(
        0x0103,
        (
            '#025F就算能用魔法，\n',
            '像现在这样也有点不方便。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '难得的发生器也\n',
            '也变宝为废了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6F6')

    def _loc_62F(): pass

    label('loc_62F')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_697',
    )

    ChrTalk(
        0x0108,
        (
            '#072F呼，就算能用魔法，\n',
            '像现在这样也有点不方便。÷',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '难得的发生器也\n',
            '也变宝为废了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6F6')

    def _loc_697(): pass

    label('loc_697')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['阿加特'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_6F6',
    )

    ChrTalk(
        0x0106,
        (
            '#552F就算能用魔法，\n',
            '像现在这样也有点不方便。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '难得的发生器也\n',
            '也变宝为废了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6F6(): pass

    label('loc_6F6')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_73D',
    )

    ChrTalk(
        0x0107,
        (
            '#064F啊，可是姐姐……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '临时性的话\n',
            '可能会有办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_779')

    def _loc_73D(): pass

    label('loc_73D')

    ChrTalk(
        0x0102,
        (
            '#1043F#1P确实……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#1040F不过临时性的话\n',
            '可能会有办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_779(): pass

    label('loc_779')

    Sleep(400)

    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_7F6',
    )

    @scena.Lambda('lambda_07A9')
    def lambda_07A9():
        ChrTurnDirection(0x0000, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_07A9)

    Sleep(120)

    @scena.Lambda('lambda_07BC')
    def lambda_07BC():
        ChrTurnDirection(0x0001, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_07BC)

    @scena.Lambda('lambda_07CA')
    def lambda_07CA():
        ChrTurnDirection(0x0002, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_07CA)

    Sleep(120)

    @scena.Lambda('lambda_07DD')
    def lambda_07DD():
        ChrTurnDirection(0x0003, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_07DD)

    @scena.Lambda('lambda_07EB')
    def lambda_07EB():
        ChrTurnDirection(0x000A, 0x0107, 400)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_07EB)

    Jump('loc_7FD')

    def _loc_7F6(): pass

    label('loc_7F6')

    ChrTurnDirection(0x0101, 0x0102, 400)

    def _loc_7FD(): pass

    label('loc_7FD')

    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0001, 0x0001)
    WaitForThreadExit(0x0002, 0x0001)
    WaitForThreadExit(0x0003, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#1004F#4P咦……什么意思！？',
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
        'loc_862',
    )

    ChrTalk(
        0x0106,
        (
            '#052F能让工房恢复使用吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8BF')

    def _loc_862(): pass

    label('loc_862')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['雪拉扎德'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_892',
    )

    ChrTalk(
        0x0103,
        (
            '#023F能让工房恢复使用吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_8BF')

    def _loc_892(): pass

    label('loc_892')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['金'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_8BF',
    )

    ChrTalk(
        0x0108,
        (
            '#073F能让工房恢复使用吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_8BF(): pass

    label('loc_8BF')

    If(
        (
            (Expr.Eval, "OP_42(ChrTable['提妲'])"),
            (Expr.PushLong, 0x1),
            Expr.Neg,
            Expr.Neq,
            Expr.Return,
        ),
        'loc_901',
    )

    ChrTalk(
        0x0107,
        (
            '#060F是，是，大概……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '用那个发生器的话……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_938')

    def _loc_901(): pass

    label('loc_901')

    ChrTalk(
        0x0102,
        (
            '#1040F#1P是，恐怕……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '用那个发生器的花，有可能。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_938(): pass

    label('loc_938')

    ChrTalk(
        0x0101,
        (
            '#1018F#4P啊，原来如此！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '喂，你们……\n',
            '从刚才起在说些什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_0982')
    def lambda_0982():
        ChrTurnDirection(0x0000, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_0982)

    Sleep(120)

    @scena.Lambda('lambda_0995')
    def lambda_0995():
        ChrTurnDirection(0x0001, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0001, 0x0001, lambda_0995)

    @scena.Lambda('lambda_09A3')
    def lambda_09A3():
        ChrTurnDirection(0x0002, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0002, 0x0001, lambda_09A3)

    Sleep(120)

    @scena.Lambda('lambda_09B6')
    def lambda_09B6():
        ChrTurnDirection(0x0003, 0x000A, 400)

        ExitThread()

    DispatchAsync(0x0003, 0x0001, lambda_09B6)

    WaitForThreadExit(0x0000, 0x0001)
    WaitForThreadExit(0x0001, 0x0001)
    WaitForThreadExit(0x0002, 0x0001)
    WaitForThreadExit(0x0003, 0x0001)

    def _loc_9D2(): pass

    label('loc_9D2')

    ChrTalk(
        0x0102,
        (
            '#1040F#1P那个，是这样的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '说明了使用『零力场发生器』\n',
            '可暂时恢复工房机能的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    ChrTurnDirection(0x000A, 0x0102, 400)

    ChrTalk(
        0x000A,
        (
            '这是真的吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '工房的器材就在那里。\n',
            '你们能不能快点试试？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1006F#4P好的。',
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
        'loc_AD6',
    )

    ChrTalk(
        0x0107,
        (
            '#560F那么～\n',
            '请稍等。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AF9')

    def _loc_AD6(): pass

    label('loc_AD6')

    ChrTalk(
        0x0102,
        (
            '#1040F#1P那我们就借用一会儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AF9(): pass

    label('loc_AF9')

    FadeOut(1000, 0, -1)
    OP_0D()
    Sleep(1000)

    PlaySE(157, 0x00, 0x64)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '使用『零力场发生器』将工房机能恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x000A,
        (
            '哦哦……\n',
            '导力好象确实恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 2, 0x20E2)),
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 3, 0x20E3)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 4, 0x20E4)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 5, 0x20E5)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x041C, 6, 0x20E6)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_BBC',
    )

    ChrTurnDirection(0x000A, 0x0000, 400)

    ChrTalk(
        0x000A,
        (
            '好，要调整导力器的话\n',
            '就趁现在了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CEE')

    def _loc_BBC(): pass

    label('loc_BBC')

    ChrTalk(
        0x0101,
        (
            '#1000F#4P听好了……\n',
            '看来是成功了。',
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
        'loc_C3F',
    )

    ChrTalk(
        0x0107,
        (
            '#063F嗯，不过是暂时\n',
            '能用而已……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#561F过一会儿应该\n',
            '就会再度停下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_C96')

    def _loc_C3F(): pass

    label('loc_C3F')

    ChrTalk(
        0x0102,
        (
            '#1040F#1P虽然很顺利……\n',
            '不过这也只能算是应急措施。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '过一会儿应该\n',
            '就会再度停下来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_C96(): pass

    label('loc_C96')

    ChrTurnDirection(0x000A, 0x0000, 400)

    ChrTalk(
        0x000A,
        (
            '唔，是吗，\n',
            '不是真的修好了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过你们可以趁现在\n',
            '调整导力器什么的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_59()

    def _loc_CEE(): pass

    label('loc_CEE')

    FadeIn(300, 0)
    OP_0D()
    OP_A9(0x77)
    OP_56(0x00)
    OP_0D()
    Sleep(30)

    ChrTalk(
        0x000A,
        (
            '即便如此，这个叫发生器的\n',
            '东西还真了不起啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '价钱是好商量……\n',
            '不过你们多少钱肯卖？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1004F#4P咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '就算价格高一些\n',
            '我们也可以事先研究。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '因为只有我们的器材能\n',
            '用的话说不定能发一笔大财。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1016F#4P那、那个……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#1040F#1P非常抱歉，\n',
            '这是我们执行任务所必须的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '而且就算工房营业，\n',
            '市民们的导力器不能使用\n',
            '也一样没有意义……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '唔，我把这事给忘了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '那么你们来店里的话\n',
            '就把那东西带过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '那样的话就能像过去一样地\n',
            '使用工房了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x041C, 5, 0x20E5))
    EventEnd(0x00)
    TalkEnd(0x000A)

    Return()

    def _loc_ED9(): pass

    label('loc_ED9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_FED',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_F98',
    )

    ChrTalk(
        0x000A,
        (
            '嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '导力停止的时候\n',
            '顾客都涌进来问\n',
            '是不是商品的缺陷和故障。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过在多姆的解释下，\n',
            '大家似乎都理解了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '如果只有我一个人的话，\n',
            '可能无法很好地说服他们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_FEA')

    def _loc_F98(): pass

    label('loc_F98')

    ChrTalk(
        0x000A,
        (
            '不过在这种情况下，\n',
            '商品应该是卖不出去的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我到现在为止\n',
            '都干了些什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_FEA(): pass

    label('loc_FEA')

    Jump('loc_1636')

    def _loc_FED(): pass

    label('loc_FED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_110F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_10B0',
    )

    ChrTalk(
        0x000A,
        (
            '昨晚在西街区\n',
            '据说导力全停止了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我记得前不久在蔡斯\n',
            '也发生过类似的事件。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '如果导力器不能用了的话\n',
            '这店就要关门大吉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我倾注在这座店里的\n',
            '人生也算玩儿完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_110C')

    def _loc_10B0(): pass

    label('loc_10B0')

    ChrTalk(
        0x000A,
        (
            '如果导力器不能用了的话\n',
            '这店就要关门大吉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我倾注在这座店里的\n',
            '人生也算玩儿完了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_110C(): pass

    label('loc_110C')

    Jump('loc_1636')

    def _loc_110F(): pass

    label('loc_110F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Return,
        ),
        'loc_1119',
    )

    Jump('loc_1636')

    def _loc_1119(): pass

    label('loc_1119')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            Expr.Return,
        ),
        'loc_1123',
    )

    Jump('loc_1636')

    def _loc_1123(): pass

    label('loc_1123')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_11D6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C8, 6, 0x1646)),
            Expr.Return,
        ),
        'loc_1197',
    )

    ChrTalk(
        0x000A,
        (
            '……穿白色衣服的女孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '莫非，\n',
            '就是你们以前带来过的那孩子吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不，今天我没看见哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_11D3')

    def _loc_1197(): pass

    label('loc_1197')

    ChrTalk(
        0x000A,
        (
            '……穿白色衣服的女孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不，应该说没来过店里吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_11D3(): pass

    label('loc_11D3')

    Jump('loc_1636')

    def _loc_11D6(): pass

    label('loc_11D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_1217',
    )

    ChrTalk(
        0x000A,
        (
            '多姆昨天好像也\n',
            '通宵修理商品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '真是个傻瓜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1636')

    def _loc_1217(): pass

    label('loc_1217')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1285',
    )

    ChrTalk(
        0x000A,
        (
            '别看多姆那个样子，\n',
            '他从小就很顽固……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不过就算我们从小一起长大，\n',
            '这次我也不能让着他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1636')

    def _loc_1285(): pass

    label('loc_1285')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_13C0',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_136E',
    )

    ChrTalk(
        0x000A,
        (
            '……我和搭档多姆大吵了一架。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '最近那家伙整天就是修理修理的，\n',
            '根本不过来我这边帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '如果顾客买新的\n',
            '来替换坏了的东西，\n',
            '店里的销售额就会上升。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '像他那么做的话，我就好像是\n',
            '花钱养一个让我赔本的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_13BD')

    def _loc_136E(): pass

    label('loc_136E')

    ChrTalk(
        0x000A,
        (
            '我没做错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '……就算是工房，\n',
            '也是一家店铺。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不赚钱就经营不下去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_13BD(): pass

    label('loc_13BD')

    Jump('loc_1636')

    def _loc_13C0(): pass

    label('loc_13C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_154C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C8, 6, 0x1646)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_14F3',
    )

    ChrTalk(
        0x000A,
        (
            '呀，欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#264F……这里是卖导力器的？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '比玲家的附近的店\n',
            '货色更齐全呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000A, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    ChrTurnDirection(0x000A, 0x012F, 400)
    Sleep(1000)

    ChrTalk(
        0x000A,
        (
            '小妹妹你莫非是\n',
            '从外国来的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '要不要买点利贝尔制的\n',
            '导力器回去送人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#260F这主意不错。\n',
            '不过玲没带钱。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '等爸爸妈妈来接我时\n',
            '我再过来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '嗯，我们等着你！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02C8, 6, 0x1646))

    Jump('loc_1549')

    def _loc_14F3(): pass

    label('loc_14F3')

    ChrTalk(
        0x000A,
        (
            '多姆那家伙昨晚修理\n',
            '别人送来的东西到很晚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '就算急着修好，别人\n',
            '也不会多加钱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1549(): pass

    label('loc_1549')

    Jump('loc_1636')

    def _loc_154C(): pass

    label('loc_154C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1636',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_15E2',
    )

    ChrTalk(
        0x000A,
        (
            '我的搭档多姆就算再忙\n',
            '也不会拒绝修理的请求。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '明明卖出新产品比修理\n',
            '来钱更快啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我真希望多姆能学好\n',
            '优先考虑利益啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_1636')

    def _loc_15E2(): pass

    label('loc_15E2')

    ChrTalk(
        0x000A,
        (
            '……明明卖出新产品比修理\n',
            '来钱更快啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我真希望多姆能学好\n',
            '优先考虑利益啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1636(): pass

    label('loc_1636')

    TalkEnd(0x000A)

    Return()

# id: 0x0005 offset: 0x163A
@scena.Code('func_05_163A')
def func_05_163A():
    Call(0, 0x0006)

    Return()

# id: 0x0006 offset: 0x163F
@scena.Code('func_06_163F')
def func_06_163F():
    TalkBegin(0x0008)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_166A',
    )

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x8),
            Expr.Geq,
            Expr.Return,
        ),
        'loc_1664',
    )

    OP_A9(0xDA)

    Jump('loc_1666')

    def _loc_1664(): pass

    label('loc_1664')

    OP_A9(0xC9)

    def _loc_1666(): pass

    label('loc_1666')

    TalkEnd(0x0008)

    Return()

    def _loc_166A(): pass

    label('loc_166A')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_167B',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_167B(): pass

    label('loc_167B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_16D6',
    )

    ChrTalk(
        0x0008,
        (
            '和那个人在一起我就无所畏惧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '从前就没有导力器，\n',
            '我们不也活得好好的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D22')

    def _loc_16D6(): pass

    label('loc_16D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_17AF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_176F',
    )

    ChrTalk(
        0x0008,
        (
            '因为夫妻吵架，\n',
            '我正准备离家出走，\n',
            '他把我挽留下来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '他因此终于\n',
            '倾吐出了自己的心声。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '原来他比我想象中的要\n',
            '体贴人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_17AC')

    def _loc_176F(): pass

    label('loc_176F')

    ChrTalk(
        0x0008,
        (
            '说起来，吵架的时候\n',
            '街上好像很吵……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '发生了什么呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17AC(): pass

    label('loc_17AC')

    Jump('loc_1D22')

    def _loc_17AF(): pass

    label('loc_17AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Return,
        ),
        'loc_17B9',
    )

    Jump('loc_1D22')

    def _loc_17B9(): pass

    label('loc_17B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            Expr.Return,
        ),
        'loc_17C3',
    )

    Jump('loc_1D22')

    def _loc_17C3(): pass

    label('loc_17C3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_184C',
    )

    ChrTalk(
        0x0008,
        (
            '不论是夫妇还是别的关系，\n',
            '有些话不说对方永远\n',
            '不会知道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '一直沉默不语的话\n',
            '就无法互相沟通了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '你不这么认为吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D22')

    def _loc_184C(): pass

    label('loc_184C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_18CC',
    )

    ChrTalk(
        0x0008,
        (
            '我们结婚\n',
            '已经五年多了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '可我先生无论是我发脾气\n',
            '还是哭泣都不会过来问一句话。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不知道他到底在想什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D22')

    def _loc_18CC(): pass

    label('loc_18CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_19DB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1968',
    )

    ChrTalk(
        0x0008,
        (
            '我先生不仅沉默寡言，\n',
            '还不愿意和人接触。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '今天好像也一直\n',
            '在仓库里干活儿。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我们要靠做买卖为生，\n',
            '真希望他能再改进一点。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    Jump('loc_19D8')

    def _loc_1968(): pass

    label('loc_1968')

    ChrTalk(
        0x0008,
        (
            '就算沉默寡言改不了，\n',
            '至少能变得更亲切一点也好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '但是硬让他笑\n',
            '也只像是在痉挛……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我该怎么办才好？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19D8(): pass

    label('loc_19D8')

    Jump('loc_1D22')

    def _loc_19DB(): pass

    label('loc_19DB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1A35',
    )

    ChrTalk(
        0x0008,
        (
            '可能互不侵犯条约的签字仪式\n',
            '临近了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '最近感觉城里似乎\n',
            '挺有活力的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D22')

    def _loc_1A35(): pass

    label('loc_1A35')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_1C5B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C9, 3, 0x164B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1BE6',
    )

    ChrTalk(
        0x0008,
        (
            '欢迎来到瓦伊斯武器商会！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(600)

    ChrTurnDirection(0x0008, 0x012F, 400)

    ChrTalk(
        0x0008,
        (
            '哎呀呀，\n',
            '这小妹妹真可爱。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x012F, 0x0008, 400)

    ChrTalk(
        0x012F,
        (
            '#264F……莫非你是\n',
            '在说玲？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嗯，是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我要是也有一个\n',
            '你这样的女儿就好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '怎么样？要不要当我的孩子？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#267F玲有自己很喜欢的\n',
            '爸爸和妈妈……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#260F很遗憾，\n',
            '不能当阿姨的孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哈哈，开玩笑啦。\n',
            '我倒是想给你糖吃……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过不巧的是\n',
            '这里只有武器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#261F呵呵，没关系的。\n',
            '心领了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02C9, 3, 0x164B))

    Jump('loc_1C58')

    def _loc_1BE6(): pass

    label('loc_1BE6')

    ChrTalk(
        0x0008,
        (
            '如果我有个女儿的话，就能\n',
            '让她陪我买东西和聊天了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……我先生真的是沉默寡言，\n',
            '至少有个孩子在我身边也好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C58(): pass

    label('loc_1C58')

    Jump('loc_1D22')

    def _loc_1C5B(): pass

    label('loc_1C5B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_1D22',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CF, 2, 0x67A)),
            Expr.Return,
        ),
        'loc_1CD4',
    )

    ChrTalk(
        0x0008,
        (
            '哎呀，你是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '你是武术大会冠军队的\n',
            '游击士小姐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呵呵，欢迎欢迎。\n',
            '你们能来真是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D22')

    def _loc_1CD4(): pass

    label('loc_1CD4')

    ChrTalk(
        0x0008,
        (
            '欢迎光临。\n',
            '欢迎来到瓦伊斯武器商会！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这里有各种武器哟。\n',
            '请慢慢选购。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D22(): pass

    label('loc_1D22')

    TalkEnd(0x0008)

    Return()

# id: 0x0007 offset: 0x1D26
@scena.Code('func_07_1D26')
def func_07_1D26():
    Call(0, 0x0008)

    Return()

# id: 0x0008 offset: 0x1D2B
@scena.Code('func_08_1D2B')
def func_08_1D2B():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_1DD2',
    )

    ChrTalk(
        0x000B,
        (
            '大家似乎都终于接受\n',
            '导力器全部无法使用\n',
            '这一事实了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '艾莉茜雅女王发布的\n',
            '公告好象也有效果了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '总之现在只能一边努力\n',
            '做力所能及的事一边忍耐了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2207')

    def _loc_1DD2(): pass

    label('loc_1DD2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_1E22',
    )

    ChrTalk(
        0x000B,
        (
            '自从吵架之后，\n',
            '塞森都不理我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不过我可没认为\n',
            '自己做错了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2207')

    def _loc_1E22(): pass

    label('loc_1E22')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Return,
        ),
        'loc_1E2C',
    )

    Jump('loc_2207')

    def _loc_1E2C(): pass

    label('loc_1E2C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            Expr.Return,
        ),
        'loc_1E36',
    )

    Jump('loc_2207')

    def _loc_1E36(): pass

    label('loc_1E36')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_1ED0',
    )

    ChrTalk(
        0x000B,
        (
            '塞森是和我从小一起长大的，\n',
            '以前就经常吵架。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那家伙就知道钱钱钱，\n',
            '太沉溺在其中了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '钱确实重要，\n',
            '不过真正的工房不应该\n',
            '只追求这个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2207')

    def _loc_1ED0(): pass

    label('loc_1ED0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_1F47',
    )

    ChrTalk(
        0x000B,
        (
            '………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '啊……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '……似乎在不知不觉中\n',
            '睡着了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '因为昨天睡得太晚了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2207')

    def _loc_1F47(): pass

    label('loc_1F47')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1F9E',
    )

    ChrTalk(
        0x000B,
        (
            '原来是……七耀石的\n',
            '接合部分松了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '换一下插座的话一定能……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2207')

    def _loc_1F9E(): pass

    label('loc_1F9E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_1FF8',
    )

    ChrTalk(
        0x000B,
        (
            '我喜欢欣赏重要的东西\n',
            '被修好时人们的笑容。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '那家伙为什么\n',
            '就不理解呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2207')

    def _loc_1FF8(): pass

    label('loc_1FF8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_21AE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_215D',
    )

    ChrTalk(
        0x000B,
        (
            '……这边是这样的，\n',
            '线路是那样的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x012F, 0x000B, 400)

    ChrTalk(
        0x012F,
        (
            '#264F大哥哥你在这里干什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000B, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(600)

    ChrTurnDirection(0x000B, 0x012F, 400)

    ChrTalk(
        0x000B,
        (
            '……我在修理赫穆特先生的\n',
            '导力灯。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '这好像是他珍藏了多年的,\n',
            '充满回忆的东西……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我一定要想办法帮他修好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x012F,
        (
            '#260F哦？\n',
            '大哥哥你真了不起。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '……咦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '啊，哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '哈哈，你这么说\n',
            '我可不好意思了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    Jump('loc_21AB')

    def _loc_215D(): pass

    label('loc_215D')

    ChrTalk(
        0x000B,
        (
            '整天修理的话\n',
            '塞森就会有意见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '不过我实在是不能\n',
            '丢开修理的活儿不管。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_21AB(): pass

    label('loc_21AB')

    Jump('loc_2207')

    def _loc_21AE(): pass

    label('loc_21AE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_2207',
    )

    ChrTalk(
        0x000B,
        (
            '呀，欢迎。\n',
            '这边是修理的接待窗口。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '如果有导力产品损坏\n',
            '可以拿来这里修理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2207(): pass

    label('loc_2207')

    TalkEnd(0x000B)

    Return()

# id: 0x0009 offset: 0x220B
@scena.Code('func_09_220B')
def func_09_220B():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_223F',
    )

    ChrTalk(
        0x00FE,
        (
            '不管发生什么，\n',
            '我都要保护妻子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_255E')

    def _loc_223F(): pass

    label('loc_223F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_22CF',
    )

    ChrTalk(
        0x00FE,
        (
            '我每天晚饭后\n',
            '都要跟妻子聊天。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我虽然一直以来都\n',
            '不太会表达自己的想法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可是我的想法如果不\n',
            '说出来的话\n',
            '她就无法知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_255E')

    def _loc_22CF(): pass

    label('loc_22CF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 2, 0x163A)),
            Expr.Return,
        ),
        'loc_22D9',
    )

    Jump('loc_255E')

    def _loc_22D9(): pass

    label('loc_22D9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 1, 0x1639)),
            Expr.Return,
        ),
        'loc_22E3',
    )

    Jump('loc_255E')

    def _loc_22E3(): pass

    label('loc_22E3')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_2343',
    )

    ChrTalk(
        0x00FE,
        (
            '我想感谢妻子，\n',
            '可我从来不擅长这些……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……那个……我究竟\n',
            '该怎样做才好呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_255E')

    def _loc_2343(): pass

    label('loc_2343')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 3, 0x162B)),
            Expr.Return,
        ),
        'loc_2399',
    )

    ChrTalk(
        0x00FE,
        (
            '这家店是我死去的父亲\n',
            '留给我的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我很感激帮我料理\n',
            '店铺的妻子……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_255E')

    def _loc_2399(): pass

    label('loc_2399')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2439',
    )

    ChrTalk(
        0x00FE,
        (
            '觉得肚子饿了\n',
            '已经傍晚了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '可能是因为呆在这里\n',
            '不了解外面的情况，\n',
            '总觉得时间过得很快……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然对我来说这种生活\n',
            '很轻松、很自由……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_255E')

    def _loc_2439(): pass

    label('loc_2439')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_24AF',
    )

    ChrTalk(
        0x00FE,
        (
            '互不侵犯条约啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不太了解详情，\n',
            '不过和平当然好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真希望我卖出去的武器\n',
            '能用来消灭魔兽……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_255E')

    def _loc_24AF(): pass

    label('loc_24AF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C2, 7, 0x1617)),
            Expr.Return,
        ),
        'loc_2510',
    )

    ChrTalk(
        0x00FE,
        (
            '……欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '想买武器的话就走上台阶\n',
            '绕到店铺的正面。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我妻子应该在柜台的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_255E')

    def _loc_2510(): pass

    label('loc_2510')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_255E',
    )

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典结束后城市\n',
            '也恢复了平静……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我喜欢这种程度的安静……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_255E(): pass

    label('loc_255E')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
