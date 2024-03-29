import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T0111_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0111   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0111.x'
    header.mapIndex       = 11
    header.bgm            = 10
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
            dword_00        = 0xFFFED720,
            dword_04        = 0x00000000,
            dword_08        = 0x00007D00,
            word_0C         = 0x0004,
            word_0E         = 0x010E,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 315,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 11,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0xFFFED720,
            dword_04        = 0x00000000,
            dword_08        = 0x00007530,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 11,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0xFFFED338,
            dword_04        = 0x00000000,
            dword_08        = 0xFFFFF830,
            word_0C         = 0x0004,
            word_0E         = 0x005A,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 11,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00000BB8,
            dword_04        = 0x00000000,
            dword_08        = 0x00007530,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 11,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
        ScenaEntryPoint(
            dword_00        = 0x00009088,
            dword_04        = 0x00000000,
            dword_08        = 0x00007530,
            word_0C         = 0x0004,
            word_0E         = 0x0000,
            dword_10        = 0,
            dword_14        = 8000,
            dword_18        = -10000,
            dword_1C        = 0,
            dword_20        = 0,
            dword_24        = 0,
            dword_28        = 2600,
            dword_2C        = 262,
            word_30         = 45,
            word_32         = 0,
            word_34         = 360,
            word_36         = 0,
            word_38         = 0,
            word_3A         = 11,
            preInitScena    = 0x0000,
            preInitFunction = 0x0000,
            initScena       = 0x0000,
            initFunction    = 0x0001,
        ),
    )

# id: 0x10000 offset: 0x1B8
@scena.ChipData('ChipData')
def ChipData():
    return [
        # (ch, cp)
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
        ('ED6_DT07/CH01170._CH', 'ED6_DT07/CH01170P._CP'),
        ('ED6_DT07/CH01000._CH', 'ED6_DT07/CH01000P._CP'),
        ('ED6_DT07/CH01030._CH', 'ED6_DT07/CH01030P._CP'),
        ('ED6_DT07/CH01130._CH', 'ED6_DT07/CH01130P._CP'),
        ('ED6_DT07/CH01070._CH', 'ED6_DT07/CH01070P._CP'),
        ('ED6_DT07/CH01040._CH', 'ED6_DT07/CH01040P._CP'),
        ('ED6_DT07/CH01530._CH', 'ED6_DT07/CH01530P._CP'),
    ]

# id: 0x10001 offset: 0x1FA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '菲特',
            x                   = 37069,
            z                   = 0,
            y                   = 33566,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '尤妮',
            x                   = 38800,
            z                   = 0,
            y                   = 30060,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '拉欧老人',
            x                   = -35400,
            z                   = 0,
            y                   = 36030,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            name                = '亚尔丽',
            x                   = -39940,
            z                   = 0,
            y                   = 33130,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            name                = '芙莉莎',
            x                   = -4547,
            z                   = 0,
            y                   = 37480,
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
            name                = '阿妮娅',
            x                   = 3137,
            z                   = 0,
            y                   = 32103,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000A,
        ),
        ScenaNpcData(
            name                = '胡里奥',
            x                   = -35634,
            z                   = 0,
            y                   = 31939,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 6,
            chipIndex           = 6,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            name                = '加通老大',
            x                   = 4600,
            z                   = 0,
            y                   = 31530,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 7,
            chipIndex           = 7,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x000B,
        ),
    )

# id: 0x10002 offset: 0x2FA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x2FA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x2FA
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x2FA
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_309',
    )

    ChrClearFlags(0x0009, 0x0080)

    Jump('loc_322')

    def _loc_309(): pass

    label('loc_309')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_322',
    )

    ChrClearFlags(0x0009, 0x0080)
    ChrClearFlags(0x000E, 0x0080)

    Jump('loc_322')

    def _loc_322(): pass

    label('loc_322')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_32E',
    )

    ChrClearFlags(0x000F, 0x0080)

    def _loc_32E(): pass

    label('loc_32E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_342',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0008)

    Jump('loc_3A0')

    def _loc_342(): pass

    label('loc_342')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_34C',
    )

    Jump('loc_3A0')

    def _loc_34C(): pass

    label('loc_34C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_360',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0008)

    Jump('loc_3A0')

    def _loc_360(): pass

    label('loc_360')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_38C',
    )

    ChrSetPos(0x000A, -35860, 0, 32500, 172)
    ChrSetPos(0x000E, -35860, 0, 31320, 357)

    Jump('loc_3A0')

    def _loc_38C(): pass

    label('loc_38C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_3A0',
    )

    ChrSetFlags(0x000A, 0x0080)
    ChrSetFlags(0x000A, 0x0008)

    Jump('loc_3A0')

    def _loc_3A0(): pass

    label('loc_3A0')

    Return()

