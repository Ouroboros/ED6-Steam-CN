import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4132_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4132   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4132.x'
    header.mapIndex       = 1
    header.bgm            = 14
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
        ('ED6_DT07/CH02060._CH', 'ED6_DT07/CH02060P._CP'),
        ('ED6_DT07/CH01620._CH', 'ED6_DT07/CH01620P._CP'),
        ('ED6_DT07/CH00175._CH', 'ED6_DT07/CH00175P._CP'),
        ('ED6_DT07/CH00176._CH', 'ED6_DT07/CH00176P._CP'),
        ('ED6_DT06/CH20041._CH', 'ED6_DT06/CH20041P._CP'),
        ('ED6_DT06/CH20047._CH', 'ED6_DT06/CH20047P._CP'),
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH02390._CH', 'ED6_DT07/CH02390P._CP'),
        ('ED6_DT07/CH02550._CH', 'ED6_DT07/CH02550P._CP'),
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH02600._CH', 'ED6_DT07/CH02600P._CP'),
    ]

# id: 0x10001 offset: 0x10A
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '奈尔',
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
            name                = '克鲁茨',
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
        ScenaNpcData(
            name                = '福立兹',
            x                   = 6940,
            z                   = 0,
            y                   = 3300,
            direction           = 166,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '乔儿',
            x                   = 6140,
            z                   = 0,
            y                   = -1760,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '汉斯',
            x                   = 7770,
            z                   = 0,
            y                   = -1720,
            direction           = 315,
            word_0E             = 0,
            dword_10            = 8,
            chipIndex           = 8,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '科洛丝',
            x                   = 6920,
            z                   = 0,
            y                   = -260,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 9,
            chipIndex           = 9,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '米亚尔',
            x                   = 36400,
            z                   = 0,
            y                   = 50700,
            direction           = 106,
            word_0E             = 0,
            dword_10            = 10,
            chipIndex           = 10,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '科林兹校长',
            x                   = 4320,
            z                   = 0,
            y                   = 1060,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 11,
            chipIndex           = 11,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
    )

# id: 0x10002 offset: 0x20A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x20A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x20A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 7060,
            triggerZ            = 0,
            triggerY            = 1700,
            triggerRange        = 800,
            actorX              = 6940,
            actorZ              = 1500,
            actorY              = 3300,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0009,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 7000,
            triggerZ            = 0,
            triggerY            = 4890,
            triggerRange        = 800,
            actorX              = 7000,
            actorZ              = 1000,
            actorY              = 4890,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0011,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x252
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_269',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, func_0C_1904)
    OP_B1('t4132_n')

    def _loc_269(): pass

    label('loc_269')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_280',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, func_0E_26BD)
    OP_B1('t4132_n')

    def _loc_280(): pass

    label('loc_280')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_2A0',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, func_0F_2A9B)
    OP_B1('t4132_n')

    def _loc_2A0(): pass

    label('loc_2A0')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000064, 'loc_2B0'),
        (0x00000078, 'loc_2CB'),
        (-1, 'loc_2E1'),
    )

    def _loc_2B0(): pass

    label('loc_2B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 0, 0x620)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 7, 0x61F)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2C8',
    )

    MapSetFlags(0x10000000)
    SetScenaFlags(ScenaFlag(0x00C4, 0, 0x620))
    Event(0, func_0D_2078)

    def _loc_2C8(): pass

    label('loc_2C8')

    Jump('loc_2E1')

    def _loc_2CB(): pass

    label('loc_2CB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 5, 0x64D)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_2DE',
    )

    SetScenaFlags(ScenaFlag(0x00C9, 5, 0x64D))
    Event(0, func_10_2EB2)

    def _loc_2DE(): pass

    label('loc_2DE')

    Jump('loc_2E1')

    def _loc_2E1(): pass

    label('loc_2E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_2FF',
    )

    ChrClearFlags(0x000B, 0x0080)
    ChrClearFlags(0x000C, 0x0080)
    ChrClearFlags(0x000D, 0x0080)
    ChrClearFlags(0x000F, 0x0080)

    Jump('loc_39F')

    def _loc_2FF(): pass

    label('loc_2FF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_30E',
    )

    ChrClearFlags(0x000E, 0x0080)

    Jump('loc_39F')

    def _loc_30E(): pass

    label('loc_30E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_318',
    )

    Jump('loc_39F')

    def _loc_318(): pass

    label('loc_318')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_322',
    )

    Jump('loc_39F')

    def _loc_322(): pass

    label('loc_322')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_32C',
    )

    Jump('loc_39F')

    def _loc_32C(): pass

    label('loc_32C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_353',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 32009, 0, 115490, 0)
    CreateThread(0x0009, 0x00, 0x00, func_02_3ED)

    Jump('loc_39F')

    def _loc_353(): pass

    label('loc_353')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_35D',
    )

    Jump('loc_39F')

    def _loc_35D(): pass

    label('loc_35D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_384',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0009, 32009, 0, 115490, 0)
    CreateThread(0x0009, 0x00, 0x00, func_02_3ED)

    Jump('loc_39F')

    def _loc_384(): pass

    label('loc_384')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_38E',
    )

    Jump('loc_39F')

    def _loc_38E(): pass

    label('loc_38E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_398',
    )

    Jump('loc_39F')

    def _loc_398(): pass

    label('loc_398')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_39F',
    )

    def _loc_39F(): pass

    label('loc_39F')

    Return()

# id: 0x0001 offset: 0x3A0
@scena.Code('func_01_3A0')
def func_01_3A0():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 1, 0x631)),
            Expr.Or,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 3, 0x623)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 3, 0x61B)),
            Expr.Or,
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 6, 0x616)),
            Expr.Nez64,
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3D3',
    )

    OP_B1('t4132_y')

    Jump('loc_3DC')

    def _loc_3D3(): pass

    label('loc_3D3')

    OP_B1('t4132_n')

    def _loc_3DC(): pass

    label('loc_3DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 2, 0x66A)),
            Expr.Return,
        ),
        'loc_3EC',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x4B),
            Expr.Nop,
            Expr.Return,
        ),
    )

    def _loc_3EC(): pass

    label('loc_3EC')

    Return()

# id: 0x0002 offset: 0x3ED
@scena.Code('func_02_3ED')
def func_02_3ED():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_402',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_3ED')

    def _loc_402(): pass

    label('loc_402')

    Return()

