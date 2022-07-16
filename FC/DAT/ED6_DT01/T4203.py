import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T4203_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4203   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '士兵丹'),
    TXT(0x02, '士兵阿尔兹'),
    TXT(0x03, '杜南公爵'),
    TXT(0x04, '管家菲利普'),
    TXT(0x05, '特务兵'),
    TXT(0x06, '特务兵'),
    TXT(0x07, '卡露娜'),
    TXT(0x08, '亚妮拉丝'),
    TXT(0x09, '库拉茨'),
    TXT(0x0A, '克鲁茨'),
    TXT(0x0B, '尤莉亚中尉'),
    TXT(0x0C, '亲卫队员'),
    TXT(0x0D, '亲卫队员'),
    TXT(0x0E, '亲卫队员'),
    TXT(0x0F, '亲卫队员'),
    TXT(0x10, '亲卫队员'),
    TXT(0x11, '亲卫队员'),
    TXT(0x12, '亲卫队员'),
    TXT(0x13, '亲卫队员'),
    TXT(0x14, '卡西乌斯'),
    TXT(0x15, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4203.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x40DA
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
        ('ED6_DT07/CH01300._CH', 'ED6_DT07/CH01300P._CP'),
        ('ED6_DT07/CH02140._CH', 'ED6_DT07/CH02140P._CP'),
        ('ED6_DT07/CH02470._CH', 'ED6_DT07/CH02470P._CP'),
        ('ED6_DT07/CH01330._CH', 'ED6_DT07/CH01330P._CP'),
        ('ED6_DT07/CH00401._CH', 'ED6_DT07/CH00401P._CP'),
        ('ED6_DT07/CH00421._CH', 'ED6_DT07/CH00421P._CP'),
        ('ED6_DT07/CH00391._CH', 'ED6_DT07/CH00391P._CP'),
        ('ED6_DT07/CH00411._CH', 'ED6_DT07/CH00411P._CP'),
        ('ED6_DT07/CH02090._CH', 'ED6_DT07/CH02090P._CP'),
        ('ED6_DT07/CH00321._CH', 'ED6_DT07/CH00321P._CP'),
        ('ED6_DT07/CH02000._CH', 'ED6_DT07/CH02000P._CP'),
    ]

# id: 0x10002 offset: 0x102
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -790,
            z                   = 0,
            y                   = 41980,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = 950,
            z                   = 0,
            y                   = 41980,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
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
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0002,
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
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
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
            dword_10            = 7,
            chipIndex           = 7,
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
            dword_10            = 8,
            chipIndex           = 8,
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
    )

# id: 0x10003 offset: 0x382
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x382
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = -5630,
            y           = -1000,
            z           = 30090,
            range       = 6050,
            dword_10    = 0x000003E8,
            dword_14    = 0x000069BE,
            dword_18    = 0x00000000,
            dword_1C    = 0x00000007,
        ),
    )

# id: 0x10005 offset: 0x3A2
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x3A2
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_3B0',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x0008)

    def _loc_3B0(): pass

    label('loc_3B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 3, 0x3FB)),
            Expr.Return,
        ),
        'loc_3BE',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 3, 0x3FB))
    Event(0, 0x0009)

    def _loc_3BE(): pass

    label('loc_3BE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 4, 0x3FC)),
            Expr.Return,
        ),
        'loc_3CC',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    Event(0, 0x000A)

    def _loc_3CC(): pass

    label('loc_3CC')

    Switch(
        (
            (Expr.PushValueByIndex, 0x0),
            Expr.Return,
        ),
        (0x00000066, 'loc_3DC'),
        (0x00000065, 'loc_3DC'),
        (-1, 'loc_3F2'),
    )

    def _loc_3DC(): pass

    label('loc_3DC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 3, 0x60B)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 1, 0x609)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3EF',
    )

    SetScenaFlags(ScenaFlag(0x00C1, 3, 0x60B))
    Event(0, 0x0006)

    def _loc_3EF(): pass

    label('loc_3EF')

    Jump('loc_3F2')

    def _loc_3F2(): pass

    label('loc_3F2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_3FC',
    )

    Jump('loc_493')

    def _loc_3FC(): pass

    label('loc_3FC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_43C',
    )

    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    SetChrPos(0x000C, -790, 0, 41980, 180)
    SetChrPos(0x000D, 950, 0, 41980, 180)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)

    Jump('loc_493')

    def _loc_43C(): pass

    label('loc_43C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_446',
    )

    Jump('loc_493')

    def _loc_446(): pass

    label('loc_446')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_450',
    )

    Jump('loc_493')

    def _loc_450(): pass

    label('loc_450')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_45A',
    )

    Jump('loc_493')

    def _loc_45A(): pass

    label('loc_45A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_464',
    )

    Jump('loc_493')

    def _loc_464(): pass

    label('loc_464')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_46E',
    )

    Jump('loc_493')

    def _loc_46E(): pass

    label('loc_46E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_478',
    )

    Jump('loc_493')

    def _loc_478(): pass

    label('loc_478')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_482',
    )

    Jump('loc_493')

    def _loc_482(): pass

    label('loc_482')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_48C',
    )

    Jump('loc_493')

    def _loc_48C(): pass

    label('loc_48C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_493',
    )

    def _loc_493(): pass

    label('loc_493')

    Return()

# id: 0x0001 offset: 0x494
@scena.Code('Init')
def Init():
    OP_16(0x02, 4000, -128000, -112000, 196704)
    OP_72(0x0000, 0x0010)
    OP_6F(0x0000, 450)

    Return()

# id: 0x0002 offset: 0x4B3
@scena.Code('ReInit')
def ReInit():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '格兰赛尔城完全封锁。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '上面下了命令，\n',
            '无论是谁也不能通行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0003 offset: 0x4FD
@scena.Code('func_03_4FD')
def func_03_4FD():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '你们是在武术大会\n',
            '取得优胜的游击士吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '晚宴已经结束了。\n',
            '快回游击士协会去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x55A
