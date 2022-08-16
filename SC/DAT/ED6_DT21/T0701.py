import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T0701_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T0701   ._SN')

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Rolent'
    header.mapModel       = 'T0701.x'
    header.mapIndex       = 9
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 'ED6_DT21/T0701_1._SN', 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
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
        ('ED6_DT07/CH01290._CH', 'ED6_DT07/CH01290P._CP'),
        ('ED6_DT07/CH01450._CH', 'ED6_DT07/CH01450P._CP'),
    ]

# id: 0x10001 offset: 0xBA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            name                = '赛希莉亚号',
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 0,
            chipIndex           = 0,
            npcIndex            = 0x0185,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            name                = '法布利',
            x                   = 43100,
            z                   = 4000,
            y                   = 31800,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            name                = '斯库拉特',
            x                   = 38670,
            z                   = 0,
            y                   = 50200,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            name                = '索斯摩夫',
            x                   = 28880,
            z                   = 0,
            y                   = 3000,
            direction           = 180,
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
            name                = '洛连特市街区',
            x                   = 35320,
            z                   = 0,
            y                   = -13920,
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

# id: 0x10002 offset: 0x15A
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10003 offset: 0x15A
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 37790,
            y           = 3000,
            z           = 40490,
            range       = 36410,
            dword_10    = 0x00001388,
            dword_14    = 0x000092D6,
            dword_18    = 0x00010000,
            dword_1C    = 0x00000004,
        ),
    )

# id: 0x10004 offset: 0x17A
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 38000,
            triggerZ            = 0,
            triggerY            = 30000,
            triggerRange        = 800,
            actorX              = 38000,
            actorZ              = 2200,
            actorY              = 30000,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0006,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 40000,
            triggerZ            = 4000,
            triggerY            = 41300,
            triggerRange        = 800,
            actorX              = 40000,
            actorZ              = 5500,
            actorY              = 41800,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0007,
            word_22             = 0x0000,
        ),
        ScenaActorData(
            triggerX            = 34500,
            triggerZ            = 0,
            triggerY            = 46570,
            triggerRange        = 800,
            actorX              = 35000,
            actorZ              = 1500,
            actorY              = 46570,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x0008,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1E6
@scena.Code('Init')
def Init():
    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0200)"),
            (Expr.Eval, "OP_29(0x0074, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_20A',
    )

    ChrSetPos(0x0009, 43080, 4000, 32060, 270)

    def _loc_20A(): pass

    label('loc_20A')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0080)"),
            Expr.Return,
        ),
        'loc_21A',
    )

    ChrClearFlags(0x000B, 0x0080)

    def _loc_21A(): pass

    label('loc_21A')

    Return()

