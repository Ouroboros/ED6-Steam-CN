import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
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
        ('ED6_DT07/CH01460._CH', 'ED6_DT07/CH01460P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10001 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '盖尔多那',
            x                   = 98500,
            z                   = 0,
            y                   = 17600,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            name                = '王国军宪兵',
            x                   = 110290,
            z                   = 1990,
            y                   = 24010,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
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

# id: 0x10002 offset: 0x11A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x11A
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x11A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x11A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_126',
    )

    ChrSetFlags(0x0009, 0x0080)

    def _loc_126(): pass

    label('loc_126')

    Return()

# id: 0x0001 offset: 0x127
@scena.Code('func_01_127')
def func_01_127():
    OP_16(0x02, 4000, -16000, -108000, 2293834)
    PlaySE(453, 0x01, 0x64)

    Return()

# id: 0x0002 offset: 0x13F
@scena.Code('func_02_13F')
def func_02_13F():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_1E0',
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
    OP_62(0x00FE, 0x00000000, 2000, 0x18, 0x1B, 0x000000FA, 0x00)
    Sleep(3000)

    OP_63(0x00FE)

    Jump('func_02_13F')

    def _loc_1E0(): pass

    label('loc_1E0')

    Return()

# id: 0x0003 offset: 0x1E1
@scena.Code('func_03_1E1')
def func_03_1E1():
    ExecExpressionWithReg(
        0x0001,
        (
            Expr.Rand,
            (Expr.PushLong, 0xE),
            Expr.Mod,
            Expr.Nop,
            Expr.Return,
        ),
    )

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_206',
    )

    OP_99(0x00FE, 0x00, 0x07, 1650)

    Jump('loc_348')

    def _loc_206(): pass

    label('loc_206')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_21F',
    )

    OP_99(0x00FE, 0x01, 0x07, 1600)

    Jump('loc_348')

    def _loc_21F(): pass

    label('loc_21F')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_238',
    )

    OP_99(0x00FE, 0x02, 0x07, 1550)

    Jump('loc_348')

    def _loc_238(): pass

    label('loc_238')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x3),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_251',
    )

    OP_99(0x00FE, 0x03, 0x07, 1500)

    Jump('loc_348')

    def _loc_251(): pass

    label('loc_251')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_26A',
    )

    OP_99(0x00FE, 0x04, 0x07, 1450)

    Jump('loc_348')

    def _loc_26A(): pass

    label('loc_26A')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_283',
    )

    OP_99(0x00FE, 0x05, 0x07, 1400)

    Jump('loc_348')

    def _loc_283(): pass

    label('loc_283')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x6),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_29C',
    )

    OP_99(0x00FE, 0x06, 0x07, 1350)

    Jump('loc_348')

    def _loc_29C(): pass

    label('loc_29C')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x7),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2B5',
    )

    OP_99(0x00FE, 0x00, 0x07, 1655)

    Jump('loc_348')

    def _loc_2B5(): pass

    label('loc_2B5')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2CE',
    )

    OP_99(0x00FE, 0x01, 0x07, 1605)

    Jump('loc_348')

    def _loc_2CE(): pass

    label('loc_2CE')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x9),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_2E7',
    )

    OP_99(0x00FE, 0x02, 0x07, 1555)

    Jump('loc_348')

    def _loc_2E7(): pass

    label('loc_2E7')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xA),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_300',
    )

    OP_99(0x00FE, 0x03, 0x07, 1505)

    Jump('loc_348')

    def _loc_300(): pass

    label('loc_300')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xB),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_319',
    )

    OP_99(0x00FE, 0x04, 0x07, 1455)

    Jump('loc_348')

    def _loc_319(): pass

    label('loc_319')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xC),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_332',
    )

    OP_99(0x00FE, 0x05, 0x07, 1405)

    Jump('loc_348')

    def _loc_332(): pass

    label('loc_332')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0xD),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_348',
    )

    OP_99(0x00FE, 0x06, 0x07, 1355)

    def _loc_348(): pass

    label('loc_348')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_35D',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('loc_348')

    def _loc_35D(): pass

    label('loc_35D')

    Return()