# id: 0x0001 offset: 0x3A1
@scena.Code('func_01_3A1')
def func_01_3A1():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_3B9',
    )

    OP_B1('t0111_y')

    Jump('loc_3C2')

    def _loc_3B9(): pass

    label('loc_3B9')

    OP_B1('t0111_n')

    def _loc_3C2(): pass

    label('loc_3C2')

    Return()

# id: 0x0002 offset: 0x3C3
@scena.Code('func_02_3C3')
def func_02_3C3():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3D8',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_3C3')

    def _loc_3D8(): pass

    label('loc_3D8')

    Return()

# id: 0x0003 offset: 0x3D9
@scena.Code('func_03_3D9')
def func_03_3D9():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_3FC',
    )

    OP_8D(0x00FE, -447, 33095, 4354, 30386, 4000)

    Jump('func_03_3D9')

    def _loc_3FC(): pass

    label('loc_3FC')

    Return()

# id: 0x0004 offset: 0x3FD
@scena.Code('func_04_3FD')
def func_04_3FD():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_4C5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_492',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '要尤妮一直跟着我生活\n',
            '的确也不太好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我是不是也该像里农的老妈那样\n',
            '从现在就开始物色女婿呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不，可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_4C2')

    def _loc_492(): pass

    label('loc_492')

    ChrTalk(
        0x00FE,
        (
            '唔～\n',
            '要尤妮一直跟着我生活\n',
            '的确也不太好……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_4C2(): pass

    label('loc_4C2')

    Jump('loc_1169')

    def _loc_4C5(): pass

    label('loc_4C5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_714',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0054, 6, 0x2A6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_6D4',
    )

    SetScenaFlags(ScenaFlag(0x0054, 6, 0x2A6))

    ChrTalk(
        0x00FE,
        (
            '里农的妈妈\n',
            '到这里找媳妇来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哈哈，\n',
            '我家的尤妮还太小了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '尤妮的夫婿一定要是\n',
            '能超越我的男人！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#002F（菲特先生这么热血，\n',
            '　真少见呀……）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F（嗯，只要是父亲\n',
            '　应该都会热血沸腾的。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '约修亚， \n',
            '我其实很欣赏你，不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你不合格。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#014F啊？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '因为，\n',
            '谁叫你长得太帅了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '而且你总是不经意\n',
            '卷入一些涉及女性的问题上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F嗯，我也有同感。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#007F约修亚对这方面的话题\n',
            '总是唯恐避之不及。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '这也是个问题啊～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#018F（……唯恐避之不及的是你吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_711')

    def _loc_6D4(): pass

    label('loc_6D4')

    ChrTalk(
        0x00FE,
        (
            '嗯，约修亚的话，\n',
            '年龄相差有些悬殊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '还是不合格……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_711(): pass

    label('loc_711')

    Jump('loc_1169')

    def _loc_714(): pass

    label('loc_714')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_7D5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_7B3',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '你们好，艾丝蒂尔、约修亚。\n',
            '听说你们最近很活跃啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '镇上人都说你们是\n',
            '备受期待的年轻一辈游击士呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真不愧是卡西乌斯的孩子啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D2')

    def _loc_7B3(): pass

    label('loc_7B3')

    ChrTalk(
        0x00FE,
        (
            '我也支持你们，\n',
            '要加油哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7D2(): pass

    label('loc_7D2')

    Jump('loc_1169')

    def _loc_7D5(): pass

    label('loc_7D5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_92C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_8F0',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '十年前，突破边境线\n',
            '大举入侵而来的帝国军\n',
            '肆意践踏了整个利贝尔王国……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但是，通过一次\n',
            '奇迹般的闪电作战，\n',
            '我们终于击退了帝国军。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果没有那次作战 \n',
            '现在这里已经是帝国的领土了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也随洛连特的\n',
            '部队一起参加了战斗，\n',
            '但被打伤了腿，变成了现在这样。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_929')

    def _loc_8F0(): pass

    label('loc_8F0')

    ChrTalk(
        0x00FE,
        (
            '如果没有那次作战，\n',
            '现在这里已经是帝国的领土了吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_929(): pass

    label('loc_929')

    Jump('loc_1169')

    def _loc_92C(): pass

    label('loc_92C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_AFE',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0054, 5, 0x2A5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_A9C',
    )

    SetScenaFlags(ScenaFlag(0x0054, 5, 0x2A5))

    ChrTalk(
        0x00FE,
        (
            '你们俩听你们父亲谈起过\n',
            '他在军队时的事吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F没……\n',
            '他不怎么提起\n',
            '成为游击士前的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#000F不过，\n',
            '倒是经常提起妈妈的事……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '约修亚听说过吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F……不，没有呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '就算问他， \n',
            '他也总是支吾着岔开话题。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F就是啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '……是吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不管怎么说，\n',
            '利贝尔终于恢复和平了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但愿尤妮……\n',
            '但愿女儿能一直\n',
            '生活在和平的时代。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AFB')

    def _loc_A9C(): pass

    label('loc_A9C')

    ChrTalk(
        0x00FE,
        (
            '不管怎么说，\n',
            '利贝尔终于恢复和平了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但愿尤妮……\n',
            '但愿女儿能一直\n',
            '生活在和平的时代。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AFB(): pass

    label('loc_AFB')

    Jump('loc_1169')

    def _loc_AFE(): pass

    label('loc_AFE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_CD8',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0054, 4, 0x2A4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_C76',
    )

    SetScenaFlags(ScenaFlag(0x0054, 4, 0x2A4))

    ChrTalk(
        0x0008,
        (
            '为何帕特和鲁克\n',
            '要跑到北边的塔里面去呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '在被魔兽袭击的时候\n',
            '多亏你们救了他们啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '干得不错啊。\n',
            '不愧是卡西乌斯的孩子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#007F嗯，唉～不过……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '怎么了？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F实际上最后我们\n',
            '也陷入了危险之中，\n',
            '多亏父亲及时赶到帮了我们。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哈哈，你们俩还年轻嘛，\n',
            '以后还有很大的潜力可以发掘的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '尤妮也回家了，\n',
            '没有什么比大家平安无事更好的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_CD5')

    def _loc_C76(): pass

    label('loc_C76')

    ChrTalk(
        0x0008,
        (
            '你们两个都还很年轻，\n',
            '以后还有很大的潜力可以发掘的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '没有什么比大家平安无事更好的了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_CD5(): pass

    label('loc_CD5')

    Jump('loc_1169')

    def _loc_CD8(): pass

    label('loc_CD8')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_E9F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_DB6',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x0008,
        (
            '我家的尤妮\n',
            '也是时候该回来了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '唔，奇怪了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '艾丝蒂尔、约修亚。\n',
            '你们如果看见了我家的尤妮\n',
            '就叫她早些回家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '现在虽然离晚上\n',
            '关门的时间还很早……\n',
            '不过女孩子是要多担心一些才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E9C')

    def _loc_DB6(): pass

    label('loc_DB6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E52',
    )

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x0008,
        (
            '对了，\n',
            '尤妮经常和帕特、\n',
            '鲁克在一起玩……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '为什么总是那么喜欢\n',
            '和男孩子一起玩呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010150156V#501F什么？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '啊，没、没什么……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E9C')

    def _loc_E52(): pass

    label('loc_E52')

    ChrTalk(
        0x0008,
        (
            '现在虽然离晚上\n',
            '关门的时间还很早……\n',
            '不过女孩子是要多担心一些才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E9C(): pass

    label('loc_E9C')

    Jump('loc_1169')

    def _loc_E9F(): pass

    label('loc_E9F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0054, 3, 0x2A3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1108',
    )

    SetScenaFlags(ScenaFlag(0x0054, 3, 0x2A3))

    ChrTalk(
        0x0008,
        (
            '噢，这不是\n',
            '艾丝蒂尔和约修亚吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F早上好啊，\n',
            '菲特叔叔。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F早上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '卡西乌斯他可还好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F嗯，还好，\n',
            '就是有些忙。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#000F疾病和伤痛\n',
            '一般都不会找他的麻烦的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '呵呵，是这样啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我家女儿说\n',
            '在街上偶尔能看到他，\n',
            '不过我已经好长时间没见他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果你们不介意的话，\n',
            '帮我捎个口信给你们父亲好吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '就说菲特偶尔\n',
            '想找老朋友叙叙旧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#010F嗯，我会转达的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F（……对了，约修亚。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0102, 500)

    ChrTalk(
        0x0101,
        (
            '#000F（菲特叔叔\n',
            '　和老爸是什么关系呢？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#000F（我只知道\n',
            '　他们是朋友。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0101, 500)

    ChrTalk(
        0x0102,
        (
            '#010F（我听说他们是\n',
            '　王国军时代的战友。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F（啊，是这样的啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1169')

    def _loc_1108(): pass

    label('loc_1108')

    ChrTalk(
        0x0008,
        (
            '你们回去告诉他，\n',
            '让他平时有空的时候\n',
            '也来我家坐坐喝喝茶。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '老朋友偶尔叙叙旧\n',
            '也很不错嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1169(): pass

    label('loc_1169')

    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x116D
@scena.Code('func_05_116D')
def func_05_116D():
    TalkBegin(0x0009)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_11A2',
    )

    ChrTalk(
        0x00FE,
        (
            '爸爸真是的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我才刚７岁啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1378')

    def _loc_11A2(): pass

    label('loc_11A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_11EE',
    )

    ChrTalk(
        0x00FE,
        (
            '爸爸问了我\n',
            '一件奇怪的事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他问我鲁克\n',
            '和帕特当中选哪个。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1378')

    def _loc_11EE(): pass

    label('loc_11EE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_1250',
    )

    ChrTalk(
        0x0009,
        (
            '今天呢，\n',
            '我一直留在爸爸身边孝顺他。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '只要我呆在爸爸身边，\n',
            '爸爸也就会很高兴的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1378')

    def _loc_1250(): pass

    label('loc_1250')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_1378',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 2, 0x2)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1315',
    )

    SetScenaFlags(ScenaFlag(0x0000, 2, 0x2))

    ChrTalk(
        0x0009,
        (
            '艾丝蒂尔姐姐，\n',
            '约修亚哥哥！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '谢谢你们救了\n',
            '帕特和鲁克啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '爱娜姐姐对你们的表现\n',
            '评价很高呢，\n',
            '艾丝蒂尔姐姐你们好厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#501F呵呵……\n',
            '谢谢你的支持，小尤妮……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1378')

    def _loc_1315(): pass

    label('loc_1315')

    ChrTalk(
        0x0009,
        (
            '谢谢你们救了\n',
            '帕特和鲁克啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '爱娜姐姐对你们的\n',
            '表现评价很高呢，\n',
            '艾丝蒂尔姐姐你们好厉害啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1378(): pass

    label('loc_1378')

    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0x137C
@scena.Code('func_06_137C')
def func_06_137C():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_14AC',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1432',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '最近的年轻人\n',
            '就只关注眼前的利益。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我年轻时\n',
            '也有一段时间瞻前不顾后地\n',
            '一心只想要得到别人认同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女儿说得没错，\n',
            '或许他也需要更多的支持和帮助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_14A9')

    def _loc_1432(): pass

    label('loc_1432')

    ChrTalk(
        0x00FE,
        (
            '我年轻的时候\n',
            '也有一段时间瞻前不顾后地\n',
            '一心只想要得到别人认同。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女儿说得没错，\n',
            '或许他也需要更多的支持和帮助。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_14A9(): pass

    label('loc_14A9')

    Jump('loc_19BF')

    def _loc_14AC(): pass

    label('loc_14AC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_15DA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1575',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '所谓林业，\n',
            '并不只是为了利用树木\n',
            '而栽培树木。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '同时也要守护森林，\n',
            '与森林相互依存并感谢其恩赐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只有领会了这一点，\n',
            '才能算一个合格的林业工人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女婿还远远不够格呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_15D7')

    def _loc_1575(): pass

    label('loc_1575')

    ChrTalk(
        0x00FE,
        (
            '要守护森林，\n',
            '与森林相互依存并感谢其恩赐。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只有领会了这一点，\n',
            '才能算一个合格的林业工人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_15D7(): pass

    label('loc_15D7')

    Jump('loc_19BF')

    def _loc_15DA(): pass

    label('loc_15DA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_16E1',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1683',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x00FE,
        (
            '要不是这腰不中用，\n',
            '我也还能在森林里干干活儿啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '身体这儿疼那儿疼的真叫人懊丧，\n',
            '我还想再接着工作呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只靠女婿一个的话总是不放心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_16DE')

    def _loc_1683(): pass

    label('loc_1683')

    ChrTalk(
        0x00FE,
        (
            '要不是这腰不中用，\n',
            '我也还能在森林里干干活儿啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只靠女婿一个的话总是不放心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_16DE(): pass

    label('loc_16DE')

    Jump('loc_19BF')

    def _loc_16E1(): pass

    label('loc_16E1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_17E7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_178A',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000A,
        (
            '哼，工作就算\n',
            '进行得顺利了一点，\n',
            '也不能有骄傲的情绪。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '你作为我女婿想接我的班\n',
            '还差得远呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '必须靠洛连特的林业发展\n',
            '自己的脚跟才会站稳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_17E4')

    def _loc_178A(): pass

    label('loc_178A')

    ChrTalk(
        0x000A,
        (
            '你作为我女婿想接我的班\n',
            '还差得远呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '必须靠洛连特的林业发展\n',
            '自己的脚跟才会站稳。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_17E4(): pass

    label('loc_17E4')

    Jump('loc_19BF')

    def _loc_17E7(): pass

    label('loc_17E7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_18AB',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1871',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000A,
        (
            '哼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '太嫩了，\n',
            '那家伙也不过是个半吊子而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '想在两三年内\n',
            '在林业上做出好成绩来，\n',
            '这种想法也太天真了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_18A8')

    def _loc_1871(): pass

    label('loc_1871')

    ChrTalk(
        0x000A,
        (
            '哼……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '太嫩了，\n',
            '那家伙也不过是个半吊子而已。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_18A8(): pass

    label('loc_18A8')

    Jump('loc_19BF')

    def _loc_18AB(): pass

    label('loc_18AB')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 3, 0x3)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1968',
    )

    SetScenaFlags(ScenaFlag(0x0000, 3, 0x3))

    ChrTalk(
        0x000A,
        (
            '农业、矿业以及林业\n',
            '是洛连特的三大产业。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '说它们是\n',
            '洛连特的经济支柱\n',
            '也毫不为过。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '其中植树造林，\n',
            '循环地利用树木作为资源的林业，\n',
            '是由艾莉茜雅女王的提案发展而来的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_19BF')

    def _loc_1968(): pass

    label('loc_1968')

    ChrTalk(
        0x000A,
        (
            '无论洛连特的森林资源有多么丰富，\n',
            '也不是取之不尽的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '女王陛下的想法真是妙啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_19BF(): pass

    label('loc_19BF')

    TalkEnd(0x000A)

    Return()

# id: 0x0007 offset: 0x19C3
@scena.Code('func_07_19C3')
def func_07_19C3():
    TalkBegin(0x000B)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_1A5F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1A33',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '最近丈夫和父亲\n',
            '好像少了很多隔阂了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '太好了啊……\n',
            '和睦温馨的家庭比什么都要好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1A5C')

    def _loc_1A33(): pass

    label('loc_1A33')

    ChrTalk(
        0x00FE,
        (
            '我对父亲苦苦的劝说\n',
            '果然得到了效果。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1A5C(): pass

    label('loc_1A5C')

    Jump('loc_1E4D')

    def _loc_1A5F(): pass

    label('loc_1A5F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_1B2E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1ADF',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '父亲不再对丈夫的工作\n',
            '抱怨不停了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '看他好像有什么话想说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '干吗不痛痛快快\n',
            '说清楚呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1B2B')

    def _loc_1ADF(): pass

    label('loc_1ADF')

    ChrTalk(
        0x00FE,
        (
            '父亲不再对丈夫的工作\n',
            '抱怨不停了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，\n',
            '看他好像有什么话想说。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1B2B(): pass

    label('loc_1B2B')

    Jump('loc_1E4D')

    def _loc_1B2E(): pass

    label('loc_1B2E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_1B7D',
    )

    ChrTalk(
        0x00FE,
        (
            '最近，父亲成天念念叨叨地\n',
            '在盘算着什么事。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '到底在想什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E4D')

    def _loc_1B7D(): pass

    label('loc_1B7D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_1BD1',
    )

    ChrTalk(
        0x00FE,
        (
            '最近丈夫的工作\n',
            '好像很顺利。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '父亲也该接受他为继承人了，\n',
            '可是……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E4D')

    def _loc_1BD1(): pass

    label('loc_1BD1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_1C87',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1C40',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x00FE,
        (
            '刚才买东西时\n',
            '我就注意到了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '新鲜蔬菜\n',
            '似乎比平时少了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是心理作用吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1C84')

    def _loc_1C40(): pass

    label('loc_1C40')

    ChrTalk(
        0x00FE,
        (
            '刚才买东西时\n',
            '我就注意到了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '新鲜蔬菜\n',
            '似乎比平时少了呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1C84(): pass

    label('loc_1C84')

    Jump('loc_1E4D')

    def _loc_1C87(): pass

    label('loc_1C87')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_1D6F',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1D0E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000B,
        (
            '又开始了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我父亲对我丈夫\n',
            '也太过严厉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '丈夫已经在拼命努力了，\n',
            '父亲应该把目光放长远一点才好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1D6C')

    def _loc_1D0E(): pass

    label('loc_1D0E')

    ChrTalk(
        0x000B,
        (
            '我父亲对我丈夫\n',
            '也太过严厉了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '丈夫已经在拼命努力了，\n',
            '父亲应该把目光放长远一点才好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1D6C(): pass

    label('loc_1D6C')

    Jump('loc_1E4D')

    def _loc_1D6F(): pass

    label('loc_1D6F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_1DB4',
    )

    ChrTalk(
        0x000B,
        (
            '很快就到\n',
            '丈夫回来的时间了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '得赶快把晚饭准备好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E4D')

    def _loc_1DB4(): pass

    label('loc_1DB4')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 4, 0x4)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1E19',
    )

    SetScenaFlags(ScenaFlag(0x0000, 4, 0x4))

    ChrTalk(
        0x000B,
        (
            '好了～\n',
            '我丈夫已经工作去了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000B,
        (
            '我要快点把\n',
            '早上的家务弄完，\n',
            '然后到街上去买菜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1E4D')

    def _loc_1E19(): pass

    label('loc_1E19')

    ChrTalk(
        0x000B,
        (
            '我要快点把\n',
            '早上的家务弄完，\n',
            '然后到街上去买菜。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1E4D(): pass

    label('loc_1E4D')

    TalkEnd(0x000B)

    Return()

# id: 0x0008 offset: 0x1E51
@scena.Code('func_08_1E51')
def func_08_1E51():
    TalkBegin(0x000E)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_1F4B',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 7, 0x7)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1EEB',
    )

    SetScenaFlags(ScenaFlag(0x0000, 7, 0x7))

    ChrTalk(
        0x000E,
        (
            '唉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不管怎样，\n',
            '我接手的那份工作一定要完成才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过想要得到岳父的认可\n',
            '可是很不容易的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '我要努力加油啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1F4B')

    def _loc_1EEB(): pass

    label('loc_1EEB')

    ChrTalk(
        0x000E,
        (
            '不管怎样，\n',
            '我接手的那份工作一定要完成才行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000E,
        (
            '不过想要得到岳父的认可\n',
            '可是很不容易的呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F4B(): pass

    label('loc_1F4B')

    TalkEnd(0x000E)

    Return()

# id: 0x0009 offset: 0x1F4F
@scena.Code('func_09_1F4F')
def func_09_1F4F():
    TalkBegin(0x000C)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_203A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2002',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '老公他终于\n',
            '从矿山回来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '已经好几天没见他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '女儿看到她爸回来肯定会很高兴的，\n',
            '今天我也要做一顿美餐。\n',
            '毕竟一家人好久都没一起吃饭了，呵呵。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2037')

    def _loc_2002(): pass

    label('loc_2002')

    ChrTalk(
        0x00FE,
        (
            '今天一家人要吃团圆饭呢。\n',
            '要早点做好晚饭才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2037(): pass

    label('loc_2037')

    Jump('loc_2567')

    def _loc_203A(): pass

    label('loc_203A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_2142',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_20E5',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '老公终于有消息了，\n',
            '说是矿山的工作\n',
            '就要告一段落了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，得准备一顿大餐才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '正因为有离别\n',
            '才更体会得到彼此的牵绊啊，\n',
            '这样也不错嘛。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_213F')

    def _loc_20E5(): pass

    label('loc_20E5')

    ChrTalk(
        0x00FE,
        (
            '老公终于有消息了，\n',
            '说是矿山的工作\n',
            '就要告一段落了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵，得准备一顿大餐才行啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_213F(): pass

    label('loc_213F')

    Jump('loc_2567')

    def _loc_2142(): pass

    label('loc_2142')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_2183',
    )

    ChrTalk(
        0x00FE,
        (
            '我听说矿山里\n',
            '有魔兽出没……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '老公他没事吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2567')

    def _loc_2183(): pass

    label('loc_2183')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_227A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_221D',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '刚才老公工作的矿山\n',
            '发了联络过来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说好像是新矿脉中\n',
            '发现了非同小可的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说是『非同小可』，\n',
            '到底是什么样的东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2277')

    def _loc_221D(): pass

    label('loc_221D')

    ChrTalk(
        0x00FE,
        (
            '老公工作的矿山\n',
            '发现了非同小可的东西。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '说是『非同小可』，\n',
            '到底是什么样的东西呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2277(): pass

    label('loc_2277')

    Jump('loc_2567')

    def _loc_227A(): pass

    label('loc_227A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_2355',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2322',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x00FE,
        (
            '老公在矿山\n',
            '努力地工作，\n',
            '我也一定要加油呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '只要这么一想，\n',
            '和老公的分别\n',
            '也意外地并不那么难耐了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '呵呵呵，这也是\n',
            '爱的其中一种形式吧㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2352')

    def _loc_2322(): pass

    label('loc_2322')

    ChrTalk(
        0x00FE,
        (
            '老公在矿山\n',
            '努力地工作，\n',
            '我也一定要加油呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2352(): pass

    label('loc_2352')

    Jump('loc_2567')

    def _loc_2355(): pass

    label('loc_2355')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_23C0',
    )

    ChrTalk(
        0x000C,
        (
            '刚才老公联络我说\n',
            '矿山又发现了\n',
            '什么新的矿脉。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '唉……今天的晚饭\n',
            '又只有我和女儿两人吃了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2567')

    def _loc_23C0(): pass

    label('loc_23C0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_24A9',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2457',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x000C,
        (
            '虽说已经到了\n',
            '可以开始准备晚餐的时候了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '不过不知道老公\n',
            '今天会不会回来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '在矿山里面\n',
            '通宵的工作\n',
            '是常有的事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_24A6')

    def _loc_2457(): pass

    label('loc_2457')

    ChrTalk(
        0x000C,
        (
            '不知道老公\n',
            '今天会不会回来啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '在矿山里面\n',
            '通宵的工作\n',
            '是常有的事情呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_24A6(): pass

    label('loc_24A6')

    Jump('loc_2567')

    def _loc_24A9(): pass

    label('loc_24A9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 6, 0x6)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2526',
    )

    SetScenaFlags(ScenaFlag(0x0000, 6, 0x6))

    ChrTalk(
        0x000C,
        (
            '我的老公\n',
            '在北面的玛鲁加矿山工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '今天也是\n',
            '一大早就去上班了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '而且经常一连几天\n',
            '都不能回一次家。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_2567')

    def _loc_2526(): pass

    label('loc_2526')

    ChrTalk(
        0x000C,
        (
            '他这样会因为\n',
            '劳累过度而病倒的啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000C,
        (
            '我真的好担心他啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2567(): pass

    label('loc_2567')

    TalkEnd(0x000C)

    Return()

# id: 0x000A offset: 0x256B
@scena.Code('func_0A_256B')
def func_0A_256B():
    TalkBegin(0x000D)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004D, 0, 0x268)),
            Expr.Return,
        ),
        'loc_25ED',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_25CE',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '爸爸回来了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '刚才回来的哦。\n',
            '他说等一下要和我玩呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '太好了！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_25EA')

    def _loc_25CE(): pass

    label('loc_25CE')

    ChrTalk(
        0x00FE,
        (
            '我好想早点和爸爸玩呢！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_25EA(): pass

    label('loc_25EA')

    Jump('loc_28AA')

    def _loc_25ED(): pass

    label('loc_25ED')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x004B, 1, 0x259)),
            Expr.Return,
        ),
        'loc_26A2',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_266E',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x00FE,
        (
            '嗨！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '听我说听我说！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '爸爸他、\n',
            '爸爸他要回家了哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '但愿快点到家。\n',
            '阿妮娅要好好和他一起玩！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_269F')

    def _loc_266E(): pass

    label('loc_266E')

    ChrTalk(
        0x00FE,
        (
            '但愿爸爸快点到家。\n',
            '阿妮娅要好好和他一起玩！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_269F(): pass

    label('loc_269F')

    Jump('loc_28AA')

    def _loc_26A2(): pass

    label('loc_26A2')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0049, 7, 0x24F)),
            Expr.Return,
        ),
        'loc_26DE',
    )

    ChrTalk(
        0x00FE,
        (
            '哎，妈妈没什么精神呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '发生什么事了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28AA')

    def _loc_26DE(): pass

    label('loc_26DE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0047, 1, 0x239)),
            Expr.Return,
        ),
        'loc_2742',
    )

    ChrTalk(
        0x00FE,
        (
            '爸爸不在的时候\n',
            '我就努力给妈妈帮忙。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '帮着打扫、\n',
            '洗衣服、做饭。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '很了不起吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28AA')

    def _loc_2742(): pass

    label('loc_2742')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 3, 0x213)),
            Expr.Return,
        ),
        'loc_2791',
    )

    ChrTalk(
        0x00FE,
        (
            '阿妮娅也马上\n',
            '要去主日学校上学了哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不知道学校好不好玩呢？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28AA')

    def _loc_2791(): pass

    label('loc_2791')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0042, 2, 0x212)),
            Expr.Return,
        ),
        'loc_27CC',
    )

    ChrTalk(
        0x000D,
        (
            '爸爸今天因为工作\n',
            '不能回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '唉……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28AA')

    def _loc_27CC(): pass

    label('loc_27CC')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0040, 5, 0x205)),
            Expr.Return,
        ),
        'loc_2812',
    )

    ChrTalk(
        0x000D,
        (
            '阿妮娅\n',
            '好崇拜爸爸哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '又有力气，\n',
            '对阿妮娅又温柔～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28AA')

    def _loc_2812(): pass

    label('loc_2812')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 5, 0x5)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2889',
    )

    SetScenaFlags(ScenaFlag(0x0000, 5, 0x5))

    ChrTalk(
        0x000D,
        (
            '我爸爸啊，\n',
            '是在矿场工作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '他发现了一个\n',
            '好漂亮好漂亮的石头哦～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000D,
        (
            '他还说\n',
            '要送给我做礼物哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_28AA')

    def _loc_2889(): pass

    label('loc_2889')

    ChrTalk(
        0x000D,
        (
            '我爸爸啊，\n',
            '是在矿场工作的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_28AA(): pass

    label('loc_28AA')

    TalkEnd(0x000D)

    Return()

# id: 0x000B offset: 0x28AE
@scena.Code('func_0B_28AE')
def func_0B_28AE():
    TalkBegin(0x000F)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0001, 0, 0x8)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_298F',
    )

    SetScenaFlags(ScenaFlag(0x0001, 0, 0x8))
    ChrTurnDirection(0x00FE, 0x0101, 0)

    ChrTalk(
        0x00FE,
        (
            '哟，这不是\n',
            '游击士小姑娘和小兄弟吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#000F啊，你是玛鲁加矿山的……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '之前给你们添麻烦了，\n',
            '好在大家最后都平安无事啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '矿山的魔兽骚动\n',
            '终于也告一段落了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也好久\n',
            '没有回家休息了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_29B0')

    def _loc_298F(): pass

    label('loc_298F')

    ChrTalk(
        0x00FE,
        (
            '果然还是\n',
            '呆在家里最舒服啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_29B0(): pass

    label('loc_29B0')

    TalkEnd(0x000F)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
