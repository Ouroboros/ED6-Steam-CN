import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T3220_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T3220   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Zeiss'
    header.mapModel       = 'T3220.x'
    header.mapIndex       = 1
    header.bgm            = 15
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
        ('ED6_DT07/CH01020._CH', 'ED6_DT07/CH01020P._CP'),
    ]

# id: 0x10001 offset: 0xB2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '希玛',
            x                   = 2550,
            z                   = 250,
            y                   = 4470,
            direction           = 192,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
    )

# id: 0x10002 offset: 0xD2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0xD2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0xD2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 2440,
            triggerZ            = 250,
            triggerY            = 2960,
            triggerRange        = 400,
            actorX              = 2550,
            actorZ              = 1750,
            actorY              = 4470,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0xF6
@scena.Code('Init')
def Init():
    Return()

# id: 0x0001 offset: 0xF7
@scena.Code('func_01_F7')
def func_01_F7():
    Return()

# id: 0x0002 offset: 0xF8
@scena.Code('func_02_F8')
def func_02_F8():
    Call(0, 0x0003)

    Return()

# id: 0x0003 offset: 0xFD
@scena.Code('func_03_FD')
def func_03_FD():
    TalkBegin(0x0008)
    Call(6, 0x0004)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_117',
    )

    OP_A9(0xA0)
    TalkEnd(0x0008)

    Return()

    def _loc_117(): pass

    label('loc_117')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_128',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_128(): pass

    label('loc_128')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0402, 2, 0x2012)),
            Expr.Return,
        ),
        'loc_1F5',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1AC',
    )

    ChrTalk(
        0x0008,
        (
            '温泉的泵\n',
            '好像顺利恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '果然是中央工房的工程师\n',
            '修好的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '真希望也能顺便修\n',
            '一下我们的照明啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_1F2')

    def _loc_1AC(): pass

    label('loc_1AC')

    ChrTalk(
        0x0008,
        (
            '温泉的泵\n',
            '好像顺利恢复了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '果然是中央工房的工程师\n',
            '修好的吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1F2(): pass

    label('loc_1F2')

    Jump('loc_720')

    def _loc_1F5(): pass

    label('loc_1F5')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_32E',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_2B6',
    )

    ChrTalk(
        0x0008,
        (
            '呀，欢迎……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '定期船好象停了，\n',
            '现在客人很少。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '你们可能知道，\n',
            '我还有个很小的儿子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '靠我这个男人\n',
            '养活他有多辛苦啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……所以啊，\n',
            '请你们买点什么吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    Jump('loc_32B')

    def _loc_2B6(): pass

    label('loc_2B6')

    ChrTalk(
        0x0008,
        (
            '你们可能知道，\n',
            '我还有个很小的儿子。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '靠我这个男人\n',
            '养活他有多辛苦啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……所以啊，\n',
            '请你们买点什么吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_32B(): pass

    label('loc_32B')

    Jump('loc_720')

    def _loc_32E(): pass

    label('loc_32E')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C0, 0, 0x1600)),
            Expr.Return,
        ),
        'loc_43C',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_399',
    )

    ChrTalk(
        0x0008,
        (
            '只要有温泉疗养的客人来，\n',
            '我家就能过得去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我会尽量细水常流地\n',
            '努力到库安长大的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_439')

    def _loc_399(): pass

    label('loc_399')

    ChrTalk(
        0x0008,
        (
            '呼，真没办法……\n',
            '听说水温恢复正常了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '暂且可以放心了啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '只要有温泉疗养的客人来，\n',
            '我家就能过得去。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我会尽量细水常流地\n',
            '努力到库安长大的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_439(): pass

    label('loc_439')

    Jump('loc_720')

    def _loc_43C(): pass

    label('loc_43C')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0284, 0, 0x1420)),
            Expr.Return,
        ),
        'loc_528',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_4A7',
    )

    ChrTalk(
        0x0008,
        (
            '我们的店就好像是靠着\n',
            '温泉疗养生意过活的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果温泉不行了，\n',
            '那就等着关门打烊吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_525')

    def _loc_4A7(): pass

    label('loc_4A7')

    ChrTalk(
        0x0008,
        (
            '如果温泉不行了，\n',
            '那就等着关门打烊吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '拜托你们了，\n',
            '赶快想想办法。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我们的店就好像是靠着\n',
            '温泉疗养生意过活的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_525(): pass

    label('loc_525')

    Jump('loc_720')

    def _loc_528(): pass

    label('loc_528')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0282, 6, 0x1416)),
            Expr.Return,
        ),
        'loc_636',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_59B',
    )

    ChrTalk(
        0x0008,
        (
            '据说互不侵犯条约的签字仪式\n',
            '就要在艾尔贝离宫举行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '反正和我们这些平民\n',
            '也没什么关系……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_633')

    def _loc_59B(): pass

    label('loc_59B')

    ChrTalk(
        0x0008,
        (
            '因为最近店里比较闲，\n',
            '就经常读利贝尔通讯……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '据说互不侵犯条约的签字仪式很快\n',
            '就要在艾尔贝离宫举行了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '反正和我们这些平民\n',
            '也没什么关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_633(): pass

    label('loc_633')

    Jump('loc_720')

    def _loc_636(): pass

    label('loc_636')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0281, 2, 0x140A)),
            Expr.Return,
        ),
        'loc_720',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_690',
    )

    ChrTalk(
        0x0008,
        (
            '有新商品进来了，\n',
            '需要的话请看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '很适合当作旅游的纪念品哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_720')

    def _loc_690(): pass

    label('loc_690')

    ChrTalk(
        0x0008,
        (
            '啊啊…\n',
            '欢迎欢迎。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '有新商品进来了，\n',
            '需要的话请看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不过客人还真少啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '库安那小鬼不知道有没有\n',
            '好好地在外面招揽顾客。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))

    def _loc_720(): pass

    label('loc_720')

    TalkEnd(0x0008)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