# id: 0x0001 offset: 0x21B
@scena.Code('func_01_21B')
def func_01_21B():
    OP_16(0x02, 4000, -92000, -97000, 2293767)

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0200)"),
            (Expr.Eval, "OP_29(0x0074, 0x00, 0x10)"),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_245',
    )

    OP_71(0x000A, 0x0004)

    def _loc_245(): pass

    label('loc_245')

    OP_72(0x000B, 0x0004)

    If(
        (
            (Expr.PushValueByIndex, 0x4),
            (Expr.PushLong, 0x4),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_26B',
    )

    MapSetFlags(0x00000010)
    OP_11(0x4B, 0x4B, 0x96, 0, 65000, 0)

    def _loc_26B(): pass

    label('loc_26B')

    Return()

# id: 0x0002 offset: 0x26C
@scena.Code('func_02_26C')
def func_02_26C():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_281',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('func_02_26C')

    def _loc_281(): pass

    label('loc_281')

    Return()

# id: 0x0003 offset: 0x282
@scena.Code('func_03_282')
def func_03_282():
    TalkBegin(0x0009)

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_2E0',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，游击士们。\n',
            '刚才辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之也发生了不少事……\n',
            '请注意保密。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_539')

    def _loc_2E0(): pass

    label('loc_2E0')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0200)"),
            Expr.Return,
        ),
        'loc_336',
    )

    ChrTalk(
        0x00FE,
        (
            '请赶快\n',
            '调查船的里面吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我可是做好了被炒的准备\n',
            '在帮助你们哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_539')

    def _loc_336(): pass

    label('loc_336')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0100)"),
            Expr.Return,
        ),
        'loc_348',
    )

    Call(1, 0x0003)

    Jump('loc_539')

    def _loc_348(): pass

    label('loc_348')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0040)"),
            Expr.Return,
        ),
        'loc_3B4',
    )

    ChrTalk(
        0x00FE,
        (
            '你们在找索斯摩夫先生？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '唔～应该\n',
            '还在飞船坪吧……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '总之你们别灰心，\n',
            '去找找看吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_539')

    def _loc_3B4(): pass

    label('loc_3B4')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_449',
    )

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_412',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，猫找到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '真是的，你们还要为了这种\n',
            '委托忙到这么晚。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_446')

    def _loc_412(): pass

    label('loc_412')

    ChrTalk(
        0x00FE,
        (
            '嗯？你们在找\n',
            '库因特吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '那家伙\n',
            '去吃饭了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_446(): pass

    label('loc_446')

    Jump('loc_539')

    def _loc_449(): pass

    label('loc_449')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0008)"),
            Expr.Return,
        ),
        'loc_4A7',
    )

    ChrTalk(
        0x00FE,
        (
            '说看到了猫的人\n',
            '肯定是斯库拉特。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '你们去找他问问吧。\n',
            '他应该在仓库附近。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_539')

    def _loc_4A7(): pass

    label('loc_4A7')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_4B8',
    )

    Call(1, 0x0000)

    Jump('loc_539')

    def _loc_4B8(): pass

    label('loc_4B8')

    ChrTalk(
        0x00FE,
        (
            '虽然明知有可能没用，\n',
            '不过我还是在重新做检查。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '让乘客等着、\n',
            '自己闲着可不行。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过这雾还真厉害。\n',
            '连工作服也湿透了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_539(): pass

    label('loc_539')

    TalkEnd(0x0009)
    ChrClearFlags(0x0009, 0x0010)

    Return()

# id: 0x0004 offset: 0x542
@scena.Code('func_04_542')
def func_04_542():
    TalkBegin(0x000A)

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_5C1',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，游击士们。\n',
            '听说你们找到猫了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '法布利那家伙\n',
            '可松了一大口气。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽然我不知道\n',
            '他有什么好放心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7BD')

    def _loc_5C1(): pass

    label('loc_5C1')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0200)"),
            Expr.Return,
        ),
        'loc_60A',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，这么晚真是辛苦你们了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '怎么样？\n',
            '猫找到了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7BD')

    def _loc_60A(): pass

    label('loc_60A')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0100)"),
            Expr.Return,
        ),
        'loc_670',
    )

    ChrTalk(
        0x00FE,
        (
            '如果想调查定期船内部，\n',
            '就去找法布利商量吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他应该在甲板上，\n',
            '你们可以去看看。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7BD')

    def _loc_670(): pass

    label('loc_670')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0040)"),
            Expr.Return,
        ),
        'loc_6ED',
    )

    ChrTalk(
        0x00FE,
        (
            '哟，游击士们。\n',
            '碰到库因特了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '索斯摩夫那家伙\n',
            '也一定在飞船坪里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过我也有一会儿\n',
            '没见到他了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7BD')

    def _loc_6ED(): pass

    label('loc_6ED')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0010)"),
            Expr.Return,
        ),
        'loc_74E',
    )

    ChrTalk(
        0x00FE,
        (
            '猫的事你们可以去找\n',
            '操舵手库因特问问。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '他刚出去\n',
            '吃晚饭了，\n',
            '应该还在城里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7BD')

    def _loc_74E(): pass

    label('loc_74E')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x00, 0x08)"),
            Expr.Return,
        ),
        'loc_75F',
    )

    Call(1, 0x0001)

    Jump('loc_7BD')

    def _loc_75F(): pass

    label('loc_75F')

    ChrTalk(
        0x00FE,
        (
            '我和大家商量后觉得\n',
            '至少得重新检查一次。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不过，雾这么厉害，\n',
            '还是准备检查完毕就撤退。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7BD(): pass

    label('loc_7BD')

    TalkEnd(0x000A)

    Return()

# id: 0x0005 offset: 0x7C1
@scena.Code('func_05_7C1')
def func_05_7C1():
    TalkBegin(0x000B)

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x00, 0x10)"),
            Expr.Return,
        ),
        'loc_825',
    )

    ChrTalk(
        0x00FE,
        (
            '听说你们找到猫了～',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好像还和\n',
            '小猫在一起……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '哎呀～怪不得会\n',
            '这么热闹。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_87B')

    def _loc_825(): pass

    label('loc_825')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0100)"),
            Expr.Return,
        ),
        'loc_86C',
    )

    ChrTalk(
        0x00FE,
        (
            '好了，各位也请\n',
            '重新振奋精神吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '好了，加油吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_87B')

    def _loc_86C(): pass

    label('loc_86C')

    If(
        (
            (Expr.Eval, "OP_29(0x0074, 0x01, 0x0040)"),
            Expr.Return,
        ),
        'loc_87B',
    )

    Call(1, 0x0002)

    def _loc_87B(): pass

    label('loc_87B')

    TalkEnd(0x000B)

    Return()

# id: 0x0006 offset: 0x87F
@scena.Code('func_06_87F')
def func_06_87F():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '定期船飞船坪\n',
            '≡　开往王都格兰赛尔\n',
            '≡　开往柏斯市',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '※请勿携带易燃物和危险品\n',
            '　　　　『利贝尔飞船公社』',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0007 offset: 0x91B
@scena.Code('func_07_91B')
def func_07_91B():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　　　飞船坪塔台　　　　\n',
            '　※无关人员禁止入内　　\n',
            '  『利贝尔飞船公社』　',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0x00FF)

    Return()

# id: 0x0008 offset: 0x996
@scena.Code('func_08_996')
def func_08_996():
    FadeOut(300, 0, 100)
    TalkSetChrName('')
    SetMessageWindowPos(-1, -1, -1, -1)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '　※无关人员禁止入内　　\n',
            '  『利贝尔飞船公社』　',
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
