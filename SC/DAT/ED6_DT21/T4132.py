import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
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
        ('ED6_DT07/CH01220._CH', 'ED6_DT07/CH01220P._CP'),
        ('ED6_DT07/CH00050._CH', 'ED6_DT07/CH00050P._CP'),
        ('ED6_DT07/CH00020._CH', 'ED6_DT07/CH00020P._CP'),
    ]

# id: 0x10001 offset: 0xC2
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '福立兹',
            x                   = 6940,
            z                   = 0,
            y                   = 3300,
            direction           = 166,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '阿加特',
            x                   = 6100,
            z                   = 0,
            y                   = 1700,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '雪拉扎德',
            x                   = 6100,
            z                   = 0,
            y                   = 1700,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0006,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
    )

# id: 0x10002 offset: 0x122
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x122
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10004 offset: 0x122
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
            talkFunctionIndex   = 0x0002,
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
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x16A
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_178',
    )

    Jump('loc_197')

    def _loc_178(): pass

    label('loc_178')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 5, 0x161D)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_197',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_192',
    )

    ChrClearFlags(0x0009, 0x0080)

    Jump('loc_197')

    def _loc_192(): pass

    label('loc_192')

    ChrClearFlags(0x000A, 0x0080)

    def _loc_197(): pass

    label('loc_197')

    Return()

# id: 0x0001 offset: 0x198
@scena.Code('func_01_198')
def func_01_198():
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
        'loc_1B4',
    )

    OP_B1('t4132_y')

    Jump('loc_1BD')

    def _loc_1B4(): pass

    label('loc_1B4')

    OP_B1('t4132_n')

    def _loc_1BD(): pass

    label('loc_1BD')

    Return()

# id: 0x0002 offset: 0x1BE
@scena.Code('func_02_1BE')
def func_02_1BE():
    Call(0, 0x0003)

    Return()

# id: 0x0003 offset: 0x1C3
@scena.Code('func_03_1C3')
def func_03_1C3():
    TalkBegin(0x0008)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x02C8, 4, 0x1644)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_1D6',
    )

    Jump('loc_1FE')

    def _loc_1D6(): pass

    label('loc_1D6')

    Call(6, 0x0006)

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1ED',
    )

    OP_A9(0xCC)
    TalkEnd(0x0008)

    Return()

    def _loc_1ED(): pass

    label('loc_1ED')

    If(
        (
            (Expr.PushReg, 0x0),
            (Expr.PushLong, 0x0),
            Expr.Neq,
            Expr.Return,
        ),
        'loc_1FE',
    )

    TalkEnd(0x0008)

    Return()

    def _loc_1FE(): pass

    label('loc_1FE')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0400, 0, 0x2000)),
            Expr.Return,
        ),
        'loc_2BD',
    )

    ChrTalk(
        0x0008,
        (
            '多亏了女王陛下，\n',
            '营业才能继续。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '虽然没有导力器了，\n',
            '虽然我们一直在努力\n',
            '保持一如既往的服务水准……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '可只有暖气和照明\n',
            '确实什么也做不了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '希望导力器能够\n',
            '赶紧恢复……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6DF')

    def _loc_2BD(): pass

    label('loc_2BD')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 5, 0x163D)),
            Expr.Return,
        ),
        'loc_347',
    )

    ChrTalk(
        0x0008,
        (
            '艾丝蒂尔小姐，您要出发了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '下次来格兰赛尔城时\n',
            '也请您能光顾我们这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '我们全体工作人员\n',
            '都真心等候着我们的再会。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6DF')

    def _loc_347(): pass

    label('loc_347')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C5, 5, 0x162D)),
            Expr.Return,
        ),
        'loc_458',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02CC, 5, 0x1665)),
            Expr.Return,
        ),
        'loc_3A8',
    )

    ChrTalk(
        0x0008,
        (
            '玲小姐就是昨天和您\n',
            '一起住宿的那位小姐吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果我看到她\n',
            '会联络协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_455')

    def _loc_3A8(): pass

    label('loc_3A8')

    ChrTalk(
        0x0101,
        (
            '#1011F福立兹先生，\n',
            '你没看到玲吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '……玲小姐就是昨天和您\n',
            '一起住宿的那位小姐吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '不，她没\n',
            '来过这里……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F是吗……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果我看到她\n',
            '会联络协会的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02CC, 5, 0x1665))

    def _loc_455(): pass

    label('loc_455')

    Jump('loc_6DF')

    def _loc_458(): pass

    label('loc_458')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 1, 0x1621)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_4B0',
    )

    ChrTalk(
        0x0008,
        (
            '出门的客人都\n',
            '快要回来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哈哈，工作的时候一天\n',
            '很快就过去了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_6DF')

    def _loc_4B0(): pass

    label('loc_4B0')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 2, 0x161A)),
            Expr.Return,
        ),
        'loc_5A7',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C3, 5, 0x161D)),
            (Expr.TestScenaFlags, ScenaFlag(0x02C4, 7, 0x1627)),
            Expr.Or,
            Expr.Return,
        ),
        'loc_58E',
    )

    ChrTalk(
        0x0008,
        (
            '关于恐吓信，\n',
            '因为内容太过模糊，\n',
            '我就让自己不要太介意……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '现在游击士协会也在调查，\n',
            '我还是感觉很放心。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '看来我原先在心底里\n',
            '还是有点不安的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '如果有什么我们能帮忙的，\n',
            '我们一定尽心竭力。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_5A4')

    def _loc_58E(): pass

    label('loc_58E')

    ChrTalk(
        0x0008,
        (
            '呼，真没办法……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_5A4(): pass

    label('loc_5A4')

    Jump('loc_6DF')

    def _loc_5A7(): pass

    label('loc_5A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C1, 3, 0x160B)),
            Expr.Return,
        ),
        'loc_6DF',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C8, 4, 0x1644)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_675',
    )

    ChrTalk(
        0x0101,
        (
            '#1001F福立兹先生，你好～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哎呀，这不是艾丝蒂尔小姐吗……\n',
            '诞辰庆典之后就没见了吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '今天是来工作的吗？\n',
            '请随意。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#1015F（咦……？）',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '(是错觉吗？\n',
            '　他表情好像有点僵……)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    SetScenaFlags(ScenaFlag(0x02C8, 4, 0x1644))

    Jump('loc_6DF')

    def _loc_675(): pass

    label('loc_675')

    ChrTalk(
        0x0008,
        (
            '据说互不侵犯条约的签字仪式\n',
            '快到了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '最近有很多从外国\n',
            '来的客人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '哈哈，看来要忙碌起来了……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_6DF(): pass

    label('loc_6DF')

    TalkEnd(0x0008)

    Return()

# id: 0x0004 offset: 0x6E3
@scena.Code('func_04_6E3')
def func_04_6E3():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#0050250377V#050F艾丝蒂尔，你在干吗？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050250378V这里是我负责的吧。\n',
            '你赶快去其他地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x748
@scena.Code('func_05_748')
def func_05_748():
    TalkBegin(0x00FE)

    ChrTalk(
        0x00FE,
        (
            '#0030250379V#020F艾丝蒂尔，怎么了？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030250380V宾馆是我负责的啊。\n',
            '你赶快去其他地方。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0006 offset: 0x7AB
@scena.Code('func_06_7AB')
def func_06_7AB():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　　　　　事务室\n',
            '※无关人员请勿入内',
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
