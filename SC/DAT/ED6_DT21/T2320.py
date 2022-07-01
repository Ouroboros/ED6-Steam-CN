import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T2320_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T2320   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '珂蕾妲婆婆'),
    TXT(0x02, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Ruan'
    header.mapModel       = 'T2320.x'
    header.mapIndex       = 1
    header.bgm            = 15
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 'ED6_DT21/SUB000._SN', 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x526
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
        ('ED6_DT07/CH01010._CH', 'ED6_DT07/CH01010P._CP'),
    ]

# id: 0x10002 offset: 0xB2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = -4000,
            z                   = 500,
            y                   = 8800,
            direction           = 180,
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

# id: 0x10003 offset: 0xD2
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0xD2
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0xD2
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = -4040,
            triggerZ            = 500,
            triggerY            = 7530,
            triggerRange        = 400,
            actorX              = -4000,
            actorZ              = 2000,
            actorY              = 8800,
            flags               = 0x007E,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0002,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0xF6
@scena.Code('PreInit')
def PreInit():
    Return()

# id: 0x0001 offset: 0xF7
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0xF8
@scena.Code('ReInit')
def ReInit():
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

    OP_A9(0x6E)
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
            (Expr.TestScenaFlags, ScenaFlag(0x0405, 7, 0x202F)),
            Expr.Return,
        ),
        'loc_1F1',
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
            '最近有年轻人\n',
            '来学料理呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '以前的烹调法\n',
            '只要有个锅就能解决了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '只用暖炉的火\n',
            '就能做简单的料理了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_1EE')

    def _loc_1AC(): pass

    label('loc_1AC')

    ChrTalk(
        0x0008,
        (
            '最近有年轻人\n',
            '来学料理呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '大家好像\n',
            '都不知道火的用法呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1EE(): pass

    label('loc_1EE')

    Jump('loc_51A')

    def _loc_1F1(): pass

    label('loc_1F1')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2D6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_283',
    )

    ChrTalk(
        0x0008,
        (
            '没有导力器\n',
            '我倒不会感到为难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '放点柴火就能取暖，\n',
            '照明用油灯也足够了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '为什么大家那么紧张\n',
            '我真是完全不明白哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_A2(0x0000)

    Jump('loc_2D3')

    def _loc_283(): pass

    label('loc_283')

    ChrTalk(
        0x0008,
        (
            '没有导力器\n',
            '我倒不会感到为难。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '为什么大家那么紧张\n',
            '我真是完全不明白哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_2D3(): pass

    label('loc_2D3')

    Jump('loc_51A')

    def _loc_2D6(): pass

    label('loc_2D6')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0280, 0, 0x1400)),
            Expr.Return,
        ),
        'loc_391',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_33B',
    )

    ChrTalk(
        0x0008,
        (
            '选举最重要的\n',
            '就是候选人的人品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '以前就是失败在这里，\n',
            '这次一定要看清楚了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_38E')

    def _loc_33B(): pass

    label('loc_33B')

    OP_A2(0x0000)

    ChrTalk(
        0x0008,
        (
            '选举最重要的\n',
            '就是候选人的人品。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '这里没出问题的话，\n',
            '应该就万事顺利了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_38E(): pass

    label('loc_38E')

    Jump('loc_51A')

    def _loc_391(): pass

    label('loc_391')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 5, 0x121D)),
            Expr.Return,
        ),
        'loc_46D',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Return,
        ),
        'loc_3FB',
    )

    ChrTalk(
        0x0008,
        (
            '扎古有扎古自己\n',
            '的考虑吧。\n',
            '行动比什么都重要。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '动口不如动手。\n',
            '我就是这么教他的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_46A')

    def _loc_3FB(): pass

    label('loc_3FB')

    OP_A2(0x0000)

    ChrTalk(
        0x0008,
        (
            '选举临近了,\n',
            '村长似乎很忙……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '相比之下扎古\n',
            '在干什么呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '年轻人不工作，\n',
            '以前可是想都不敢想哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_46A(): pass

    label('loc_46A')

    Jump('loc_51A')

    def _loc_46D(): pass

    label('loc_46D')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0243, 2, 0x121A)),
            Expr.Return,
        ),
        'loc_4B9',
    )

    ChrTalk(
        0x0008,
        (
            '我孙女萨蒂在店前\n',
            '开花店呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不介意的话\n',
            '也去那边看看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_51A')

    def _loc_4B9(): pass

    label('loc_4B9')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 6, 0x1206)),
            Expr.Return,
        ),
        'loc_51A',
    )

    ChrTalk(
        0x0008,
        (
            '刚才在前面\n',
            '碰到巡回神父了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '好像是新上任的神父，\n',
            '实在太年轻了，让人大吃一惊呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_51A(): pass

    label('loc_51A')

    TalkEnd(0x0008)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
