import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED6.Parser.scena_writer_helper import *
try:
    import T1511_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T1511   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '雷纳德'),
    TXT(0x02, '索菲娜'),
    TXT(0x03, '罗伊德'),
    TXT(0x04, '艾露凯'),
    TXT(0x05, '阿妮特'),
    TXT(0x06, '奥利维尔'),
    TXT(0x07, '奥利维尔'),
    TXT(0x08, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Bose'
    header.mapModel       = 'T1511.x'
    header.mapIndex       = 1
    header.bgm            = 84
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0xC00
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
            word_30         = 225,
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
        ('ED6_DT07/CH01270._CH', 'ED6_DT07/CH01270P._CP'),
        ('ED6_DT07/CH01690._CH', 'ED6_DT07/CH01690P._CP'),
        ('ED6_DT07/CH01023._CH', 'ED6_DT07/CH01023P._CP'),
        ('ED6_DT07/CH01180._CH', 'ED6_DT07/CH01180P._CP'),
        ('ED6_DT07/CH01210._CH', 'ED6_DT07/CH01210P._CP'),
        ('ED6_DT06/CH20050._CH', 'ED6_DT06/CH20050P._CP'),
    ]

# id: 0x10002 offset: 0xDA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 24400,
            z                   = 0,
            y                   = 9200,
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
            x                   = 14000,
            z                   = 0,
            y                   = 3600,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 1,
            chipIndex           = 1,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0005,
        ),
        ScenaNpcData(
            x                   = 49500,
            z                   = 200,
            y                   = 26230,
            direction           = 90,
            word_0E             = 0,
            dword_10            = 2,
            chipIndex           = 2,
            npcIndex            = 0x0155,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0008,
        ),
        ScenaNpcData(
            x                   = 54500,
            z                   = 0,
            y                   = 3400,
            direction           = 180,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0006,
        ),
        ScenaNpcData(
            x                   = 49900,
            z                   = 0,
            y                   = 5800,
            direction           = 135,
            word_0E             = 0,
            dword_10            = 4,
            chipIndex           = 4,
            npcIndex            = 0x0101,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0003,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0007,
        ),
        ScenaNpcData(
            x                   = 109100,
            z                   = 600,
            y                   = 5100,
            direction           = 270,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0156,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0xFFFF,
            talkScenaIndex      = 0xFFFF,
        ),
        ScenaNpcData(
            x                   = 110010,
            z                   = -500,
            y                   = 5150,
            direction           = 0,
            word_0E             = 0,
            dword_10            = 5,
            chipIndex           = 5,
            npcIndex            = 0x0156,
            initFunctionIndex   = 0xFFFF,
            initScenaIndex      = 0xFFFF,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0009,
        ),
    )

# id: 0x10003 offset: 0x1BA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1BA
@scena.EventData('EventData')
def EventData():
    return (
    )

# id: 0x10005 offset: 0x1BA
@scena.ActorData('ActorData')
def ActorData():
    return (
        ScenaActorData(
            triggerX            = 80610,
            triggerZ            = 0,
            triggerY            = 9100,
            triggerRange        = 1400,
            actorX              = 80610,
            actorZ              = 1500,
            actorY              = 9100,
            flags               = 0x007C,
            talkScenaIndex      = 0x0000,
            talkFunctionIndex   = 0x000B,
            word_22             = 0x0000,
        ),
    )

# id: 0x0000 offset: 0x1DE
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x007F, 2, 0x3FA)),
            Expr.Return,
        ),
        'loc_1EC',
    )

    ClearScenaFlags(ScenaFlag(0x007F, 2, 0x3FA))
    Event(0, 0x000A)

    def _loc_1EC(): pass

    label('loc_1EC')

    Return()

# id: 0x0001 offset: 0x1ED
@scena.Code('Init')
def Init():
    Return()

# id: 0x0002 offset: 0x1EE
@scena.Code('ReInit')
def ReInit():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_203',
    )

    OP_99(0x00FE, 0x00, 0x07, 1500)

    Jump('ReInit')

    def _loc_203(): pass

    label('loc_203')

    Return()

# id: 0x0003 offset: 0x204
@scena.Code('func_03_204')
def func_03_204():
    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_227',
    )

    OP_8D(0x00FE, 50200, 5000, 54800, 6300, 2000)

    Jump('func_03_204')

    def _loc_227(): pass

    label('loc_227')

    Return()