# id: 0x0003 offset: 0x403
@scena.Code('func_03_403')
def func_03_403():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_426',
    )

    OP_8D(0x00FE, 153520, 48510, 156020, 53700, 3000)

    Jump('func_03_403')

    def _loc_426(): pass

    label('loc_426')

    Return()

# id: 0x0004 offset: 0x427
@scena.Code('func_04_427')
def func_04_427():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '诞辰庆典之前的这几天\n',
            '就在这个酒店里\n',
            '舒舒服服地度过吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不愧是王国最大的酒店。\n',
            '真是豪华啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x493
@scena.Code('func_05_493')
def func_05_493():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Return,
        ),
        'loc_4FA',
    )

    ChrTalk(
        0x000D,
        (
            '#0060140798V#040F艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060140799V能够遇到你们两个，\n',
            '我真是太幸福了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D7')

    def _loc_4FA(): pass

    label('loc_4FA')

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))
    SetScenaFlags(ScenaFlag(0x00DE, 2, 0x6F2))

    ChrTalk(
        0x000D,
        (
            '#0060140785V#040F艾丝蒂尔、约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140786V#000F科洛丝，原来你在这里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060140787V#045F嗯，是啊。\n',
            '我听说校长、乔儿和汉斯他们都来这里了……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060140788V所以就从王城里面偷偷跑了出来。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140789V#001F啊哈哈，真看不出来，\n',
            '科洛丝你也会做出这么大胆的行动呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060140790V#041F呵呵，这次真是多谢你们了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060140791V我从头到尾一直都承蒙你们两位的关照。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140792V#505F嗯～我觉得倒是\n',
            '科洛丝你教会了我许多东西。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140793V待人温柔，意志坚强……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140794V#008F对不起，我不太会说话，\n',
            '所以说不出什么好的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140795V#006F总之，我们以后继续像现在这样\n',
            '互相帮助，一起努力就可以了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#0060140796V#044F艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060140797V#048F能够遇到你们两个，\n',
            '我真是太幸福了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7D7(): pass

    label('loc_7D7')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x7DB
@scena.Code('func_06_7DB')
def func_06_7DB():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Return,
        ),
        'loc_873',
    )

    ChrTalk(
        0x00FE,
        (
            '#0520140817V#730F虽然发生了许多的事情，\n',
            '不过看到你们俩这么有精神，我就放心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520140816V如果再到卢安来的话，\n',
            '记得到学院来玩玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_A6F')

    def _loc_873(): pass

    label('loc_873')

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))
    ChrTurnDirection(0x00FE, 0x0102, 400)

    ChrTalk(
        0x00FE,
        (
            '#0520140808V#730F哟，约修亚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140809V#014F这不是汉斯吗。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140810V为什么会在这里呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0520140811V#734F喂喂……\n',
            '这么久没见面了，\n',
            '你却说出这样绝情的话来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520140812V#730F自从学园祭之后，\n',
            '又回到独自过夜的生活真是寂寞啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520140813V#731F因为对你难以忘怀，\n',
            '所以千里迢迢追到王都来了哦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020140814V#019F哈哈，你还是老样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0520140815V#730F嗯，虽然发生了许多的事情，\n',
            '不过看到你这么有精神，我就放心了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0520140816V如果再到卢安来的话，\n',
            '记得到学院来玩玩哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_A6F(): pass

    label('loc_A6F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0007 offset: 0xA73
@scena.Code('func_07_A73')
def func_07_A73():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Return,
        ),
        'loc_AF1',
    )

    ChrTalk(
        0x00FE,
        (
            '#0510140806V#640F我从科洛丝那里听说了，\n',
            '你们这次真是大显神威啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510140804V#648F不愧是红骑士尤利乌斯哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_BEE')

    def _loc_AF1(): pass

    label('loc_AF1')

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x00FE,
        (
            '#0510140800V#640F艾丝蒂尔、约修亚！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140801V#004F啊，乔儿！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0510140802V#641F好久不见了啦～',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510140803V我从科洛丝那里听说了，\n',
            '你们这次真是大显神威啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0510140804V#648F不愧是红骑士尤利乌斯哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010140805V#008F哈哈哈……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_BEE(): pass

    label('loc_BEE')

    TalkEnd(0x00FE)

    Return()

# id: 0x0008 offset: 0xBF2
@scena.Code('func_08_BF2')
def func_08_BF2():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#0530140819V#780F呵呵，好久不见了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0530140820V我和学院的学生代表乔儿还有汉斯一起\n',
            '来参加诞辰庆典了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0009 offset: 0xC68
@scena.Code('func_09_C68')
def func_09_C68():
    Call(0, 0x000A)

    Return()

# id: 0x000A offset: 0xC6D
@scena.Code('func_0A_C6D')
def func_0A_C6D():
    TalkBegin(0x000A)
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
            TXT(0x01, '休息\n'),
            TXT(0x02, '离开\n'),
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
        'loc_CC9',
    )

    OP_0D()
    OP_A9(0x5F)
    OP_56(0x00)
    TalkEnd(0x000A)

    Return()

    def _loc_CC9(): pass

    label('loc_CC9')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_CDA',
    )

    TalkEnd(0x000A)

    Return()

    def _loc_CDA(): pass

    label('loc_CDA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_D51',
    )

    ChrTalk(
        0x000A,
        (
            '不愧是诞辰庆典啊，\n',
            '比武术大会还要热闹许多。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '从外国来的客人\n',
            '也比历年的要多很多，\n',
            '真是快忙不过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15C9')

    def _loc_D51(): pass

    label('loc_D51')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_DC4',
    )

    ChrTalk(
        0x000A,
        (
            '正规军撤离了，\n',
            '取而代之是黑衣士兵\n',
            '在街上巡逻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽然诞辰庆典将近了，\n',
            '令人不安的事情却接踵而至。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15C9')

    def _loc_DC4(): pass

    label('loc_DC4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 5, 0x64D)),
            Expr.Return,
        ),
        'loc_E12',
    )

    ChrTalk(
        0x000A,
        (
            '克鲁茨先生\n',
            '刚才到外面去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '他的身体\n',
            '已经没有问题了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15C9')

    def _loc_E12(): pass

    label('loc_E12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_EC9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_E69',
    )

    ChrTalk(
        0x000A,
        (
            '刚才游击士\n',
            '克鲁茨先生回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但他的脸色\n',
            '似乎不是很好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_EC6')

    def _loc_E69(): pass

    label('loc_E69')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x000A,
        (
            '刚才游击士\n',
            '克鲁茨先生回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '但他的脸色\n',
            '似乎不是很好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '应该没事吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_EC6(): pass

    label('loc_EC6')

    Jump('loc_15C9')

    def _loc_EC9(): pass

    label('loc_EC9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_105A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_F41',
    )

    ChrTalk(
        0x000A,
        (
            '恭喜你们二人取得\n',
            '这次武术大会的优胜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '你们就不用在意\n',
            '这边的安排了。\n',
            '请好好享受王城的晚宴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1057')

    def _loc_F41(): pass

    label('loc_F41')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0101,
        (
            '#000F啊，福立兹先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '哦，艾丝蒂尔小姐，\n',
            '有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F今天晚上我们准备住在别的地方了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '嗯，\n',
            '之前艾南先生已经告知我了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '恭喜你们取得\n',
            '武术大会的优胜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '不用在意这边的安排，\n',
            '请好好享受王城的晚宴吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F不愧是艾南先生啊，\n',
            '动作这么快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1057(): pass

    label('loc_1057')

    Jump('loc_15C9')

    def _loc_105A(): pass

    label('loc_105A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_10CE',
    )

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔小姐，约修亚先生，\n',
            '今天是武术大会的决赛吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我会在这里默默支持各位的。\n',
            '请你们路上慢走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15C9')

    def _loc_10CE(): pass

    label('loc_10CE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_1207',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1150',
    )

    ChrTalk(
        0x000A,
        (
            '听说从今天起\n',
            '士兵就要严加巡逻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽然给你们带来种种不便，\n',
            '但是请不要在外面待得太晚，\n',
            '一定要早点回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1204')

    def _loc_1150(): pass

    label('loc_1150')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔小姐，约修亚先生，\n',
            '刚才收到了\n',
            '王国军发来的联络……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '听说从今天起\n',
            '他们就要严加巡逻了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '虽然给你们带来种种不便，\n',
            '但是请不要在外面待得太晚，\n',
            '一定要早点回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1204(): pass

    label('loc_1204')

    Jump('loc_15C9')

    def _loc_1207(): pass

    label('loc_1207')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_1255',
    )

    ChrTalk(
        0x000A,
        (
            '怎么样，\n',
            '昨晚睡得好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '今天是准决赛吧。\n',
            '请你们路上慢走。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15C9')

    def _loc_1255(): pass

    label('loc_1255')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_1333',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_12B2',
    )

    ChrTalk(
        0x000A,
        (
            '对了，\n',
            '还有另外两位游击士\n',
            '现在也住在酒店里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '你们见到他们了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1330')

    def _loc_12B2(): pass

    label('loc_12B2')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x000A,
        (
            '艾丝蒂尔小姐，约修亚先生，\n',
            '欢迎你们回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '对了，\n',
            '还有另外两位游击士\n',
            '现在也住在酒店里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '你们见到他们了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1330(): pass

    label('loc_1330')

    Jump('loc_15C9')

    def _loc_1333(): pass

    label('loc_1333')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_1384',
    )

    ChrTalk(
        0x000A,
        (
            '各位是大会的出场选手吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '期待你们大显身手，\n',
            '祝你们一路顺风。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15C9')

    def _loc_1384(): pass

    label('loc_1384')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_1552',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 7, 0x617)),
            Expr.Return,
        ),
        'loc_13EE',
    )

    ChrTalk(
        0x000A,
        (
            '两位的房间\n',
            '在楼上走廊尽头的\n',
            '２０２号室。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '如果有什么需要的话，\n',
            '请来前台告诉我。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_154F')

    def _loc_13EE(): pass

    label('loc_13EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_1477',
    )

    ChrTalk(
        0x000A,
        (
            '尊敬的客人，非常抱歉。\n',
            '现在还不能为你们安排房间，\n',
            '因为房间还没有清扫完毕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '想要在这里登记住宿的话，\n',
            '请三点以后再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_154F')

    def _loc_1477(): pass

    label('loc_1477')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x000A,
        (
            '尊敬的客人，非常抱歉。\n',
            '现在还不能为你们安排房间，\n',
            '因为房间还没有清扫完毕。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '想要在这里登记住宿的话，\n',
            '请三点以后再来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#010F待会儿来登记吧，\n',
            '还是先去找到金先生再说。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#001FＯＫ。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_154F(): pass

    label('loc_154F')

    Jump('loc_15C9')

    def _loc_1552(): pass

    label('loc_1552')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_15C9',
    )

    ChrTalk(
        0x000A,
        (
            '有许多客人\n',
            '都是从很远的地方\n',
            '赶来参加武术大会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '我们也非常欢迎\n',
            '参加大会的选手\n',
            '前来光顾我们的酒店呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15C9(): pass

    label('loc_15C9')

    TalkEnd(0x000A)

    Return()

# id: 0x000B offset: 0x15CD
@scena.Code('func_0B_15CD')
def func_0B_15CD():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_15DA',
    )

    Jump('loc_1900')

    def _loc_15DA(): pass

    label('loc_15DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_15E4',
    )

    Jump('loc_1900')

    def _loc_15E4(): pass

    label('loc_15E4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_15EE',
    )

    Jump('loc_1900')

    def _loc_15EE(): pass

    label('loc_15EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_15F8',
    )

    Jump('loc_1900')

    def _loc_15F8(): pass

    label('loc_15F8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_1602',
    )

    Jump('loc_1900')

    def _loc_1602(): pass

    label('loc_1602')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_16E7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1650',
    )

    ChrTalk(
        0x00FE,
        (
            '#0330110495V『不动金』自不用说，\n',
            '你们的战斗也十分出色。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16E4')

    def _loc_1650(): pass

    label('loc_1650')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0330110492V#840F哦，是你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330110493V『不动金』自不用说，\n',
            '你们的战斗也十分出色。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330110483V每个人的技术都不错，\n',
            '配合也相当熟练。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16E4(): pass

    label('loc_16E4')

    Jump('loc_1900')

    def _loc_16E7(): pass

    label('loc_16E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_16F1',
    )

    Jump('loc_1900')

    def _loc_16F1(): pass

    label('loc_16F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_18E5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_1766',
    )

    ChrTalk(
        0x00FE,
        (
            '#0330110498V#840F我们两组今天都能成功晋级，\n',
            '真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330110504V我很期待与你们的对战哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18E2')

    def _loc_1766(): pass

    label('loc_1766')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '#0330110496V#840F哟，这不是艾丝蒂尔和约修亚嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110497V#000F啊，克鲁茨前辈。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0330110498V#840F我们两组今天都能成功晋级，\n',
            '真是太好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330110499V虽然之前也听卡露娜说过，\n',
            '不过这次是亲眼见到你们的实力了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110500V#010F哪里，我们还在修行中。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110501V我们要在这次大会里\n',
            '多向前辈们学习才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '#0330110502V#841F哈哈，\n',
            '我很期待与你们的对战哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18E2(): pass

    label('loc_18E2')

    Jump('loc_1900')

    def _loc_18E5(): pass

    label('loc_18E5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_18EF',
    )

    Jump('loc_1900')

    def _loc_18EF(): pass

    label('loc_18EF')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_18F9',
    )

    Jump('loc_1900')

    def _loc_18F9(): pass

    label('loc_18F9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_1900',
    )

    def _loc_1900(): pass

    label('loc_1900')

    TalkEnd(0x00FE)

    Return()

# id: 0x000C offset: 0x1904
@scena.Code('func_0C_1904')
def func_0C_1904():
    MapClearFlags(0x10000000)
    EventBegin(0x00)
    ChrSetStatus(0x0003, 0x00, 30)
    OP_B5(0x0003, 0x00)
    OP_B5(0x0003, 0x01)
    OP_B5(0x0003, 0x02)
    OP_B5(0x0003, 0x03)
    OP_B5(0x0003, 0x04)
    OP_B5(0x0003, 0x05)
    EquipCmd(0x03, 0x005E)
    EquipCmd(0x03, 0x00F5)
    EquipCmd(0x03, 0x0113)
    EquipCmd(0x03, 0x025C, 0x00)
    EquipCmd(0x03, 0x026B, 0x01)
    EquipCmd(0x03, 0x025F, 0x02)
    EquipCmd(0x03, 0x0262, 0x02)
    AddCraft(0x0003, 0x00B4)
    AddCraft(0x0003, 0x00B5)
    AddSCraft(0x0003, 0x00F5)
    CameraMove(12040, 2000, 7430, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6E(262, 0)
    FormationAddMember(0x03, 0xFF)
    FormationAddMember(0x07, 0xFF)
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    ChrSetPos(0x0101, 11710, 2000, 7600, 0)
    ChrSetPos(0x0102, 12480, 2000, 8230, 0)
    ChrSetPos(0x0108, 8480, 0, -1270, 135)
    ChrSetPos(0x0104, 7240, -250, -7700, 135)
    ChrSetFlags(0x0104, 0x0080)

    @scena.Lambda('lambda_1A05')
    def lambda_1A05():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_1A05')

    DispatchAsync2(0x0101, 0x0001, lambda_1A05)

    @scena.Lambda('lambda_1A16')
    def lambda_1A16():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_1A16')

    DispatchAsync2(0x0102, 0x0001, lambda_1A16)

    @scena.Lambda('lambda_1A27')
    def lambda_1A27():
        ChrWalkTo(0x00FE, 11700, 0, 290, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1A27)

    @scena.Lambda('lambda_1A42')
    def lambda_1A42():
        ChrWalkTo(0x00FE, 12500, 0, 950, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1A42)

    @scena.Lambda('lambda_1A5D')
    def lambda_1A5D():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_1A5D')

    DispatchAsync2(0x0108, 0x0001, lambda_1A5D)

    CameraMove(10650, 0, 1690, 3000)

    ChrTalk(
        0x0108,
        (
            '#0080110001V#070F#5P哟，起得真早。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110002V#501F啊，早上好～金先生！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1AD2')
    def lambda_1AD2():
        ChrWalkTo(0x00FE, 9710, 0, -2100, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1AD2)

    @scena.Lambda('lambda_1AED')
    def lambda_1AED():
        ChrWalkTo(0x00FE, 9480, 0, -880, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_1AED)

    CameraMove(8570, 0, -1520, 2000)
    WaitForThreadExit(0x0102, 0x0002)

    ChrTalk(
        0x0102,
        (
            '#0020110003V#010F真是抱歉，\n',
            '让您特地来接我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110004V#070F没什么啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110005V不管怎么说，\n',
            '比赛之前还是要做好各种准备啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110006V最好把工房、武器店和\n',
            '百货店什么的都通通逛一遍。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110007V#006F这就是所谓的『有备无患』吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110008V#505F对了……\n',
            '奥利维尔那家伙怎么还没来？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    PlaySE(6, 0x00, 0x64)
    Sleep(200)

    ChrTalk(
        0x0104,
        (
            '#0040110009V#2P早上好啊～亲爱的各位㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1C87')
    def lambda_1C87():
        ChrTurnDirection(0x00FE, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_1C87)

    @scena.Lambda('lambda_1C95')
    def lambda_1C95():
        ChrTurnDirection(0x00FE, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1C95)

    @scena.Lambda('lambda_1CA3')
    def lambda_1CA3():
        ChrTurnDirection(0x00FE, 0x0104, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1CA3)

    ChrClearFlags(0x0104, 0x0080)
    ChrSetRGBAMask(0x0104, 255, 255, 255, 0, 0)

    @scena.Lambda('lambda_1CC1')
    def lambda_1CC1():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0104, 0x0002, lambda_1CC1)

    ChrWalkTo(0x0104, 7180, -250, -6350, 2000, 0x00)

    @scena.Lambda('lambda_1CE7')
    def lambda_1CE7():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_1CE7')

    DispatchAsync2(0x0108, 0x0001, lambda_1CE7)

    @scena.Lambda('lambda_1CF8')
    def lambda_1CF8():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_1CF8')

    DispatchAsync2(0x0101, 0x0001, lambda_1CF8)

    @scena.Lambda('lambda_1D09')
    def lambda_1D09():
        ChrTurnDirection(0x00FE, 0x0104, 0)
        Yield()

        Jump('lambda_1D09')

    DispatchAsync2(0x0102, 0x0001, lambda_1D09)

    @scena.Lambda('lambda_1D1A')
    def lambda_1D1A():
        ChrWalkTo(0x00FE, 8430, 0, -2470, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0104, 0x0001, lambda_1D1A)

    WaitForThreadExit(0x0104, 0x0001)

    ChrTalk(
        0x0104,
        (
            '#0040110010V#031F哈·哈·哈。\n',
            '如此清爽的早晨，\n',
            '给我们的初次上阵增色不少呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110011V#509F又是这样……\n',
            '老是算好时间突然出现人家面前……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110012V#010F早上好，奥利维尔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110013V#070F早上好。\n',
            '这样人员已经到齐了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110014V那就赶快出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110015V#000F我记得武术大会\n',
            '应该是从中午开始的吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110016V现在还很早，\n',
            '我们要怎样打发时间呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0108, 0xFF)
    ChrSetDirection(0x0108, 135, 400)

    ChrTalk(
        0x0108,
        (
            '#0080110017V#070F刚才说过了，\n',
            '我们最好去商店补充一下不足的装备。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110018V而且，为了让身体活动开，\n',
            '去城外街道上打打魔兽也不错。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrSetDirection(0x0104, 0, 400)

    ChrTalk(
        0x0104,
        (
            '#0040110019V#030F原来如此，就算是热身啦。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110020V#010F确实，很有必要在比赛之前\n',
            '找找团体战斗的感觉呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110021V以这样的阵容作战，还是第一次呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110022V#001F那就这样决定吧，我们出发吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110023V做好准备之后就去竞技场吧！\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    SetScenaFlags(ScenaFlag(0x00C3, 1, 0x619))
    OP_28(0x0047, 0x04, 0x02)
    OP_28(0x0047, 0x04, 0x04)
    OP_28(0x0047, 0x01, 0x0001)
    OP_28(0x0047, 0x01, 0x0002)
    EventEnd(0x00)

    Return()

# id: 0x000D offset: 0x2078
@scena.Code('func_0D_2078')
def func_0D_2078():
    MapClearFlags(0x10000000)
    EventBegin(0x00)
    CameraMove(7340, -250, -5730, 0)
    OP_67(0, 5960, -10000, 0)
    CameraSetDistance(3010, 0)
    ChrSetPos(0x0008, 4320, 0, 1700, 180)
    ChrTurnDirection(0x0008, 0x0101, 0)
    ChrClearFlags(0x0008, 0x0080)
    ChrSetPos(0x0101, 6490, -250, -5810, 0)
    ChrSetPos(0x0102, 7740, -250, -5800, 0)
    FadeIn(1000, 0)
    OP_0D()

    NpcTalk(
        0x0008,
        '男人的声音',
        (
            '#0270110452V#6P终于回来了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    NpcTalk(
        0x0008,
        '男人的声音',
        (
            '#0270110453V#6P真是让我好等啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(1000)

    @scena.Lambda('lambda_218A')
    def lambda_218A():
        ChrTurnDirection(0x00FE, 0x0008, 0)
        Yield()

        Jump('lambda_218A')

    DispatchAsync2(0x0101, 0x0001, lambda_218A)

    ChrTalk(
        0x0101,
        (
            '#0010110454V#501F这个声音……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_21BE')
    def lambda_21BE():
        CameraMove(4450, 0, 1130, 2000)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_21BE)

    @scena.Lambda('lambda_21D6')
    def lambda_21D6():
        ChrWalkTo(0x00FE, 4090, 0, -140, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_21D6)

    Sleep(300)

    @scena.Lambda('lambda_21F6')
    def lambda_21F6():
        ChrWalkTo(0x00FE, 5210, 0, -350, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_21F6)

    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020110455V#010F#6P很久不见了，奈尔先生。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110456V#008F哇～是奈尔啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010110457V怎么，是特地来拜访我们的吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270110458V#141F嗯。就是特地来拜访你们的。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110459V据对武术大会进行取材的同事说，\n',
            '有两位年轻有为的少年参加了比赛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110460V听说了详细情况之后，\n',
            '不管怎么想都觉得是你们啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110461V所以我才来到王都这里，\n',
            '在酒店门口等着你们回来。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110462V#506F哈哈……看来你还是老样子，\n',
            '无论什么时候消息都是那么的灵通。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110463V#010F#6P虽然很高兴您能来看我们……\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110464V不过奈尔先生，\n',
            '恐怕您是有事才来这里的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110465V#006F啊，又是在寻找新闻素材吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270110466V#145F啊～真是可叹啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110467V这次特地抛开利益得失来维持我们的友情，\n',
            '你们就这么不明白大哥我的苦心吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110468V#509F说谎～……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110469V#019F#6P而且，说自己是大哥，\n',
            '年纪也似乎相差得太远了吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270110470V#144F哼，别提啦。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110471V不说这个啦，\n',
            '我们赶快出去吃饭吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110472V#014F#6P又这么突然……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110473V#001F可以是可以，\n',
            '不过是谁请客你应该清楚吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0270110474V#145F呜……算了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110475V#141F那么我们就去杂志社附近的酒馆吧。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0270110476V就在那里吃晚饭好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_28(0x0047, 0x01, 0x0400)
    OP_20(0x000005DC)
    FadeOut(1500, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4152._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000E offset: 0x26BD
@scena.Code('func_0E_26BD')
def func_0E_26BD():
    EventBegin(0x00)
    CameraMove(6960, 0, 4490, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(287, 0)
    FormationAddMember(0x03, 0xFF)
    FormationAddMember(0x07, 0xFF)
    ChrSetPos(0x0108, 8480, 0, -1270, 90)
    ChrSetPos(0x0104, 8430, 0, -2470, 45)
    ChrSetPos(0x0101, 9710, 0, -2100, 270)
    ChrSetPos(0x0102, 9480, 0, -880, 270)
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)
    FadeIn(2000, 0)
    CameraMove(8570, 0, -1520, 3000)

    ChrTalk(
        0x0104,
        (
            '#0040110616V#031F呵呵，大家都到齐了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110617V我们赶快出发吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080110618V#070F和昨天一样，比赛是从中午开始，\n',
            '上午我们可以自由行动。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110619V在商店里整理装备也好，\n',
            '去街道上打魔兽活动一下筋骨也好。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010110620V#006F啊，如果是这样的话，\n',
            '我这里有一个非常好的地方呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔向金和奥利维尔说明了\n',
            '从渡鸦帮成员那里得到地下水路钥匙的事情。',
            (TxtCtl.SetColor, 0x0),
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0108,
        (
            '#0080110621V#073F哦，还真是有意思啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080110622V有比较强的魔兽的话，\n',
            '正好可以用来当练习的对手。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040110623V#035F美丽高贵的王都地下\n',
            '布满了古代的地下水路……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040110624V呵呵，真是浪漫啊。\n',
            '这不是在刺激我的冒险之心嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020110625V#010F如果有空的话，\n',
            '中午以前去看看吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020110626V地下水路的入口处就在\n',
            '西街区住宅区外围的城墙上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00C4, 1, 0x621))
    OP_28(0x0048, 0x04, 0x02)
    OP_28(0x0048, 0x04, 0x04)
    OP_28(0x0048, 0x01, 0x0001)
    OP_28(0x0048, 0x01, 0x0002)
    EventEnd(0x00)

    Return()

# id: 0x000F offset: 0x2A9B
@scena.Code('func_0F_2A9B')
def func_0F_2A9B():
    EventBegin(0x00)
    CameraMove(6960, 0, 4490, 0)
    OP_67(0, 8000, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315000, 0)
    OP_6E(287, 0)
    FormationAddMember(0x03, 0xFF)
    FormationAddMember(0x07, 0xFF)
    ChrSetPos(0x0108, 8480, 0, -1270, 90)
    ChrSetPos(0x0104, 8430, 0, -2470, 45)
    ChrSetPos(0x0101, 9710, 0, -2100, 270)
    ChrSetPos(0x0102, 9480, 0, -880, 270)
    FadeOut(0, 0, -1)
    OP_20(0x00000000)
    ChrSetStatus(0x0000, 0xFE, 0)
    ChrSetStatus(0x0001, 0xFE, 0)
    ChrSetStatus(0x0002, 0xFE, 0)
    ChrSetStatus(0x0003, 0xFE, 0)
    ChrSetStatus(0x0004, 0xFE, 0)
    ChrSetStatus(0x0005, 0xFE, 0)
    ChrSetStatus(0x0006, 0xFE, 0)
    ChrSetStatus(0x0007, 0xFE, 0)

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0xE),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_1E()
    FadeIn(2000, 0)
    CameraMove(8570, 0, -1520, 3000)

    ChrTalk(
        0x0104,
        (
            '#0040111479V#034F昨天真是不走运啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040111480V要是回大使馆的时候装成喝醉的样子，\n',
            '就不会被那些士兵诘难了。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080111481V#070F据说，好像是针对恐怖活动的对策，\n',
            '强化夜间巡逻也是没办法的事啊。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111482V你们没事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111483V#019F嗯，昨天早早地就休息了，\n',
            '没有发生什么问题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111484V#506F而、而且我们还从艾南哥哥那里\n',
            '借到了好东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkSetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '艾丝蒂尔和约修亚向金和奥利维尔说明了\n',
            '从艾南那里借到另外一把地下水路钥匙的事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)

    ChrTalk(
        0x0108,
        (
            '#0080111485V#071F哦哦，这还真是帮大忙了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080111486V那个小哥，虽然还很年轻,\n',
            '不过考虑事情都很周到嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010111487V#006F这样的话，中午之前\n',
            '我们就去地下水路锻炼一下吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020111488V#010F另外一个入口就在竞技场的旁边。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0104,
        (
            '#0040111489V#035F呼，为了我的晚宴，\n',
            '就做一下最后的努力吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00C5, 7, 0x62F))
    OP_28(0x0049, 0x04, 0x02)
    OP_28(0x0049, 0x04, 0x04)
    OP_28(0x0049, 0x01, 0x0001)
    OP_28(0x0049, 0x01, 0x0002)
    EventEnd(0x00)

    Return()

# id: 0x0010 offset: 0x2EB2
@scena.Code('func_10_2EB2')
def func_10_2EB2():
    EventBegin(0x00)
    ChrSetPos(0x0009, 35140, 0, 114000, 0)
    CameraMove(35210, 0, 115000, 0)
    OP_67(0, 4890, -10000, 0)
    CameraSetDistance(1680, 0)
    OP_6C(320000, 0)
    OP_6E(509, 0)
    ChrSetRGBAMask(0x0101, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0102, 255, 255, 255, 0, 0)
    ChrSetRGBAMask(0x0108, 255, 255, 255, 0, 0)
    ChrClearFlags(0x0009, 0x0080)
    ChrSetPos(0x0101, 35130, 0, 107040, 180)
    ChrSetPos(0x0102, 35130, 0, 107040, 180)
    ChrSetPos(0x0108, 35130, 0, 107040, 180)
    FadeIn(1000, 0)
    OP_0D()

    ChrTalk(
        0x0009,
        (
            '#0330130147V#843F#5P……………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330130148V#6P#5P那个时候的记忆……\n',
            '后来还是回想起来了一点……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330130149V#844F#5P模模糊糊的一点都不清晰……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_300C')
    def lambda_300C():
        CameraMove(35210, 0, 113750, 2000)

        ExitThread()

    DispatchAsync(0x0108, 0x0003, lambda_300C)

    @scena.Lambda('lambda_3024')
    def lambda_3024():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_3024)

    @scena.Lambda('lambda_3036')
    def lambda_3036():
        ChrWalkTo(0x00FE, 34750, 0, 112320, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3036)

    Sleep(600)

    @scena.Lambda('lambda_3056')
    def lambda_3056():
        ChrWalkTo(0x00FE, 35750, 0, 112210, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3056)

    @scena.Lambda('lambda_3071')
    def lambda_3071():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_3071)

    Sleep(600)

    @scena.Lambda('lambda_3088')
    def lambda_3088():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 255, 500)

        ExitThread()

    DispatchAsync(0x0108, 0x0002, lambda_3088)

    @scena.Lambda('lambda_309A')
    def lambda_309A():
        ChrWalkTo(0x00FE, 35160, 0, 111080, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_309A)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#0010130150V#501F啊，克鲁茨大哥……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020130151V#010F太好了，您在这里啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0108, 400)

    ChrTalk(
        0x0009,
        (
            '#0330130152V#840F咦……\n',
            '是艾丝蒂尔和约修亚啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330130153V金大哥也在，到底怎么回事了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130154V#070F我们几个昨晚到王城里参加了晚宴的\n',
            '这件事情你应该知道吧？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130155V在那时，这两位新来的游击士\n',
            '接受了一个非常重大的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330130156V#4P#842F非常重大的委托……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130157V#010F我们给克鲁茨大哥您说明一下情况吧。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '说明了至今为止发生的事情和女王的委托。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x0009,
        (
            '#0330130158V#4P#842F…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330130159V#844F……这是……真的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130160V#006F当然是了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130161V因此我们也需要克鲁茨大哥来帮忙。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330130162V#4P#842F不……我不是说这个。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330130163V女王陛下的委托\n',
            '的确让我深感震惊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_20(0x000005DC)

    ChrTalk(
        0x0009,
        (
            '#0330130164V#4P#844F但是，理查德上校\n',
            '得到的那个黑色导力器\n',
            '真的……存在吗……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_21()
    PlayBGM(81)

    ChrTalk(
        0x0101,
        (
            '#0010130165V#505F……克鲁茨大哥？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130166V你、你怎么了？\n',
            '为什么脸都发青了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330130167V#4P#847F#20A呜呜呜……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0009, 30, 0, 1000, 3000)
    ChrSetFlags(0x0009, 0x0020)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0009, 4)

    @scena.Lambda('lambda_34C0')
    def lambda_34C0():
        OP_99(0x00FE, 0x00, 0x03, 1000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_34C0)

    Sleep(500)

    ChrTalk(
        0x0009,
        (
            '#0330130168V#4P#847F#10A#3S啊啊啊啊啊啊啊啊……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    OP_9E(0x0009, 30, 0, 1000, 4000)

    @scena.Lambda('lambda_351D')
    def lambda_351D():
        OP_9E(0x00FE, 20, 0, 1000, 6000)
        Yield()

        Jump('lambda_351D')

    DispatchAsync2(0x0009, 0x0001, lambda_351D)

    Sleep(800)

    ChrTalk(
        0x0009,
        (
            '#0330130169V#4P#847F#5S哦啊啊啊啊啊啊！',
            TxtCtl.Enter,
        ),
    )

    OP_7C(0, 200, 3000, 100)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130170V#580F哇啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130171V#012F这、这是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130172V#072F呼……你们让开一下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_35E8')
    def lambda_35E8():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_35E8)

    ChrTurnDirection(0x0101, 0x0108, 400)

    ChrTalk(
        0x0101,
        (
            '#0010130173V#004F咦……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_361A')
    def lambda_361A():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_361A')

    DispatchAsync2(0x0102, 0x0001, lambda_361A)

    @scena.Lambda('lambda_362B')
    def lambda_362B():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_362B')

    DispatchAsync2(0x0101, 0x0001, lambda_362B)

    @scena.Lambda('lambda_363C')
    def lambda_363C():
        ChrMoveTo(0x00FE, 33810, 0, 111520, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_363C)

    @scena.Lambda('lambda_3657')
    def lambda_3657():
        ChrMoveTo(0x00FE, 36340, 0, 111380, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_3657)

    Sleep(300)

    ChrWalkTo(0x0108, 35020, 0, 112600, 2000, 0x00)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    Sleep(500)

    ChrTalk(
        0x0108,
        (
            '#0080130174V#074F嘿咿咿唔唔唔唔唔唔……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)
    ChrSetChipByIndex(0x0108, 2)
    OP_0D()

    ChrTalk(
        0x0108,
        (
            '#0080130175V#076F#20A#3S哈～……',
            0x5,
            TxtCtl.Enter,
        ),
    )

    @scena.Lambda('lambda_36F6')
    def lambda_36F6():
        OP_99(0x00FE, 0x00, 0x03, 1000)
        Yield()

        Jump('lambda_36F6')

    DispatchAsync2(0x0108, 0x0001, lambda_36F6)

    CameraSetDistance(1600, 3000)
    TerminateThread(0x0108, 0xFF)

    ExecExpressionWithValue(
        0x0108,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0108, 3)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0009, 5)
    TerminateThread(0x0009, 0xFF)
    ChrSetFlags(0x0009, 0x0800)

    @scena.Lambda('lambda_373F')
    def lambda_373F():
        CameraMove(35130, 0, 115000, 500)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_373F)

    @scena.Lambda('lambda_3757')
    def lambda_3757():
        ChrMoveTo(0x00FE, 35130, 0, 115500, 10000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_3757)

    @scena.Lambda('lambda_3772')
    def lambda_3772():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000258, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_3772)

    @scena.Lambda('lambda_3788')
    def lambda_3788():
        OP_94(0x01, 0x00FE, 0x00B4, 0x00000258, 0x00000BB8, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3788)

    ChrTalk(
        0x0108,
        (
            '#0080130176V#077F#3P#10A#5S喝！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    PlaySE(507, 0x00, 0x64)
    PlaySE(535, 0x00, 0x64)
    WaitForThreadExit(0x0009, 0x0001)
    PlaySE(554, 0x00, 0x64)

    ChrTalk(
        0x0009,
        (
            '#0330130177V#847F#2P#10A#3S啊！',
            0x5,
            TxtCtl.Enter,
        ),
    )

    CameraSetDistance(1700, 0)
    CameraSetDistance(1670, 100)

    ExecExpressionWithValue(
        0x0009,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0009, 4)

    @scena.Lambda('lambda_381E')
    def lambda_381E():
        OP_99(0x00FE, 0x00, 0x03, 2000)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_381E)

    Sleep(2000)

    ChrSetFlags(0x0009, 0x0800)
    OP_62(0x0101, 0x00000000, 2000, 0x28, 0x2B, 0x00000064, 0x03)

    ChrTalk(
        0x0101,
        (
            '#0010130178V#004F#5P刚、刚才那是……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130179V虽然没有接触到身体，\n',
            '但却听到了啪的一声呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130180V#012F刚才那是气功……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130181V虽然没有接触到身体，\n',
            '但可以对肉体直接作用……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130182V#074F#5P因为事出突然，\n',
            '所以只有采取这种粗鲁的方式。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Fade(500)

    ExecExpressionWithValue(
        0x0108,
        0x08,
        (
            (Expr.PushLong, 0x0),
            Expr.Nop,
            Expr.Return,
        ),
    )

    ChrSetChipByIndex(0x0108, 65535)
    OP_0D()

    @scena.Lambda('lambda_396A')
    def lambda_396A():
        ChrMoveTo(0x00FE, 34130, 0, 114720, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_396A)

    Sleep(300)

    @scena.Lambda('lambda_398A')
    def lambda_398A():
        CameraMove(35130, 0, 115500, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_398A)

    Sleep(300)

    ChrSetFlags(0x0101, 0x0004)

    @scena.Lambda('lambda_39AC')
    def lambda_39AC():
        ChrWalkTo(0x00FE, 34980, 0, 113450, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_39AC)

    Sleep(200)

    @scena.Lambda('lambda_39CC')
    def lambda_39CC():
        ChrWalkTo(0x00FE, 35840, 0, 113580, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_39CC)

    WaitForThreadExit(0x0108, 0x0001)
    ChrSetDirection(0x0108, 90, 400)
    WaitForThreadExit(0x0101, 0x0001)
    ChrSetDirection(0x0101, 0, 400)
    ChrClearFlags(0x0101, 0x0004)

    ChrTalk(
        0x0108,
        (
            '#0080130183V#070F感觉如何？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330130184V#4P#843F是啊……\n',
            '对不起，已经没事了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_99(0x0009, 0x03, 0x00, 1000)
    Sleep(200)

    ChrSetChipByIndex(0x0009, 1)

    ChrTalk(
        0x0009,
        (
            '#0330130185V#4P#844F虽然不是全部……\n',
            '但终于回想起来了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330130186V如果没有这一震，\n',
            '身体就会不听使唤了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130187V#505F回、回想起来了什么……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330130188V#845F之前也说过的吧？\n',
            '三个月前的那起事故……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130189V#012F克鲁茨大哥在任务中失去记忆的事。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330130190V#4P#844F是啊……\n',
            '那时有一个人委托我调查\n',
            '黑衣人一伙的事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330130191V#843F然后我夺取了那伙人运送的\n',
            '一个可疑物品。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330130192V#842F那就是黑色导力器。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010121285V#005F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130194V#012F那个委托您的人难道是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330130195V#4P#842F是啊……\n',
            '就是你们的父亲卡西乌斯先生。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330130196V我急忙把那个导力器\n',
            '用小包裹装着寄给了卡西乌斯先生……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330130197V#845F到这里为止，之后的我就想不起来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130198V#580F这、这么说！\n',
            '寄小包裹的『Ｋ』就是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330130199V#4P#843F啊……就是我。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330130200V我记得还写了让拉赛尔博士\n',
            '分析这东西的讯息。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330130201V#840F哦，那个小包裹\n',
            '是你们收到的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130202V#012F克鲁茨大哥……\n',
            '那之后的记忆呢？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130203V把小包裹寄给父亲之后，\n',
            '你又遇到了什么事情呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330130204V#4P#844F啊……离开了飞艇坪后，\n',
            '好像听到有人在背后叫我……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330130205V然后……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330130206V#843F………………………………\n',
            '………………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330130207V#847F不行啊，记忆模模糊糊的，\n',
            '完全记不起来啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130208V#072F不要太勉强了，记不起来就算了。\n',
            '　',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130209V这样只会增加身体的负担。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330130210V#4P#845F……啊，我明白了……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330130211V总之，那时的事情\n',
            '我就只能记起这么多了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130212V#003F可是……\n',
            '到底是谁做出的这种事情……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130213V果然和那些特务兵有所关系吗？\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020130214V#015F有这种可能性……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130215V#013F让阿加特兄深受煎熬的\n',
            '神经性毒药也是这样……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130216V看来是开发了特殊的药品\n',
            '然后以此来作为测试。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020130217V#012F也许是使用了可以让记忆超负荷的药品。\n',
            '　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130218V#007F让、让人有些毛骨悚然呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130219V#002F这么说来，空贼的头目\n',
            '和戴尔蒙市长也是这样的了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010130220V我们也必须小心才行……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330130221V#4P#840F抱歉……\n',
            '关键的事情还没有说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330130222V陛下委托的事情我知道了，\n',
            '无论如何我也要尽一份力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010130223V#505F可、可是……\n',
            '克鲁茨大哥你的身体行吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0330130224V#4P#841F啊，取回了记忆，\n',
            '感觉轻松了不少啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0330130225V就算是为了报这个仇也好，\n',
            '请务必让我尽一份力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080130226V#070F这样的状况来看已经没问题了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080130227V作战会议即将开始了，\n',
            '还请你先回协会稍等一会吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrClearFlags(0x0009, 0x0020)

    @scena.Lambda('lambda_4395')
    def lambda_4395():
        ChrTurnDirection(0x00FE, 0x0108, 0)
        Yield()

        Jump('lambda_4395')

    DispatchAsync2(0x0009, 0x0001, lambda_4395)

    ChrTalk(
        0x0009,
        (
            '#0330130228V#840F我明白了……多谢您刚才的相助！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0009, 0xFF)

    @scena.Lambda('lambda_43DF')
    def lambda_43DF():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_43DF')

    DispatchAsync2(0x0101, 0x0001, lambda_43DF)

    @scena.Lambda('lambda_43F0')
    def lambda_43F0():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_43F0')

    DispatchAsync2(0x0102, 0x0001, lambda_43F0)

    @scena.Lambda('lambda_4401')
    def lambda_4401():
        ChrTurnDirection(0x00FE, 0x0009, 0)
        Yield()

        Jump('lambda_4401')

    DispatchAsync2(0x0108, 0x0001, lambda_4401)

    @scena.Lambda('lambda_4412')
    def lambda_4412():
        CameraMove(34710, 0, 112900, 2000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_4412)

    ChrWalkTo(0x0009, 34310, 0, 113450, 3000, 0x00)
    ChrWalkTo(0x0009, 35090, 0, 107160, 3000, 0x00)

    @scena.Lambda('lambda_4452')
    def lambda_4452():
        ChrSetRGBAMask(0x00FE, 255, 255, 255, 0, 500)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_4452)

    ChrSetFlags(0x0009, 0x0004)
    ChrWalkTo(0x0009, 35010, 0, 105270, 3000, 0x00)
    ChrSetFlags(0x0009, 0x0080)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    TerminateThread(0x0108, 0xFF)
    OP_28(0x004B, 0x01, 0x0080)

    If(
        (
            (Expr.Eval, "OP_29(0x004B, 0x01, 0x0010)"),
            (Expr.Eval, "OP_29(0x004B, 0x01, 0x0020)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x004B, 0x01, 0x0040)"),
            Expr.Nez64,
            (Expr.Eval, "OP_29(0x004B, 0x01, 0x0080)"),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_44B7',
    )

    OP_28(0x004B, 0x01, 0x0100)

    def _loc_44B7(): pass

    label('loc_44B7')

    OP_20(0x000003E8)
    FadeOut(1000, 0, -1)
    OP_0D()
    CameraMove(34980, 0, 113450, 0)
    OP_67(0, 6150, -10000, 0)
    CameraSetDistance(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    ChrSetPos(0x0101, 34980, 0, 113450, 180)
    ChrSetPos(0x0102, 34980, 0, 113450, 180)
    ChrSetPos(0x0108, 34980, 0, 113450, 180)
    FadeIn(1000, 0)
    PlayBGM(14)
    EventEnd(0x00)

    Return()

# id: 0x0011 offset: 0x4545
@scena.Code('func_11_4545')
def func_11_4545():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　　　　　事务室　　　　　　　\n',
            '※工作人员以外禁止进入。',
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
