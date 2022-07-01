import sys
sys.path.append(r'D:\Dev\Source\Falcom\Decompiler2')

from Falcom.ED62.Parser.scena_writer_helper import *
try:
    import T4153_hook
except ModuleNotFoundError:
    pass

scena = createScenaWriter('T4153   ._SN')

stringTable = [
    TXT(0x00, '@FileName'),
    TXT(0x01, '科洛丝'),
    TXT(0x02, '提妲'),
    TXT(0x03, '玲'),
    TXT(0x04, '王国军士兵'),
    TXT(0x05, '王国军士兵'),
    TXT(0x06, '王都格兰赛尔·西街区'),
    TXT(0x07, '格兰赛尔城方面'),
    TXT(0x08, '王都格兰赛尔·东街区'),
    TXT(0x09, '王都格兰赛尔·南街区'),
    TXT(0x0A, ''),
]

# id: 0xFFFF offset: 0x0
@scena.Header('Header')
def Header():
    header = ScenaHeader()
    header.mapName        = 'Grancel'
    header.mapModel       = 'T4153.x'
    header.mapIndex       = 1
    header.bgm            = 34
    header.flags          = 0x0000
    header.entryFunction  = 0xFFFF
    header.importTable    = [0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF, 0xFFFFFFFF]
    header.reserved       = 0
    return header

# id: 0xFFFF offset: 0x1335
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
        ('ED6_DT07/CH00040._CH', 'ED6_DT07/CH00040P._CP'),
        ('ED6_DT07/CH00060._CH', 'ED6_DT07/CH00060P._CP'),
        ('ED6_DT27/CH03510._CH', 'ED6_DT27/CH03510P._CP'),
        ('ED6_DT07/CH01640._CH', 'ED6_DT07/CH01640P._CP'),
    ]

# id: 0x10002 offset: 0xCA
@scena.NpcData('NpcData')
def NpcData():
    return (
        ScenaNpcData(
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            x                   = 0,
            z                   = 0,
            y                   = 0,
            direction           = 0,
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
            direction           = 0,
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
            x                   = -6050,
            z                   = 0,
            y                   = 69190,
            direction           = 190,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0003,
        ),
        ScenaNpcData(
            x                   = 6050,
            z                   = 0,
            y                   = 69190,
            direction           = 190,
            word_0E             = 0,
            dword_10            = 3,
            chipIndex           = 3,
            npcIndex            = 0x0181,
            initFunctionIndex   = 0x0000,
            initScenaIndex      = 0x0002,
            talkFunctionIndex   = 0x0000,
            talkScenaIndex      = 0x0004,
        ),
        ScenaNpcData(
            x                   = -40080,
            z                   = 0,
            y                   = 17660,
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
        ScenaNpcData(
            x                   = 100,
            z                   = 0,
            y                   = 104130,
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
        ScenaNpcData(
            x                   = 40430,
            z                   = 0,
            y                   = 64060,
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
        ScenaNpcData(
            x                   = 20,
            z                   = 0,
            y                   = -3500,
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

# id: 0x10003 offset: 0x1EA
@scena.MonsterData('MonsterData')
def MonsterData():
    return (
    )

# id: 0x10004 offset: 0x1EA
@scena.EventData('EventData')
def EventData():
    return (
        ScenaEventData(
            x           = 18520,
            y           = 0,
            z           = 44050,
            range       = 1500,
            dword_10    = 0x000009C4,
            dword_14    = 0x00000000,
            dword_18    = 0x00000041,
            dword_1C    = 0x00000009,
        ),
    )

# id: 0x10005 offset: 0x20A
@scena.ActorData('ActorData')
def ActorData():
    return (
    )

# id: 0x0000 offset: 0x20A
@scena.Code('PreInit')
def PreInit():
    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x021E, 0, 0x10F0)),
            Expr.Return,
        ),
        'loc_226',
    )

    ExecExpressionWithVar(
        0x01,
        (
            (Expr.PushLong, 0x54),
            Expr.Nop,
            Expr.Return,
        ),
    )

    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 0x0005)

    def _loc_226(): pass

    label('loc_226')

    Return()