# id: 0x0004 offset: 0x228
@scena.Code('func_04_228')
def func_04_228():
    TalkBegin(0x0008)

    ChrTalk(
        0x00FE,
        (
            '要出去吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '晚上外出钓鱼的话，\n',
            '不带上导力灯可是看不清周围的哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0008)

    Return()

# id: 0x0005 offset: 0x278
@scena.Code('func_05_278')
def func_05_278():
    TalkBegin(0x0009)

    ChrTalk(
        0x00FE,
        (
            '你们的同伴看起来醉得很厉害，\n',
            '不要紧吧？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '不介意的话，\n',
            '我给他送点水吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x0009)

    Return()

# id: 0x0006 offset: 0x2CF
@scena.Code('func_06_2CF')
def func_06_2CF():
    TalkBegin(0x000B)

    ChrTalk(
        0x00FE,
        (
            '啊呀，晚上好。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '我也很想认识一下\n',
            '同在这里住宿的人。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '如果您不介意的话，\n',
            '请多来找我聊聊天吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000B)

    Return()

# id: 0x0007 offset: 0x340
@scena.Code('func_07_340')
def func_07_340():
    TalkBegin(0x000C)

    ChrTalk(
        0x00FE,
        (
            '母亲好像\n',
            '很喜欢这里的氛围呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '虽说最初\n',
            '推荐她来这里的是我……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '现在则是母亲主动要求\n',
            '要到这里来呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000C)

    Return()

# id: 0x0008 offset: 0x3B8
@scena.Code('func_08_3B8')
def func_08_3B8():
    TalkBegin(0x000A)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_4E3',
    )

    SetScenaFlags(ScenaFlag(0x0000, 0, 0x0))
    SetMessageWindowPos(72, 320, 56, 3)
    FadeOut(300, 0, 100)

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '罗伊德正在研究展开在桌面上的地图。\n',
            '好像是瓦雷利亚湖的地图。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    FadeIn(300, 0)

    ChrTalk(
        0x00FE,
        (
            '西侧的方向\n',
            '结构比较简单，\n',
            '在那边不会钓到什么鱼。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '东侧的港湾处鱼的数量会多点，\n',
            '不过都是一些小型的鱼类。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '在这两处的话，\n',
            '那个家伙可能不会出来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x00FE,
        (
            '果然还是要\n',
            '坚持陆钓啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_50C')

    def _loc_4E3(): pass

    label('loc_4E3')

    ChrTalk(
        0x00FE,
        (
            '这次我一定要\n',
            '把那个努西给钓上来……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_50C(): pass

    label('loc_50C')

    TalkEnd(0x000A)

    Return()

# id: 0x0009 offset: 0x510
@scena.Code('func_09_510')
def func_09_510():
    TalkBegin(0x000D)

    ChrTalk(
        0x00FE,
        (
            '#0040031173V嗯嗯……雪拉君……\n',
            '再这样下去我就……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x000D)

    Return()

# id: 0x000A offset: 0x549
@scena.Code('func_0A_549')
def func_0A_549():
    ClearMapFlags(0x00000001)
    EventBegin(0x00)
    FormationAddMember(0x02, 0xFF)
    SetChrPos(0x0101, 107680, 0, 5310, 90)
    SetChrPos(0x0103, 109180, 0, 6400, 180)
    SetChrPos(0x0102, 107620, 0, 6630, 135)
    CameraMove(107890, 0, 13120, 0)
    SetScenaFlags(ScenaFlag(0x0069, 6, 0x34E))
    OP_28(0x0038, 0x01, 0x0080)
    FadeIn(2000, 0)
    CameraMove(109120, 0, 5740, 3000)

    ChrTalk(
        0x000E,
        (
            '#0040031143V#038F啊……唔……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0040031144V唔……咕噜咕噜……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031145V#007F#6P啊～哈，醉得不成样子了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031146V我就知道这个奥利维尔\n',
            '是喝不过我们的雪拉姐的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_62(0x0103, 0x00000000, 2000, 0x26, 0x27, 0x000000FA, 0x02)
    Sleep(1200)

    ChrTalk(
        0x0103,
        (
            '#0030031147V#021F#5P呵呵，也不能这么说。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031148V最近一直忙于工作，\n',
            '今天我的酒瘾一下子爆发出来了㈱',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0102, 0x0103, 200)

    ChrTalk(
        0x0102,
        (
            '#0020031149V#017F喝了这么多还面不改色……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0020031150V#018F雪拉姐姐，\n',
            '难道你受过什么特殊的训练吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0102, 400)

    ChrTalk(
        0x0103,
        (
            '#0030031151V#020F#5P唔……可能是因为\n',
            '我从来都不会挑酒喝吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031152V加了蝎子的、毒蛇的，什么酒都喝过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031153V#021F越古怪的酒喝起来才越有滋味。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031154V#017F不……\n',
            '我觉得好像不是这样……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0101, 0x0103, 400)

    ChrTalk(
        0x0101,
        (
            '#0010031155V#009F#6P对了，这家伙该怎么处理？\n',
            '他暂时应该醒不过来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0103, 0x0101, 400)

    ChrTalk(
        0x0103,
        (
            '#0030031156V#026F#5P就让他好好睡下去吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031157V#022F……毕竟我们今晚\n',
            '很有可能和那些空贼正面交锋。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031158V还是不要让这种普通市民\n',
            '卷入这件事比较好啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031159V#004F#6P咦，难道雪拉姐你……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010031160V为了不让他跟着我们，\n',
            '所以才会特意把他灌醉的？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031161V#023F#5P哎……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031162V…………………………',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031163V#021F啊，那、那是当然的啦。\n',
            '这就是我深谋远虑的良苦用心啊。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031164V#509F#6P在这之前的『哎』是什么啊……',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031165V#018F之前明明那么享受。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031166V#026F#5P不说了，现在已经夜深了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031167V我们还是早点\n',
            '做好监视的准备吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031168V#507F#6P啊，岔开话题了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030031169V#022F#5P好啦，多说无用。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030031170V我们先到栈桥那里看看吧。\n',
            '说不定那些空贼很快会来到的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0102,
        (
            '#0020031171V#010F嗯，知道了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0101,
        (
            '#0010031172V#006F#6P那好，我们出发吧！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    FadeOut(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0101, 107480, 0, 9560, 0)
    SetChrPos(0x0103, 107480, 0, 9560, 0)
    SetChrPos(0x0102, 107480, 0, 9560, 0)
    CameraMove(107480, 0, 9560, 0)
    Sleep(500)

    FadeIn(1000, 0)
    EventEnd(0x00)
    ClearMapFlags(0x10000000)

    Return()

# id: 0x000B offset: 0xB9D
@scena.Code('func_0B_B9D')
def func_0B_B9D():
    FadeOut(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName('')

    Talk(
        (
            (TxtCtl.SetColor, 0x5),
            '钓鱼工具并排摆在架子上。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_56(0x00)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeIn(300, 0)
    TalkEnd(0x00FF)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