# id: 0x0004 offset: 0x35E
@scena.Code('func_04_35E')
def func_04_35E():
    TalkBegin(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_467',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_3D2',
    )

    ChrTalk(
        0x00FE,
        (
            '如果下任市长确定了，房屋\n',
            '就完全属于卢安市民了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我们士兵也希望\n',
            '能住进出色的大人物啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_464')

    def _loc_3D2(): pass

    label('loc_3D2')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '如果下任市长确定了，房屋\n',
            '就完全属于卢安市民了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '无论哪位候选人胜出\n',
            '都将是首位平民出身的市长……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '这样贵族制的影子\n',
            '也将被抹去吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_464(): pass

    label('loc_464')

    Jump('loc_65F')

    def _loc_467(): pass

    label('loc_467')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_51E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_4C4',
    )

    ChrTalk(
        0x00FE,
        (
            '强化跟协会的合作\n',
            '是军队全体的改善目标。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '最近军队高层\n',
            '都这样说了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51B')

    def _loc_4C4(): pass

    label('loc_4C4')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '好像发生了骚动，\n',
            '不过这边没有异常。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果有什么事\n',
            '会马上联系游击士协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_51B(): pass

    label('loc_51B')

    Jump('loc_65F')

    def _loc_51E(): pass

    label('loc_51E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_60A',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 1, 0x1)),
            Expr.Return,
        ),
        'loc_58D',
    )

    ChrTalk(
        0x00FE,
        (
            '这里的女佣们，相当亲切地\n',
            '拿出茶点款待我们呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '伙食也很不错，\n',
            '真是不想回要塞了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_607')

    def _loc_58D(): pass

    label('loc_58D')

    SetScenaFlags(ScenaFlag(0x0000, 1, 0x1))

    ChrTalk(
        0x00FE,
        (
            '这个宅邸现在被\n',
            '王国军管理。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '进出是无所谓，\n',
            '但府邸内也有贵重物品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '以防万一请不要损坏，\n',
            '在府邸内请当心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_607(): pass

    label('loc_607')

    Jump('loc_65F')

    def _loc_60A(): pass

    label('loc_60A')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_65F',
    )

    ChrTalk(
        0x00FE,
        (
            '这个宅邸现在\n',
            '在王国军的管理下。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '下任市长选出之后\n',
            '将作为市政厅使用。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_65F(): pass

    label('loc_65F')

    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x663
@scena.Code('func_05_663')
def func_05_663():
    TalkBegin(0x00FE)
    OP_63(0x00FE)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_6BA',
    )

    ChrTalk(
        0x00FE,
        (
            '刚才游击士的大哥\n',
            '气势汹汹地跑了过来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '是发生什么事件了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_90B')

    def _loc_6BA(): pass

    label('loc_6BA')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_714',
    )

    ChrTalk(
        0x00FE,
        (
            '选定了新市长\n',
            '我的干劲也倍增了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '幸亏处理庭院树木\n',
            '和导力器没什么关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_90B')

    def _loc_714(): pass

    label('loc_714')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_75F',
    )

    ChrTalk(
        0x00FE,
        (
            '呼，我的肚子时钟\n',
            '说到吃饭时间了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '待会儿去厨房看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_90B')

    def _loc_75F(): pass

    label('loc_75F')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_7B7',
    )

    ChrTalk(
        0x00FE,
        (
            '唔，难得\n',
            '士兵大哥们来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '把庭园的树木整理成\n',
            '士兵的样子也挺好玩的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_90B')

    def _loc_7B7(): pass

    label('loc_7B7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0242, 4, 0x1214)),
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_881',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_7F9',
    )

    ChrTalk(
        0x00FE,
        (
            '既然是女王陛下的庭园，\n',
            '自然就有干劲了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_87E')

    def _loc_7F9(): pass

    label('loc_7F9')

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    ChrTalk(
        0x00FE,
        (
            '怎么说呢，这房子\n',
            '好像属于王国军了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '也就是说，我的雇主\n',
            '变成艾莉茜雅王陛下了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '嘿嘿，身为专业人士真是无上光荣啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_87E(): pass

    label('loc_87E')

    Jump('loc_90B')

    def _loc_881(): pass

    label('loc_881')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_90B',
    )

    ChrTalk(
        0x00FE,
        (
            '前市长被逮捕\n',
            '已经过去相当长的一段时间了啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我一直在这里工作，\n',
            '没问题吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说没有任何命令，\n',
            '可以毫不介意的工作。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_90B(): pass

    label('loc_90B')

    TalkEnd(0x00FE)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