@scena.Code('func_04_55A')
def func_04_55A():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_679',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_5D9',
    )

    ChrTalk(
        0x00FE,
        (
            '尤莉亚中尉是恐怖分子的说法\n',
            '让我难以置信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而理查德上校\n',
            '是政变的主谋这一点\n',
            '同样让我难以置信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_676')

    def _loc_5D9(): pass

    label('loc_5D9')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '尤莉亚中尉是恐怖分子的说法\n',
            '让我难以置信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而理查德上校\n',
            '是政变的主谋这一点\n',
            '同样让我难以置信……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那么优秀的一个人，\n',
            '怎么会做出这种事来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_676(): pass

    label('loc_676')

    Jump('loc_B84')

    def _loc_679(): pass

    label('loc_679')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_683',
    )

    Jump('loc_B84')

    def _loc_683(): pass

    label('loc_683')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_6B0',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，\n',
            '在王城里面好好参观了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B84')

    def _loc_6B0(): pass

    label('loc_6B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_70E',
    )

    ChrTalk(
        0x00FE,
        (
            '欢迎来到\n',
            '女王陛下的格兰赛尔城！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们从这里进去，\n',
            '就会有接待人员前来迎接。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B84')

    def _loc_70E(): pass

    label('loc_70E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_778',
    )

    ChrTalk(
        0x00FE,
        (
            '啊～\n',
            '不知道尤莉亚中尉现在怎么样了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '每天向中尉打招呼\n',
            '可是我日常工作当中的一大乐趣啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B84')

    def _loc_778(): pass

    label('loc_778')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_85D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_7E1',
    )

    ChrTalk(
        0x00FE,
        (
            '从今天开始\n',
            '全城的警戒都加强了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这项工作似乎是由\n',
            '上校的副官凯诺娜上尉负责的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_85A')

    def _loc_7E1(): pass

    label('loc_7E1')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '从今天开始\n',
            '全城的警戒都加强了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这项工作似乎是由\n',
            '上校的副官凯诺娜上尉负责的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '理查德上校果然相当忙呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_85A(): pass

    label('loc_85A')

    Jump('loc_B84')

    def _loc_85D(): pass

    label('loc_85D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_8CC',
    )

    ChrTalk(
        0x00FE,
        (
            '特务部队的那群人\n',
            '在大会中连续获胜啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '比起去参加比赛，\n',
            '我倒希望他们\n',
            '快点去搜捕亲卫队的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B84')

    def _loc_8CC(): pass

    label('loc_8CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_9C9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_946',
    )

    ChrTalk(
        0x00FE,
        (
            '女王陛下生病后，\n',
            '就几乎很少能在城外\n',
            '看见理查德上校。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '情报部的本部好像转移到了王城内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_9C6')

    def _loc_946(): pass

    label('loc_946')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '理查德上校\n',
            '好像非常忙碌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女王陛下生病后，\n',
            '几乎很少能在城外看见他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说起来，\n',
            '情报部的本部好像转移到了王城内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_9C6(): pass

    label('loc_9C6')

    Jump('loc_B84')

    def _loc_9C9(): pass

    label('loc_9C9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_A73',
    )

    ChrTalk(
        0x00FE,
        (
            '说起理查德上校，\n',
            '我当然是很尊敬他啦。\n',
            '可是那些情报部的黑衣家伙们啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我承认他们有实力，\n',
            '可他们给人的感觉很不舒服，\n',
            '在军队里面关于他们的流言也不少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B84')

    def _loc_A73(): pass

    label('loc_A73')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_ADE',
    )

    ChrTalk(
        0x00FE,
        (
            '理查德上校\n',
            '的确是个优秀的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为在王国军中颇具人气，\n',
            '有许多人都慕名\n',
            '转到情报部去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B84')

    def _loc_ADE(): pass

    label('loc_ADE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_B84',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 3, 0x60B)),
            Expr.Return,
        ),
        'loc_B49',
    )

    ChrTalk(
        0x00FE,
        (
            '虽然不能进城参观，\n',
            '也不要这么灰心丧气嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '格兰赛尔的大街上\n',
            '还有很多观光胜地呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_B84')

    def _loc_B49(): pass

    label('loc_B49')

    ChrTalk(
        0x00FE,
        (
            '请你们站住。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很抱歉，\n',
            '王城现在禁止无关人等进入。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_B84(): pass

    label('loc_B84')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0xB88
@scena.Code('func_05_B88')
def func_05_B88():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CD, 3, 0x66B)),
            Expr.Return,
        ),
        'loc_C08',
    )

    ChrTalk(
        0x00FE,
        (
            '这次政变竟然是由\n',
            '城内的情报部发起的，\n',
            '的确让我感到震惊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过庆典总算能够平安无事地进行，\n',
            '真的是太好了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10BE')

    def _loc_C08(): pass

    label('loc_C08')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00CB, 2, 0x65A)),
            Expr.Return,
        ),
        'loc_C12',
    )

    Jump('loc_10BE')

    def _loc_C12(): pass

    label('loc_C12')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C9, 1, 0x649)),
            Expr.Return,
        ),
        'loc_C7F',
    )

    ChrTalk(
        0x00FE,
        (
            '你们好啊，\n',
            '晚宴怎么样啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '宫廷料理什么的，\n',
            '我只在执行警卫时见过，\n',
            '从来都没机会品尝过呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10BE')

    def _loc_C7F(): pass

    label('loc_C7F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Return,
        ),
        'loc_CA9',
    )

    ChrTalk(
        0x00FE,
        (
            '那么，祝各位晚上玩得愉快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10BE')

    def _loc_CA9(): pass

    label('loc_CA9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C5, 7, 0x62F)),
            Expr.Return,
        ),
        'loc_D0D',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才，\n',
            '宫廷料理的材料都已经运到城内来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '大概那就是\n',
            '用来烹制今晚晚宴的食材吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10BE')

    def _loc_D0D(): pass

    label('loc_D0D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 6, 0x626)),
            Expr.Return,
        ),
        'loc_D69',
    )

    ChrTalk(
        0x00FE,
        (
            '从今晚开始\n',
            '必须要在市内巡逻。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为恐怖分子还未抓到，\n',
            '要严加防范才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10BE')

    def _loc_D69(): pass

    label('loc_D69')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C4, 1, 0x621)),
            Expr.Return,
        ),
        'loc_DDE',
    )

    ChrTalk(
        0x00FE,
        (
            '唉……\n',
            '关于女王陛下病情的详细情况，\n',
            '我们也不太了解。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '的确感觉有些不安呢，\n',
            '也不知道到底会怎么样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10BE')

    def _loc_DDE(): pass

    label('loc_DDE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 6, 0x61E)),
            Expr.Return,
        ),
        'loc_E3E',
    )

    ChrTalk(
        0x00FE,
        (
            '大会正式赛第一回合\n',
            '好像已经结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '代表王国警备队出场的\n',
            '那些人怎么样了呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10BE')

    def _loc_E3E(): pass

    label('loc_E3E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C3, 1, 0x619)),
            Expr.Return,
        ),
        'loc_F4E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_EB4',
    )

    ChrTalk(
        0x00FE,
        (
            '杜南公爵\n',
            '就算在王城里也很招人讨厌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉……\n',
            '要是理查德上校不在的话，\n',
            '不知道会变成什么样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_F4B')

    def _loc_EB4(): pass

    label('loc_EB4')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '杜南公爵\n',
            '就算在王城里也很招人讨厌。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为无论是谁，\n',
            '都只看到过他在吃、睡、玩。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唉……\n',
            '要是理查德上校不在的话，\n',
            '不知道会变成什么样子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_F4B(): pass

    label('loc_F4B')

    Jump('loc_10BE')

    def _loc_F4E(): pass

    label('loc_F4E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C2, 0, 0x610)),
            Expr.Return,
        ),
        'loc_105A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_FCB',
    )

    ChrTalk(
        0x00FE,
        (
            '因为今年的武术大会是团体战，\n',
            '比赛场次比以往减少了一些呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正式赛和预选赛不一样，\n',
            '是在下午进行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1057')

    def _loc_FCB(): pass

    label('loc_FCB')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '武术大会的预选赛\n',
            '好像已经结束了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '今年因为是团体战，\n',
            '比赛场次比以往减少了一些呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正式赛和预选赛不一样，\n',
            '是在下午进行的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1057(): pass

    label('loc_1057')

    Jump('loc_10BE')

    def _loc_105A(): pass

    label('loc_105A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 0, 0x608)),
            Expr.Return,
        ),
        'loc_10BE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C1, 3, 0x60B)),
            Expr.Return,
        ),
        'loc_10A6',
    )

    ChrTalk(
        0x00FE,
        (
            '好不容易来一次王都，\n',
            '就请舒舒服服地享受观光的乐趣吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_10BE')

    def _loc_10A6(): pass

    label('loc_10A6')

    ChrTalk(
        0x00FE,
        (
            '现在不能进城参观。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_10BE(): pass

    label('loc_10BE')

    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x10C2
@scena.Code('func_06_10C2')
def func_06_10C2():
    EventBegin(0x00)
    OP_6C(30000, 0)

    @scena.Lambda('lambda_10D3')
    def lambda_10D3():
        CameraMove(-930, 750, 44710, 7000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_10D3)

    @scena.Lambda('lambda_10EB')
    def lambda_10EB():
        OP_67(0, 4250, -10000, 8000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_10EB)

    @scena.Lambda('lambda_1103')
    def lambda_1103():
        CameraSetDistance(11000, 10000)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_1103)

    @scena.Lambda('lambda_1113')
    def lambda_1113():
        OP_6C(0, 15000)

        ExitThread()

    DispatchAsync(0x0102, 0x0003, lambda_1113)

    Sleep(12000)

    SetChrPos(0x0101, -910, 0, 8880, 0)
    SetChrPos(0x0102, 2029, 0, 10110, 0)

    @scena.Lambda('lambda_114A')
    def lambda_114A():
        CameraMove(-290, 0, 32350, 5000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_114A)

    @scena.Lambda('lambda_1162')
    def lambda_1162():
        CameraSetDistance(7180, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1162)

    @scena.Lambda('lambda_1172')
    def lambda_1172():
        OP_6E(262, 5000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1172)

    @scena.Lambda('lambda_1182')
    def lambda_1182():
        ChrWalkTo(0x00FE, -670, 0, 18440, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1182)

    @scena.Lambda('lambda_119D')
    def lambda_119D():
        ChrWalkTo(0x00FE, 1310, 0, 18440, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_119D)

    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0101,
        (
            '#000F哇～……\n',
            '这就是格兰赛尔城啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100753V女王住的地方，\n',
            '果然又气派又漂亮呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#0020100754V#010F嗯……\n',
            '不过看起来不仅是漂亮，\n',
            '也十分地坚固呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100755V那个巨大的城门就是很好的例子了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F确实，\n',
            '不可能那么简单就能进得去。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100757V总之，\n',
            '只能先向那边的士兵们打听一下了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我们先暗中调查一下吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '……就像刚从乡下来，\n',
            '想进王城参观那样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100760V想借此机会拜见女王，\n',
            '哪怕看一眼也好。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '——这种设定不错吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#000F还是老样子，摆出一幅若无其事的表情，\n',
            '立刻就能说出想法来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100763V真是让人感叹啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 400)

    ChrTalk(
        0x0102,
        (
            '#010F这句话我就当成是夸奖收下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_13FF')
    def lambda_13FF():
        CameraMove(0, 250, 42590, 4000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_13FF)

    CameraSetDistance(5100, 4000)
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    SetChrPos(0x0101, -850, 0, 25330, 0)
    SetChrPos(0x0102, 1090, 0, 22700, 0)
    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#000F喂～你们好～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_147D')
    def lambda_147D():
        ChrTurnDirection(0x00FE, 0x0101, 0)
        Yield()

        Jump('lambda_147D')

    DispatchAsync2(0x0008, 0x0001, lambda_147D)

    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_14A5')
    def lambda_14A5():
        ChrTurnDirection(0x00FE, 0x0102, 0)
        Yield()

        Jump('lambda_14A5')

    DispatchAsync2(0x0009, 0x0001, lambda_14A5)

    @scena.Lambda('lambda_14B6')
    def lambda_14B6():
        ChrWalkTo(0x00FE, -850, 0, 37520, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_14B6)

    @scena.Lambda('lambda_14D1')
    def lambda_14D1():
        ChrWalkTo(0x00FE, 790, 0, 37520, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_14D1)

    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0008,
        (
            '哦，你们好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '欢迎来到格兰赛尔城。\n',
            '有什么事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我们是刚从洛连特\n',
            '来到王都参观的。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100769V借此机会，\n',
            '想进城里面参观一下……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '啊，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '很抱歉，\n',
            '格兰赛尔城是无关人员禁止入内的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '由于恐怖分子骚乱，\n',
            '检查更为严格了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过，抓到了恐怖分子之后，\n',
            '应该就允许参观了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F是这样啊……真可惜。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010100775V唉，难道想见女王陛下一面的梦想\n',
            '还是没办法实现吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '对了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '诞辰庆典那天，\n',
            '女王会照例在城的阳台上对市民致意，\n',
            '应该会有见面的机会的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过最近，\n',
            '陛下的身体状况不是很好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '例行的致意还会不会有呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎……！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F那个……\n',
            '女王陛下生病了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '是啊……\n',
            '大概是因为操劳过度……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '而且，因为自己十分信赖的亲卫队\n',
            '被当成恐怖事件嫌疑犯这件事，\n',
            '也受了相当大的打击吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '最近都没有出现在会见室，\n',
            '应该是在女王宫静养吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010100785V#000F是这样吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '真是的，亲卫队那些家伙们，\n',
            '对陛下的信赖反倒恩将仇报……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '平常我就不喜欢\n',
            '这些所谓的精英们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0008, 0xFF)
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '可、可是，\n',
            '尤莉亚中尉平时不是很亲切的吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '对我们这些普通的士兵，\n',
            '也亲自教剑术和行事方法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '说她是恐怖分子，\n',
            '我有点不太相信呢……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 800)

    ChrTalk(
        0x0008,
        (
            '这、这是肯定的啦！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '大概，她是因为部下的胡作非为\n',
            '而感到责任重大，所以才失踪了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '是啊……\n',
            '尤莉亚小姐真是可怜啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x10, 0x13, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#000F（看起来，这些人……）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '（只是因为尤莉亚小姐的关系，\n',
            '在嫉妒其他的队员呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（嗯，好像是这样呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0008,
        (
            '咳咳……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '总之，就是这个原因，\n',
            '格兰赛尔城禁止入内。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '抱歉，请回去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F唉，这样的话，\n',
            '也只好放弃了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F不过，稍微有点担心呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020100802V女王陛下的健康且不必说，\n',
            '政务方面不要紧吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '是啊……\n',
            '这个担心很有道理呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '虽然这样，\n',
            '还是有名义上的代理人的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F名义上的代理人？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哈哈。\n',
            '顾名思义，只是『名义上的』。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '那一位大人和政务\n',
            '还真是八竿子打不着啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0008, 400)

    ChrTalk(
        0x0009,
        (
            '喂喂，说话要小心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过确实，\n',
            '我也觉得公主更为适合呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0008, 0x0009, 400)

    ChrTalk(
        0x0008,
        (
            '看，你不也是这样想的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ClearChrFlags(0x000A, 0x0080)
    ClearChrFlags(0x000B, 0x0080)
    SetChrPos(0x000A, -370, 750, 48420, 180)
    SetChrPos(0x000B, 550, 750, 49230, 180)

    @scena.Lambda('lambda_1C9E')
    def lambda_1C9E():
        OP_67(0, 9500, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_1C9E)

    @scena.Lambda('lambda_1CB6')
    def lambda_1CB6():
        CameraSetDistance(3800, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_1CB6)

    @scena.Lambda('lambda_1CC6')
    def lambda_1CC6():
        OP_6C(0, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_1CC6)

    Sleep(100)

    @scena.Lambda('lambda_1CDB')
    def lambda_1CDB():
        ChrMoveTo(0x00FE, -2320, 0, 41990, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0002, lambda_1CDB)

    @scena.Lambda('lambda_1CF6')
    def lambda_1CF6():
        ChrMoveTo(0x00FE, 2050, 0, 42150, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0002, lambda_1CF6)

    CameraMove(-10, 750, 48050, 3000)

    @scena.Lambda('lambda_1D22')
    def lambda_1D22():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_1D22')

    DispatchAsync2(0x0101, 0x0001, lambda_1D22)

    @scena.Lambda('lambda_1D33')
    def lambda_1D33():
        ChrTurnDirection(0x00FE, 0x000A, 0)
        Yield()

        Jump('lambda_1D33')

    DispatchAsync2(0x0102, 0x0001, lambda_1D33)

    @scena.Lambda('lambda_1D44')
    def lambda_1D44():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_1D44')

    DispatchAsync2(0x0009, 0x0001, lambda_1D44)

    @scena.Lambda('lambda_1D55')
    def lambda_1D55():
        ChrTurnDirection(0x00FE, 0x000A, 400)
        Yield()

        Jump('lambda_1D55')

    DispatchAsync2(0x0008, 0x0001, lambda_1D55)

    SetChrPos(0x0101, -2130, 0, 39490, 0)
    SetChrPos(0x0102, -2130, 0, 37840, 0)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 120)
    Sleep(1000)

    Sleep(1000)

    @scena.Lambda('lambda_1DA0')
    def lambda_1DA0():
        ChrWalkTo(0x00FE, -360, 750, 44590, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1DA0)

    Sleep(500)

    @scena.Lambda('lambda_1DC0')
    def lambda_1DC0():
        ChrWalkTo(0x00FE, 630, 750, 44920, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_1DC0)

    CameraMove(0, 750, 44920, 2000)
    WaitForThreadExit(0x000A, 0x0001)
    ChrTurnDirection(0x000A, 0x000B, 400)

    ChrTalk(
        0x000A,
        (
            '#220F哼，这叫什么事啊！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '现在预选赛\n',
            '不是已经开始了吗！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '菲利普！\n',
            '都是因为你没有叫我！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x000B, 0x000A, 400)

    ChrTalk(
        0x000B,
        (
            '#720F实在是抱歉，阁下。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660100817V不过，这也是因为\n',
            '阁下不注意生活规律啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660100818V这几天连续大摆宴席，\n',
            '又是吃又是唱的大闹……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660100819V啤酒和油炸食品\n',
            '放在一起大量地吃，\n',
            '还彻夜看漫画杂志一直到早上……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0660100820V总是这样，\n',
            '睡过头也是理所当然的了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#220F闭嘴，菲利普！\n',
            '你的这些话我已经听够了！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0640100822V作为继任国王的我，\n',
            '有权力想干什么就干什么！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0641110001V哎呀，时间紧迫！\n',
            '赶快赶去王立竞技场！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_1FE8')
    def lambda_1FE8():
        ChrWalkTo(0x00FE, -270, 0, 28020, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_1FE8)

    Sleep(500)

    @scena.Lambda('lambda_2008')
    def lambda_2008():
        ChrWalkTo(0x00FE, 1070, 0, 27640, 3000, 0x00)

        ExitThread()

    DispatchAsync(0x000B, 0x0001, lambda_2008)

    OP_62(0x0101, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x14, 0x17, 0x000000FA, 0x01)
    PlaySE(49, 0x00, 0x64)
    CameraMove(-30, 0, 40870, 5000)

    @scena.Lambda('lambda_2062')
    def lambda_2062():
        ChrMoveTo(0x00FE, -790, 0, 41980, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2062)

    @scena.Lambda('lambda_207D')
    def lambda_207D():
        ChrMoveTo(0x00FE, 950, 0, 41980, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_207D)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0101, 0x0009, 400)

    ChrTalk(
        0x0101,
        (
            '#000F……哎…………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0101, 0)
    ChrWalkTo(0x0102, -610, 0, 38320, 2000, 0x00)
    ChrTurnDirection(0x0102, 0x0009, 400)

    ChrTalk(
        0x0102,
        (
            '#010F……我说，难道……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……我知道，不用再说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '刚才那位就是陛下的代理人，\n',
            '现在主理政务的公爵阁下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F我……\n',
            '我的头开始疼了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0009, 0xFF)
    TerminateThread(0x0008, 0xFF)
    ChrTurnDirection(0x0008, 0x0101, 400)

    ChrTalk(
        0x0009,
        (
            '总、总之不用担心，\n',
            '有个可靠的人在辅佐，所以没问题的啦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '多亏了那个人，\n',
            '至今还没出什么大乱子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)

    @scena.Lambda('lambda_21F9')
    def lambda_21F9():
        ChrTurnDirection(0x00FE, 0x0009, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_21F9)

    ChrTurnDirection(0x0102, 0x0009, 400)

    ChrTalk(
        0x0102,
        (
            '#010F可靠的辅佐人……吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '嘿嘿，就是王国军情报部\n',
            '一个叫『理查德上校』的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '可以说，他代替放荡的公爵阁下，\n',
            '一手处理政务呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0101, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0102, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    ChrTalk(
        0x0101,
        (
            '#000F（果、果然……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（比预想的还要更加深入地\n',
            '控制了国家的核心呢……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过，虽然不能进城参观，\n',
            '也不要这么灰心丧气嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '格兰赛尔的大街上\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0009, 0x0102, 400)

    ChrTalk(
        0x0009,
        (
            '好不容易来一次王都，\n',
            '就请舒舒服服地享受观光的乐趣吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，说的也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F感谢你们的好意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4103._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0007 offset: 0x23E8
@scena.Code('func_07_23E8')
def func_07_23E8():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x00C7, 0, 0x638)),
            (Expr.TestScenaFlags, ScenaFlag(0x00C6, 7, 0x637)),
            Expr.Ez,
            Expr.Or,
            Expr.Return,
        ),
        'loc_23F5',
    )

    Return()

    def _loc_23F5(): pass

    label('loc_23F5')

    EventBegin(0x00)

    @scena.Lambda('lambda_23FD')
    def lambda_23FD():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_23FD)

    @scena.Lambda('lambda_240B')
    def lambda_240B():
        ChrTurnDirection(0x00FE, 0x0108, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_240B)

    ChrTurnDirection(0x0108, 0x0101, 400)

    ChrTalk(
        0x0108,
        (
            '#070F哦，现在就进城去吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120002V晚宴结束之后\n',
            '要在城里的客房过夜，\n',
            '明天才能回到街上来哦。',
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
            TXT(0x00, '进入格兰赛尔城\n'),
            TXT(0x01, '等一会儿再来\n'),
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
        (0x00000000, 'loc_24E7'),
        (0x00000001, 'loc_2571'),
        (-1, 'loc_25B5'),
    )

    def _loc_24E7(): pass

    label('loc_24E7')

    ChrTalk(
        0x0108,
        (
            '#0080120004V#070F那么就把请帖\n',
            '给那边的门卫看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯～\n',
            '总觉得很紧张呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F没错，像这样被招待\n',
            '这种体验还真是难得呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25B5')

    def _loc_2571(): pass

    label('loc_2571')

    ChrTalk(
        0x0108,
        (
            '#0080120003V#070F知道了，一会儿再来吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveToRelative(0x0000, 0, 0, -1500, 3000, 0x00)
    Sleep(50)

    EventEnd(0x04)

    Return()

    def _loc_25B5(): pass

    label('loc_25B5')

    @scena.Lambda('lambda_25BB')
    def lambda_25BB():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_25BB)

    @scena.Lambda('lambda_25C9')
    def lambda_25C9():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_25C9)

    @scena.Lambda('lambda_25D7')
    def lambda_25D7():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0108, 0x0001, lambda_25D7)

    @scena.Lambda('lambda_25E5')
    def lambda_25E5():
        OP_67(0, 5220, -10000, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_25E5)

    @scena.Lambda('lambda_25FD')
    def lambda_25FD():
        OP_6E(287, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_25FD)

    CameraMove(880, 500, 43300, 3000)
    SetChrPos(0x0101, -620, 0, 32729, 0)
    SetChrPos(0x0102, 920, 0, 32590, 0)
    SetChrPos(0x0108, 90, 0, 34050, 0)

    @scena.Lambda('lambda_2651')
    def lambda_2651():
        ChrWalkTo(0x00FE, -770, 0, 39810, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2651)

    Sleep(300)

    @scena.Lambda('lambda_2671')
    def lambda_2671():
        ChrWalkTo(0x00FE, 1250, 0, 39890, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_2671)

    OP_62(0x0008, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    Sleep(500)

    ChrTalk(
        0x0008,
        (
            '#2160120007V这里是女王陛下\n',
            '居住的格兰赛尔城。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '如果没有事情的话，\n',
            '就请离开这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '哎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0001)

    ChrTalk(
        0x0101,
        (
            '#000F晚上好～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0102, 0x0001)

    ChrTalk(
        0x0102,
        (
            '#010F那天麻烦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160120012V怎么，原来是你们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '你们还呆在王都吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯。\n',
            '稍微有点事情。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F今天是因为受到正式的邀请\n',
            '才来这里的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0008, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    OP_62(0x0009, 0x00000000, 2000, 0x00, 0x01, 0x000000FA, 0x02)
    PlaySE(38, 0x00, 0x64)
    Sleep(1000)

    ChrTalk(
        0x0008,
        (
            '#2160120016V正式的……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '邀请……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0081040013V#070F……是公爵亲自\n',
            '给我们的请帖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrWalkTo(0x0108, 360, 0, 39010, 3000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#2160120019V哇！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '巨、巨人！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F给，这就是请帖。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrMoveTo(0x0108, 540, 0, 41430, 2000, 0x00)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '金把晚宴请帖\n',
            '递给了士兵们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    ChrMoveTo(0x0108, 360, 0, 39010, 2000, 0x00)

    ChrTalk(
        0x0008,
        (
            '#2160120022V嗯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '金·瓦赛克等４人\n',
            '在武术大会获得优胜，\n',
            '特此邀请参加晚宴……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '是这样吗……\n',
            '你们是武术大会的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160120025V我记得，获得优胜的是\n',
            '来自东方的武术家\n',
            '所率领的小组……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160120026V难道，你们就是\n',
            '那个小组的人吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嘿嘿，你说对了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F我们只不过是\n',
            '帮了点微不足道的忙而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '原来如此，是这样啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '……你们的事情\n',
            '我从女官长那里听说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '不过，好像少一个人啊。\n',
            '那一位怎么没有来呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#070F因为有点私事，\n',
            '所以没办法来参加了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0080120033V出席的只有我们而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160120034V是吗，那真是遗憾啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#2160120035V算了……\n',
            '现在就让你们进城吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2B5E')
    def lambda_2B5E():
        CameraMove(70, 750, 44190, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2B5E)

    @scena.Lambda('lambda_2B76')
    def lambda_2B76():
        OP_6C(0, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_2B76)

    @scena.Lambda('lambda_2B86')
    def lambda_2B86():
        OP_6E(438, 3000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_2B86)

    ChrWalkTo(0x0009, 70, 750, 45470, 2000, 0x00)
    WaitForThreadExit(0x0102, 0x0002)

    ChrTalk(
        0x0009,
        (
            '#2170120036V武术大会的优胜者，\n',
            '金选手等３个人前来光临！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#2170120037V开门！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_2BFA')
    def lambda_2BFA():
        CameraMove(70, 3450, 44190, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_2BFA)

    @scena.Lambda('lambda_2C12')
    def lambda_2C12():
        OP_67(0, 2270, -10000, 10000)

        ExitThread()

    DispatchAsync(0x0101, 0x0003, lambda_2C12)

    @scena.Lambda('lambda_2C2A')
    def lambda_2C2A():
        ChrWalkTo(0x0008, -1840, 750, 45060, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_2C2A)

    ChrWalkTo(0x0009, 1960, 750, 45000, 2000, 0x00)
    SetChrDirection(0x0009, 180, 400)
    WaitForThreadExit(0x0008, 0x0001)
    SetChrDirection(0x0008, 180, 400)
    OP_6F(0x0000, 0)
    OP_70(0x0000, 120)

    ChrTalk(
        0x0101,
        (
            '#000F哇啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010120039V和哈肯门一样，\n',
            '这个城门真有魄力啊！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020120040V#010F而且，只有王城才能\n',
            '建造得如此坚固呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这是不可能被攻陷的城呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '建国以来，虽然亚宁堡\n',
            '没有被外敌突破过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '因为贵族的叛乱，\n',
            '王都数次被卷入战火之中呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那个时候，这座王城\n',
            '击退了反叛军的进攻，\n',
            '保护了王家和避难的人民……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '有很多这种故事流传下来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎～有这样的事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0108,
        (
            '#0080120047V#070F嗯，有悠久历史的国家\n',
            '总会有古代浪漫的传说呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    WaitForThreadExit(0x0101, 0x0003)

    ChrTalk(
        0x0008,
        (
            '好了，请进吧！\n',
            '欢迎来到女王陛下的格兰赛尔城！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '从这里进去\n',
            '就会有接待人员前来迎接。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '那么，祝各位晚上玩得愉快。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00C7, 0, 0x638))
    EventEnd(0x00)

    Return()

# id: 0x0008 offset: 0x2EB3
@scena.Code('func_08_2EB3')
def func_08_2EB3():
    EventBegin(0x00)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0008, 0x0080)
    SetChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000C, 0x0080)
    ClearChrFlags(0x000D, 0x0080)
    CameraMove(70, -1900, 45200, 0)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(0, 0)
    OP_6E(357, 0)
    SetChrPos(0x000C, -790, 0, 41980, 180)
    SetChrPos(0x000D, 950, 0, 41980, 180)
    Sleep(500)

    @scena.Lambda('lambda_2F42')
    def lambda_2F42():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2F42)

    @scena.Lambda('lambda_2F50')
    def lambda_2F50():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2F50)

    CameraMove(70, 2550, 45150, 2000)

    ChrTalk(
        0x000C,
        (
            '#2620131152V怎、怎么回事……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '#2630131153V奇怪了啊……\n',
            '不是说已经完全封闭了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x000C, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)
    OP_62(0x000D, 0x00000000, 2000, 0x02, 0x07, 0x00000050, 0x01)
    PlaySE(39, 0x00, 0x64)

    @scena.Lambda('lambda_2FEE')
    def lambda_2FEE():
        SetChrDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000C, 0x0001, lambda_2FEE)

    @scena.Lambda('lambda_2FFC')
    def lambda_2FFC():
        SetChrDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x000D, 0x0001, lambda_2FFC)

    CameraMove(70, -1900, 45200, 1000)

    ChrTalk(
        0x000C,
        (
            '什么！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '怎么会！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    Sleep(100)

    Fade(1000)
    CameraMove(-1030, 0, 9000, 0)
    OP_67(0, 9340, -13360, 0)
    CameraSetDistance(1000, 0)
    OP_6C(135000, 0)
    OP_6E(747, 0)
    ClearChrFlags(0x0012, 0x0080)
    ClearChrFlags(0x0013, 0x0080)
    ClearChrFlags(0x0014, 0x0080)
    ClearChrFlags(0x0015, 0x0080)
    ClearChrFlags(0x0016, 0x0080)
    ClearChrFlags(0x000F, 0x0080)
    ClearChrFlags(0x0010, 0x0080)
    ClearChrFlags(0x0017, 0x0080)
    ClearChrFlags(0x0018, 0x0080)
    ClearChrFlags(0x0019, 0x0080)
    ClearChrFlags(0x001A, 0x0080)
    ClearChrFlags(0x000E, 0x0080)
    ClearChrFlags(0x0011, 0x0080)
    SetChrPos(0x0012, 1730, 0, -280, 0)
    SetChrPos(0x0013, 1730, 0, -2790, 180)
    SetChrPos(0x0014, 1730, 0, -5480, 180)
    SetChrPos(0x0015, 1730, 0, -8070, 180)
    SetChrPos(0x0016, 1730, 0, -10050, 180)
    SetChrPos(0x000F, 3230, 0, -4350, 0)
    SetChrPos(0x0010, 3230, 0, -1480, 0)
    SetChrPos(0x0017, -1770, 0, -380, 260)
    SetChrPos(0x0018, -1770, 0, -2970, 180)
    SetChrPos(0x0019, -1770, 0, -5140, 180)
    SetChrPos(0x001A, -1770, 0, -7650, 180)
    SetChrPos(0x000E, -3240, 0, -1470, 360)
    SetChrPos(0x0011, -3240, 0, -4130, 360)

    @scena.Lambda('lambda_319E')
    def lambda_319E():
        ChrWalkTo(0x00FE, -250, 0, 98520, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0012, 0x0001, lambda_319E)

    @scena.Lambda('lambda_31B9')
    def lambda_31B9():
        ChrWalkTo(0x00FE, -250, 0, 98520, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0013, 0x0001, lambda_31B9)

    @scena.Lambda('lambda_31D4')
    def lambda_31D4():
        ChrWalkTo(0x00FE, -250, 0, 98520, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0014, 0x0001, lambda_31D4)

    @scena.Lambda('lambda_31EF')
    def lambda_31EF():
        ChrWalkTo(0x00FE, -250, 0, 98520, 7500, 0x00)

        ExitThread()

    DispatchAsync(0x0015, 0x0001, lambda_31EF)

    @scena.Lambda('lambda_320A')
    def lambda_320A():
        ChrWalkTo(0x00FE, -250, 0, 98520, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x0016, 0x0001, lambda_320A)

    @scena.Lambda('lambda_3225')
    def lambda_3225():
        ChrWalkTo(0x00FE, -250, 0, 98520, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x000F, 0x0001, lambda_3225)

    @scena.Lambda('lambda_3240')
    def lambda_3240():
        ChrWalkTo(0x00FE, -250, 0, 98520, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0010, 0x0001, lambda_3240)

    @scena.Lambda('lambda_325B')
    def lambda_325B():
        ChrWalkTo(0x00FE, -250, 0, 98520, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0017, 0x0001, lambda_325B)

    @scena.Lambda('lambda_3276')
    def lambda_3276():
        ChrWalkTo(0x00FE, -250, 0, 98520, 8000, 0x00)

        ExitThread()

    DispatchAsync(0x0018, 0x0001, lambda_3276)

    @scena.Lambda('lambda_3291')
    def lambda_3291():
        ChrWalkTo(0x00FE, -250, 0, 98520, 7500, 0x00)

        ExitThread()

    DispatchAsync(0x0019, 0x0001, lambda_3291)

    @scena.Lambda('lambda_32AC')
    def lambda_32AC():
        ChrWalkTo(0x00FE, -250, 0, 98520, 7000, 0x00)

        ExitThread()

    DispatchAsync(0x001A, 0x0001, lambda_32AC)

    @scena.Lambda('lambda_32C7')
    def lambda_32C7():
        ChrWalkTo(0x00FE, -250, 0, 98520, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x000E, 0x0001, lambda_32C7)

    @scena.Lambda('lambda_32E2')
    def lambda_32E2():
        ChrWalkTo(0x00FE, -250, 0, 98520, 9000, 0x00)

        ExitThread()

    DispatchAsync(0x0011, 0x0001, lambda_32E2)

    @scena.Lambda('lambda_32FD')
    def lambda_32FD():
        CameraMove(-390, 0, 29050, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_32FD)

    @scena.Lambda('lambda_3315')
    def lambda_3315():
        OP_6C(44000, 5000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_3315)

    Sleep(1500)

    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    NewScene('ED6_DT01/T4201._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0009 offset: 0x333C
@scena.Code('func_09_333C')
def func_09_333C():
    EventBegin(0x00)
    FadeIn(2000, 0)
    SetChrFlags(0x0000, 0x0080)
    SetChrFlags(0x0001, 0x0080)
    SetChrFlags(0x0002, 0x0080)
    SetChrFlags(0x0003, 0x0080)
    CameraMove(0, 4000, 27740, 0)
    OP_67(0, 3170, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(12000, 0)
    OP_6E(568, 0)
    CameraMove(0, 1000, 27740, 4000)
    Sleep(1000)

    @scena.Lambda('lambda_33B4')
    def lambda_33B4():
        CameraMove(-310, 5670, 42340, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0001, lambda_33B4)

    @scena.Lambda('lambda_33CC')
    def lambda_33CC():
        OP_6C(0, 4000)

        ExitThread()

    DispatchAsync(0x0000, 0x0002, lambda_33CC)

    Sleep(2000)

    FadeOut(2000, 0, -1)
    OP_0D()
    SetScenaFlags(ScenaFlag(0x007F, 4, 0x3FC))
    NewScene('ED6_DT01/T4201._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x000A offset: 0x33F3
@scena.Code('func_0A_33F3')
def func_0A_33F3():
    EventBegin(0x00)
    SetChrPos(0x001B, 2600, 0, -3950, 0)
    SetChrPos(0x0101, 3420, 0, -2610, 357)
    SetChrPos(0x0102, 4150, 0, -4140, 0)
    ClearChrFlags(0x001B, 0x0080)
    SetMapFlags(0x00000001)
    OP_69(0x0101, 0)
    OP_6A(0x0101)
    OP_67(0, 9500, -10000, 0)
    CameraSetDistance(2800, 0)
    OP_6C(315, 0)
    OP_6E(262, 0)

    @scena.Lambda('lambda_346E')
    def lambda_346E():
        OP_6C(45000, 20000)

        ExitThread()

    DispatchAsync(0x0101, 0x0002, lambda_346E)

    @scena.Lambda('lambda_347E')
    def lambda_347E():
        ChrMoveToRelativeAsync(0x00FE, -3470, 0, 41430, 800, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_347E)

    @scena.Lambda('lambda_3499')
    def lambda_3499():
        ChrMoveToRelative(0x00FE, -3470, 0, 41430, 800, 0x00)

        ExitThread()

    DispatchAsync(0x0102, 0x0001, lambda_3499)

    @scena.Lambda('lambda_34B4')
    def lambda_34B4():
        ChrMoveToRelative(0x00FE, -3470, 0, 41430, 800, 0x00)

        ExitThread()

    DispatchAsync(0x001B, 0x0001, lambda_34B4)

    Sleep(1000)

    ChrTalk(
        0x0101,
        (
            '#000F老爸也真是的……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140559V生日庆典，还有王都观光，\n',
            '如果能一起就好了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0160140560V#080F不好意思，必须赶快召开军事会议了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140561V虽然理查德被逮捕了，\n',
            '逃亡中的特种兵还有很多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140562V凯诺娜上尉也不知道什么时候\n',
            '从那个地下遗迹中失踪了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140563V而且，参加大会的空贼团\n',
            '也趁混乱的时候逃走了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140564V为了在生日庆典中不发生骚动，\n',
            '必须加强警卫工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F真是的……\n',
            ' ',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F不过，我觉得在这种情况下\n',
            '也不会再引起什么骚动了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#080F总之，警卫方面可以放心。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '问题是，在那个地下遗迹里发生的事情，\n',
            '到底有什么含义呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140569V理查德解开的那个封印，\n',
            '到底会产生什么样的影响……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '『辉之环』是什么……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140571V这些事情必须要弄清楚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯……确实是这样。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140573V而且，理查德上校的\n',
            '记忆好像也很奇怪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#080F嗯，和克鲁茨一样，\n',
            '有些事情想不起来。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '尽管如此，在讯问中\n',
            '还是弄清楚了一件事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140576V就是那个黑色导力器的来历。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_381E')
    def lambda_381E():
        SetChrDirection(0x00FE, 180, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_381E)

    ChrTalk(
        0x0101,
        (
            '#000F哎……！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F查到制造它的人了吗！？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#080F不……\n',
            '知道把它带到情报部的人了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '是情报部特务部队队长，\n',
            '洛伦斯·博格少尉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F！！！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是、是那个人……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#080F在被选拔进情报部的时候，\n',
            '他把那个东西给了理查德。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140584V而且，理查德\n',
            '开始计划武装政变\n',
            '大概也是那个时候。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '总之，有必要调查清楚\n',
            '那个洛伦斯少尉的真实身份。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3989')
    def lambda_3989():
        SetChrDirection(0x00FE, 0, 400)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_3989)

    ChrTalk(
        0x0101,
        (
            '#000F是吗……\n',
            '虽然不知道具体怎么回事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '不过，只有我们见过他的真面目，\n',
            '真是幸运啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140588V如果可以的话，\n',
            '我可以画一张肖像画哦？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0160140589V#080F啊，那么到时候就拜托了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '虽然，对你的绘画水平\n',
            '没抱什么希望……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140591V还是去拜托雪拉扎德\n',
            '或者陛下她们比较好吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x001B, 400)

    ChrTalk(
        0x0101,
        (
            '#000F呜，这是什么意思！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TerminateThread(0x0102, 0xFF)
    ChrTurnDirection(0x0102, 0x0101, 400)

    @scena.Lambda('lambda_3AD2')
    def lambda_3AD2():
        OP_6C(45000, 2000)

        ExitThread()

    DispatchAsync(0x0102, 0x0002, lambda_3AD2)

    ClearMapFlags(0x00000001)
    OP_69(0x0101, 1000)

    ChrTalk(
        0x0102,
        (
            '#010F艾丝蒂尔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140594V洛伦斯少尉的脸，你看见过了？',
            TxtCtl.Enter,
        ),
    )

    Sleep(500)

    TerminateThread(0x0101, 0xFF)
    ChrTurnDirection(0x0101, 0x0102, 400)
    TerminateThread(0x001B, 0xFF)
    ChrTurnDirection(0x001B, 0x0102, 400)
    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F哎，我没告诉过你吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '在他逃跑前看到了一眼，\n',
            '他把头盔摘掉了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '是个银灰色头发的美男子呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F哎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F不过女王也说了，\n',
            '他的眼神非常的狂放。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '该怎么说呢……非常冷漠，\n',
            '却又很炽热……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140601V『您没有怜悯我的资格』\n',
            '他是这样对女王说的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F没有怜悯的资格……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140603V………………………………',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F约修亚……？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#0160140605V#080F唉，你从以前开始\n',
            '就经常考虑得太多。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140606V事情的善后处理就交给我们，\n',
            '你们还是尽情享受生日庆典吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x001B, 400)

    ChrTalk(
        0x0102,
        (
            '#010F啊……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '嗯，说的也是。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F是啊是啊。\n',
            '我们一定要玩个痛快。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '对了，今天晚上\n',
            '要在城里住吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x001B, 0x0101, 400)

    ChrTalk(
        0x001B,
        (
            '#0160140611V#080F对，女王陛下安排了\n',
            '王城右翼的两间客房给我们。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '我和约修亚在右边，\n',
            '艾丝蒂尔和雪拉扎德在左边。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x001B, 400)

    ChrTalk(
        0x0101,
        (
            '#000F哎……？\n',
            '我和雪拉姐住一起吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#080F别的组合可以吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0160140615V那么，我和艾丝蒂尔，\n',
            '约修亚和雪拉扎德，这样安排好了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '你可以尽情向老爸撒娇了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F……果然\n',
            '还是和雪拉姐一起比较好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x001B,
        (
            '#080F哇哈哈，真是害羞啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '那么，晚上再见了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    @scena.Lambda('lambda_3EFA')
    def lambda_3EFA():
        ChrTurnDirection(0x00FE, 0x001B, 0)
        Yield()

        Jump('lambda_3EFA')

    DispatchAsync2(0x0101, 0x0001, lambda_3EFA)

    @scena.Lambda('lambda_3F0B')
    def lambda_3F0B():
        ChrTurnDirection(0x00FE, 0x001B, 0)
        Yield()

        Jump('lambda_3F0B')

    DispatchAsync2(0x0102, 0x0001, lambda_3F0B)

    CreateThread(0x001B, 0x01, 0x00, 0x000B)
    Sleep(3000)

    TerminateThread(0x0101, 0xFF)
    TerminateThread(0x0102, 0xFF)
    OP_92(0x0102, 0x0101, 1500, 1000, 0x00)

    ChrTalk(
        0x0102,
        (
            '#010F好久没能和父亲住在同一间屋子了，\n',
            '不是很好嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020140621V关于你的母亲……\n',
            '不是有很多想说的事情吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F虽然是这样没错……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140623V不过很不情愿\n',
            '让约修亚和雪拉姐在一起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F哎？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 400)

    ChrTalk(
        0x0101,
        (
            '#000F没、没什么啦！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '话说回来……\n',
            '赶快去散步吧！',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010140627V街上好像很热闹呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F是啊。\n',
            '还有很多地方没看呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x00CD, 3, 0x66B))
    EventEnd(0x00)
    OP_6A(0x0000)

    Return()

# id: 0x000B offset: 0x4085
@scena.Code('func_0B_4085')
def func_0B_4085():
    ChrMoveToRelative(0x001B, -730, 0, 1250, 2000, 0x00)
    ChrWalkTo(0x001B, 70, 750, 43730, 2000, 0x00)
    ChrWalkTo(0x001B, 400, 750, 48060, 2000, 0x00)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