# id: 0x0001 offset: 0x227
@scena.Code('Init')
def Init():
    OP_16(0x02, 0x00000FA0, 0xFFFDE4F0, 0xFFFECF50, 0x0023005E)
    OP_1B(0x06, 0x00, 0x0007)
    OP_1B(0x07, 0x00, 0x0008)
    ClearChrFlags(0x000B, 0x0080)
    ClearChrFlags(0x000C, 0x0080)

    Return()

# id: 0x0002 offset: 0x24E
@scena.Code('ReInit')
def ReInit():
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
        'loc_273',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x00000672)

    Jump('loc_289')

    def _loc_273(): pass

    label('loc_273')

    If(
        (
            (Expr.PushReg, 0x1),
            (Expr.PushLong, 0x1),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_289',
    )

    OP_99(0x00FE, 0x01, 0x07, 0x00000640)

    def _loc_289(): pass

    label('loc_289')

    If(
        (
            (Expr.PushLong, 0x1),
            Expr.Return,
        ),
        'loc_29E',
    )

    OP_99(0x00FE, 0x00, 0x07, 0x000005DC)

    Jump('loc_289')

    def _loc_29E(): pass

    label('loc_29E')

    Return()

# id: 0x0003 offset: 0x29F
@scena.Code('func_03_29F')
def func_03_29F():
    TalkBegin(0x00FE)

    ChrTalk(
        0x000B,
        (
            '由于警戒体制的强化\n',
            '这里也被封锁了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '任何人都\n',
            '不准通过这里。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0004 offset: 0x2E8
@scena.Code('func_04_2E8')
def func_04_2E8():
    TalkBegin(0x00FE)

    ChrTalk(
        0x000C,
        (
            '这里不允许任何人通过。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '上面下达了指示，\n',
            '任何人都不准接近格兰赛尔城。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    TalkEnd(0x00FE)

    Return()

# id: 0x0005 offset: 0x33A
@scena.Code('func_05_33A')
def func_05_33A():
    EventBegin(0x00)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Ez,
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Ez,
            Expr.Nez64,
            Expr.Return,
        ),
        'loc_34D',
    )

    Call(0, 0x0006)

    def _loc_34D(): pass

    label('loc_34D')

    ClearChrFlags(0x0008, 0x0080)
    ClearChrFlags(0x0009, 0x0080)
    ClearChrFlags(0x000A, 0x0080)
    SetChrPos(0x0008, 5380, 0, 35040, 360)
    SetChrPos(0x0101, 6180, 0, 34540, 360)
    SetChrPos(0x00F7, 4690, 0, 34460, 360)
    SetChrPos(0x0009, 6190, 0, 33520, 360)
    SetChrPos(0x000A, 4770, 0, 33300, 360)
    OP_6D(6190, 250, 68540, 0)
    OP_67(0, 10150, -10000, 0)
    OP_6B(3270, 0)
    OP_6C(56000, 0)
    OP_6E(403, 0)

    @scena.Lambda('lambda_03F4')
    def lambda_03F4():
        OP_6D(9330, 250, 47830, 6000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_03F4)

    FadeIn(1000, 0)
    Sleep(2000)

    @scena.Lambda('lambda_041A')
    def lambda_041A():
        OP_8E(0x00FE, 5380, 0, 46040, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0008, 0x0001, lambda_041A)

    Sleep(300)

    @scena.Lambda('lambda_043A')
    def lambda_043A():
        OP_8E(0x00FE, 6120, 0, 44570, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_043A)

    Sleep(50)

    @scena.Lambda('lambda_045A')
    def lambda_045A():
        OP_8E(0x00FE, 4940, 0, 44600, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_045A)

    Sleep(100)

    @scena.Lambda('lambda_047A')
    def lambda_047A():
        OP_8E(0x00FE, 6180, 0, 43520, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_047A)

    Sleep(50)

    @scena.Lambda('lambda_049A')
    def lambda_049A():
        OP_8E(0x00FE, 4970, 0, 43300, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_049A)

    WaitForThreadExit(0x000A, 0x0001)
    OP_8C(0x0008, 180, 400)
    Fade(1000)
    OP_6D(5550, 0, 44780, 0)
    OP_67(0, 8070, -10000, 0)
    OP_6B(4059, 0)
    OP_6C(45000, 0)
    OP_6E(180, 0)
    OP_0D()

    ChrTalk(
        0x0101,
        (
            '#0010251517V#1006F好了……\n',
            '我们就到这里吧。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251518V科洛丝。\n',
            '小心点回去哦。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0060251519V#048F#5P呵呵，很近的\n',
            '没关系。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251520V#264F咦，姐姐？\n',
            '你住在这附近？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0008,
        (
            '#0060251521V#045F#5P啊，嗯嗯。\n',
            '住在亲属家里。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0060251522V#040F那么各位，我失陪了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_63F',
    )

    ChrTalk(
        0x0106,
        (
            '#0050251523V#051F#6P啊啊，明天见。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_667')

    def _loc_63F(): pass

    label('loc_63F')

    ChrTalk(
        0x0103,
        (
            '#0030251524V#021F#6P呵呵，辛苦了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_667(): pass

    label('loc_667')

    ChrTalk(
        0x0009,
        (
            '#0070251525V#061F#2P科洛丝姐姐，再见～～！',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0008, 0, 400)

    @scena.Lambda('lambda_06A4')
    def lambda_06A4():
        OP_6D(5630, 0, 47820, 3000)

        ExitThread()

    DispatchAsync(0x0101, 0x0000, lambda_06A4)

    OP_8E(0x0008, 5370, 0, 58780, 2500, 0x00)
    SetChrFlags(0x0008, 0x0080)
    OP_6D(6030, 0, 44520, 1800)
    OP_8C(0x0101, 225, 400)

    ChrTalk(
        0x0101,
        (
            '#0010251526V#1016F话说回来……\n',
            '闹得还真夸张呢。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251527V奥利维尔把\n',
            '穆拉先生都给找来了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x00F7, 90, 400)
    OP_8C(0x000A, 45, 400)

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_79A',
    )

    ChrTalk(
        0x0106,
        (
            '#0050251528V#051F#6P你不也是\n',
            '把那个记者也叫来了吗？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_7D3')

    def _loc_79A(): pass

    label('loc_79A')

    ChrTalk(
        0x0103,
        (
            '#0030251529V#027F#6P你不也是\n',
            '把记者先生都叫来了吗。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_7D3(): pass

    label('loc_7D3')

    ChrTalk(
        0x0101,
        (
            '#0010251530V#1008F啊哈哈……\n',
            '想着无所谓的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251531V玲你们怎样？',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x000A,
        (
            '#0220251532V#261F哈哈哈，很开心啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251533V饭菜也好吃\n',
            '还听到很多有趣的事。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0220251534V钢琴也特别好听。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0009,
        (
            '#0070251535V#061F#4P嗯嗯，奥利维尔先生\n',
            '的钢琴弹得很好啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0070251536V真有点吃惊呢。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_9F8',
    )

    ChrTalk(
        0x0101,
        (
            '#0010251537V#1016F嗯，好歹都是\n',
            '自称演奏家来的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251538V#1006F阿加特\n',
            '也还尽兴？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251539V和金先生他们\n',
            '好像闹得挺开心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0106, 0x0101, 400)

    ChrTalk(
        0x0106,
        (
            '#0050251540V#053F#6P和那家伙在一起\n',
            '可真是聊个没完啊。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050251541V#051F走了很多路也累了\n',
            '赶快回去休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_AE3')

    def _loc_9F8(): pass

    label('loc_9F8')

    ChrTalk(
        0x0101,
        (
            '#0010251537V#1016F嗯，好歹都是\n',
            '自称演奏家来的嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251543V#1006F雪拉姐\n',
            '也还尽兴？',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251539V和金先生他们\n',
            '好像闹得挺开心的。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    ChrTalk(
        0x0103,
        (
            '#0030251545V#027F#6P真的喝开了\n',
            '可就停不下来了嘛。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030251546V明天还有工作\n',
            '今天早点休息吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_AE3(): pass

    label('loc_AE3')

    ChrTalk(
        0x0101,
        (
            '#0010251547V#1006F是吗……',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0010251548V那么，我们也\n',
            '回去酒店的房间吧。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    OP_8C(0x0101, 90, 400)

    @scena.Lambda('lambda_0B3D')
    def lambda_0B3D():
        OP_8E(0x00FE, 18520, 750, 44050, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0B3D)

    Sleep(500)

    OP_8C(0x0009, 90, 400)

    @scena.Lambda('lambda_0B64')
    def lambda_0B64():
        OP_8E(0x00FE, 17200, 400, 44460, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0B64)

    Sleep(200)

    OP_8C(0x000A, 90, 400)

    @scena.Lambda('lambda_0B8B')
    def lambda_0B8B():
        OP_8E(0x00FE, 17240, 410, 43550, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0B8B)

    Sleep(500)

    @scena.Lambda('lambda_0BAB')
    def lambda_0BAB():
        OP_8E(0x00FE, 15900, 250, 44030, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x00F7, 0x0001, lambda_0BAB)

    OP_6D(18520, 750, 44050, 4000)
    WaitForThreadExit(0x0101, 0x0001)
    OP_6F(0x0004, 0)
    OP_70(0x0004, 0x0000003C)
    Sleep(1000)

    @scena.Lambda('lambda_0BEF')
    def lambda_0BEF():
        OP_8E(0x00FE, 20470, 750, 44050, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0101, 0x0001, lambda_0BEF)

    Sleep(500)

    FadeOut(1000, 0, -1)

    @scena.Lambda('lambda_0C19')
    def lambda_0C19():
        OP_8E(0x00FE, 20470, 750, 44050, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x0009, 0x0001, lambda_0C19)

    Sleep(500)

    @scena.Lambda('lambda_0C39')
    def lambda_0C39():
        OP_8E(0x00FE, 20470, 750, 44050, 2000, 0x00)

        ExitThread()

    DispatchAsync(0x000A, 0x0001, lambda_0C39)

    WaitForThreadExit(0x0101, 0x0001)
    OP_9F(0x0101, 0xFF, 0xFF, 0xFF, 0x00, 0x00000190)
    SetChrFlags(0x0101, 0x0080)
    OP_0D()
    OP_A2(0x10F0)
    NewScene('ED6_DT21/T4133._SN', 100, 0, 0)
    IdleLoop()

    Return()

# id: 0x0006 offset: 0xC71
@scena.Code('func_06_C71')
def func_06_C71():
    FadeOut(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    FormationDelMember(0x02, 0xFF)
    FormationDelMember(0x05, 0xFF)

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
        0,
        (
            TXT(0x00, '【◇选择雪拉扎德为队友】\n'),
            TXT(0x01, '【◇选择阿加特为队友】\n'),
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
    OP_56(0x00)

    Switch(
        (
            (Expr.PushReg, 0x0),
            Expr.Return,
        ),
        (0x00000000, 'loc_CEB'),
        (0x00000001, 'loc_CF1'),
        (-1, 'loc_CF7'),
    )

    def _loc_CEB(): pass

    label('loc_CEB')

    OP_A2(0x1200)

    Jump('loc_CF7')

    def _loc_CF1(): pass

    label('loc_CF1')

    OP_A2(0x1201)

    Jump('loc_CF7')

    def _loc_CF7(): pass

    label('loc_CF7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 0, 0x1200)),
            Expr.Return,
        ),
        'loc_D05',
    )

    FormationAddMember(ChrTable['雪拉扎德'], 0xF7, 0xFF)

    Jump('loc_D09')

    def _loc_D05(): pass

    label('loc_D05')

    FormationAddMember(ChrTable['阿加特'], 0xF7, 0xFF)

    def _loc_D09(): pass

    label('loc_D09')

    Return()

# id: 0x0007 offset: 0xD0A
@scena.Code('func_07_D0A')
def func_07_D0A():
    EventBegin(0x01)
    OP_4A(0x000B, 255)
    OP_8C(0x000B, 90, 400)

    ChrTalk(
        0x000B,
        (
            '#4190270284V哦，\n',
            '请别再往前进了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4190270285V由于警戒体制的强化\n',
            '这里也被封锁了。',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_FEA',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_EF2',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_D94',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_D9B')

    def _loc_D94(): pass

    label('loc_D94')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_D9B(): pass

    label('loc_D9B')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 3, 0x163B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_E14',
    )

    ChrTalk(
        0x0103,
        (
            '#0030270286V#022F（格兰赛尔城交给王国军\n',
            '应该没问题吧。)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270287V（我们还是赶快\n',
            '  去西街区那边吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_E75')

    def _loc_E14(): pass

    label('loc_E14')

    ChrTalk(
        0x0103,
        (
            '#0030270286V#022F（格兰赛尔城交给王国军\n',
            '应该没问题吧。)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270289V(我们就赶紧去码头吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_E75(): pass

    label('loc_E75')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EB1',
    )

    ChrTalk(
        0x0101,
        (
            '#0010270290V#1002F（嗯，是啊。）',
            TxtCtl.Enter,
        ),
    )

    ChrTurnDirection(0x0000, 0x0103, 400)
    CloseMessageWindow()

    Jump('loc_EEC')

    def _loc_EB1(): pass

    label('loc_EB1')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_EEC',
    )

    ChrTalk(
        0x0109,
        (
            '#0180270291V#1063F（啊啊，是啊。）',
            TxtCtl.Enter,
        ),
    )

    ChrTurnDirection(0x0000, 0x0103, 400)
    CloseMessageWindow()

    def _loc_EEC(): pass

    label('loc_EEC')

    OP_A2(0x0000)

    Jump('loc_FEA')

    def _loc_EF2(): pass

    label('loc_EF2')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_F08',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_F0F')

    def _loc_F08(): pass

    label('loc_F08')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_F0F(): pass

    label('loc_F0F')

    ChrTalk(
        0x0106,
        (
            '#0050270292V#050F（格兰赛尔城交给王国军\n',
            '应该没问题吧。)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270293V(我们就赶紧去码头吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FAC',
    )

    ChrTalk(
        0x0101,
        (
            '#0010270290V#1002F（嗯，是啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0000, 0x0103, 400)

    Jump('loc_FE7')

    def _loc_FAC(): pass

    label('loc_FAC')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_FE7',
    )

    ChrTalk(
        0x0109,
        (
            '#0180270291V#1063F（啊啊，是啊。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()
    ChrTurnDirection(0x0000, 0x0103, 400)

    def _loc_FE7(): pass

    label('loc_FE7')

    OP_A2(0x0000)

    def _loc_FEA(): pass

    label('loc_FEA')

    OP_90(0x0000, 0, 0, -1500, 3000, 0x00)
    OP_8C(0x000B, 180, 0)
    OP_4B(0x000B, 255)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0008 offset: 0x1011
@scena.Code('func_08_1011')
def func_08_1011():
    EventBegin(0x01)
    OP_4A(0x000C, 255)
    OP_8C(0x000C, 270, 400)

    ChrTalk(
        0x000C,
        (
            '#4200270296V请不要再继续前进了。',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#4200270297V上面有指示说，任何人都\n',
            '不得接近格兰赛尔城',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0000, 0, 0x0)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_12F6',
    )

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x0240, 1, 0x1201)),
            Expr.Return,
        ),
        'loc_11FE',
    )

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x2),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_10A0',
    )

    ChrTurnDirection(0x0103, 0x0001, 400)

    Jump('loc_10A7')

    def _loc_10A0(): pass

    label('loc_10A0')

    ChrTurnDirection(0x0103, 0x0000, 400)

    def _loc_10A7(): pass

    label('loc_10A7')

    If(
        (
            (Expr.TestScenaFlags, ScenaFlag(0x02C7, 3, 0x163B)),
            Expr.Ez,
            Expr.Return,
        ),
        'loc_1120',
    )

    ChrTalk(
        0x0103,
        (
            '#0030270286V#022F（格兰赛尔城交给王国军\n',
            '应该没问题吧。)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270287V（我们还是赶快\n',
            '  去西街区那边吧。）',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    Jump('loc_1181')

    def _loc_1120(): pass

    label('loc_1120')

    ChrTalk(
        0x0103,
        (
            '#0030270286V#022F（格兰赛尔城交给王国军\n',
            '应该没问题吧。)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0030270289V(我们就赶紧去码头吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    def _loc_1181(): pass

    label('loc_1181')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11BD',
    )

    ChrTalk(
        0x0101,
        (
            '#0010270290V#1002F（嗯，是啊。）',
            TxtCtl.Enter,
        ),
    )

    ChrTurnDirection(0x0000, 0x0103, 400)
    CloseMessageWindow()

    Jump('loc_11F8')

    def _loc_11BD(): pass

    label('loc_11BD')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_11F8',
    )

    ChrTalk(
        0x0109,
        (
            '#0180270291V#1063F（啊啊，是啊。）',
            TxtCtl.Enter,
        ),
    )

    ChrTurnDirection(0x0000, 0x0103, 400)
    CloseMessageWindow()

    def _loc_11F8(): pass

    label('loc_11F8')

    OP_A2(0x0000)

    Jump('loc_12F6')

    def _loc_11FE(): pass

    label('loc_11FE')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x5),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_1214',
    )

    ChrTurnDirection(0x0106, 0x0001, 400)

    Jump('loc_121B')

    def _loc_1214(): pass

    label('loc_1214')

    ChrTurnDirection(0x0106, 0x0000, 400)

    def _loc_121B(): pass

    label('loc_121B')

    ChrTalk(
        0x0106,
        (
            '#0050270292V#050F（格兰赛尔城交给王国军\n',
            '应该没问题吧。)',
            TxtCtl.Enter,
            TxtCtl.Clear,
            '#0050270293V(我们就赶紧去码头吧。)',
            TxtCtl.Enter,
        ),
    )

    CloseMessageWindow()

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x0),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12B8',
    )

    ChrTalk(
        0x0101,
        (
            '#0010270290V#1002F（嗯，是啊。）',
            TxtCtl.Enter,
        ),
    )

    ChrTurnDirection(0x0000, 0x0103, 400)
    CloseMessageWindow()

    Jump('loc_12F3')

    def _loc_12B8(): pass

    label('loc_12B8')

    If(
        (
            (Expr.PushValueByIndex, 0xA),
            (Expr.PushLong, 0x8),
            Expr.Equ,
            Expr.Return,
        ),
        'loc_12F3',
    )

    ChrTalk(
        0x0109,
        (
            '#0180270291V#1063F（啊啊，是啊。）',
            TxtCtl.Enter,
        ),
    )

    ChrTurnDirection(0x0000, 0x0103, 400)
    CloseMessageWindow()

    def _loc_12F3(): pass

    label('loc_12F3')

    OP_A2(0x0000)

    def _loc_12F6(): pass

    label('loc_12F6')

    OP_90(0x0000, 0, 0, -1500, 3000, 0x00)
    OP_8C(0x000C, 180, 0)
    OP_4B(0x000C, 255)
    Sleep(50)

    EventEnd(0x04)

    Return()

# id: 0x0009 offset: 0x131D
@scena.Code('func_09_131D')
def func_09_131D():
    SetPlaceName(0x00B4)

    Return()

def main():
    scena.run(globals())

if __name__ == '__main__':
    Try(main)
